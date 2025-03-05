from vstools import core, depth, get_y, split, join, replace_ranges, finalize_clip
from vsdenoise import BM3DCudaRTC, nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, Profile
import vsdeband as vsdb
import vsscale
import vsmlrt
import vskernels as vsk
from vodesfunc import adaptive_grain
from vsmuxtools import src_file, GlobSearch, Setup, SourceFilter, x265, settings_builder_x265, do_audio, Opus, mux
from vspreview import set_output


setup = Setup("06")

op_ed_range = [(0, 2145), (32626, 34764)]


# Clip
debd = src_file(GlobSearch(f"*Jigokuraku - {setup.episode}*.mkv"), preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
debd_init = debd.init()
bd = debd_init[360:]

#usbd = src_file(GlobSearch(f"*Paradise.S01E{setup.episode}*.mkv"), preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
#usbd_init = usbd.init()

#vodes = src_file(GlobSearch(f"*Jigokuraku - S01E{setup.episode} v2*.mkv"), preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
#vodes_init = vodes.init(bits=10)
#vodes = vodes_init[360:]

# Denoise
mvref = MVTools.denoise(bd, thSAD=100, tr=2, prefilter=Prefilter.BM3D, block_size=32, overlap=16, motion=MotionMode.HIGH_SAD, sad_mode=SADMode.SPATIAL.same_recalc, search=SearchMode.DIAMOND.defaults)
den_y = BM3DCudaRTC.denoise(bd, sigma=1, tr=2, profile=Profile.FAST, ref=mvref, planes=0)
den_uv = nlm.nl_means(bd, strength=0.25, tr=2, sr=2, device_type=DeviceType.CUDA, ref=mvref, planes=[1, 2])
den = join(den_y, den_uv)

# Descale
den32 = depth(den, 32)
deny, denu, denv = split(den32)
desc = vsk.Bilinear.descale(deny, width=1500, height=844, src_top=0.125, src_height=843.75, src_left=0, src_width=1500)
double = vsscale.ArtCNN.R8F64(backend=vsmlrt.Backend.ORT_CUDA).multi(desc)
resc = vsk.Hermite.scale(double, 1920, 1080, linear=True, keep_ar=True)
rescj = join(resc, denu, denv)
rescd = depth(rescj, 16)
rescf = replace_ranges(rescd, den, op_ed_range)

# Deband
rescf32 = depth(rescf, 32)
deb_mask = vsdb.deband_detail_mask(get_y(rescf), brz=(0.1, 0.1))
deb = core.placebo.Deband(rescf32, planes=7, iterations=4, threshold=3.44, radius=16.0)
deb16 = depth(deb, 16)
debf = core.std.MaskedMerge(deb16, rescf, deb_mask)

# Regrain
grain = adaptive_grain(debf, strength=[1.8, 0], size=3.4, type=2, scale=0.7, scaler=vsk.Bicubic(b=-0.4, c=0.2), temporal_average=50, luma_scaling=4, static=False)

# Final
final = finalize_clip(grain, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=16,
        aq_strength=0.85, psy_rd=2, psy_rdoq=2,
        qcomp=0.72, cutree=False,
        preset="slower", chroma_qpoffsets=-2,
        deblock=[-2, -2], ref=5, bframes=16,
        aq_mode=3,
        rect=False
    )
    zones = [(0, 2145, 1.1), (32626, 34764, 1.1)]
    enc = x265(settings, zones).encode(final)
    audio = do_audio(debd, 0, trims=(360, None), encoder=Opus(bitrate=192, vbr=True))
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="ja", default=True),
        audio.to_track(name="Japanese 2.0", lang="ja", default=True),
    )
else:
    set_output(final)

#set_output(bd, "DEBD")
#set_output(vodes, "Vodes")
#set_output(usbd_init, "USBD")
#set_output(anozu, "AnoZu")
#set_output(den)
#set_output(rescf)
#set_output(deb_mask)
#set_output(deb)
#set_output(debf)
#set_output(grain)
#set_output(final)
#set_output(den_y)
#set_output(den_uv)
#set_output(desc)
#set_output(double)
#set_output(resc)
#set_output(denf)
#set_output(aa)
#set_output(dhfin)
#set_output(deb)
#set_output(grain)