from vstools import core, finalize_clip, replace_ranges
from vsdenoise import MVToolsPreset, Prefilter, mc_degrain, bm3d, nl_means
import vskernels as vsk
from vodesfunc import adaptive_grain
from vsmuxtools import src_file, SourceFilter, Setup, x265, sb265, TmdbConfig, mux
from vspreview import is_preview, set_output


setup = Setup(
    "movie",
    None,
    show_name="2 States (2014)",
    out_dir=R".\premux",
    mkv_title_naming=R"$show$ (1080p Bluray DDP 5.1 Hindi x265) [AnoZu]",
    out_name=R"$show$ (1080p Bluray DDP 5.1 Hindi x265) [AnoZu]",
    clean_work_dirs=False,
    debug=True,
)


# Clip
src = src_file(R".\2.States.2014.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv", preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
clip = src.init()

# Filter range
flrange = (2568, 205332)

# Crop black bars
crop = core.std.Crop(clip, top=132, bottom=132)

# Denoise
ref = mc_degrain(crop, prefilter=Prefilter.DFTTEST(), preset=MVToolsPreset.HQ_SAD, thsad=100)

denoise_y = bm3d(crop, sigma=1, tr=2, profile=bm3d.Profile.NORMAL, ref=ref, planes=0)

denoise_uv = nl_means(denoise_y, 0.2, tr=2, ref=ref, planes=[1, 2])

# Grain
grain = adaptive_grain(denoise_uv, strength=[3, 0.75], size=3.4, type=2, scale=0.7, scaler=vsk.Bicubic(b=-0.4, c=0.2), temporal_average=50, luma_scaling=4, static=False)

# Final
prefin = replace_ranges(crop, grain, flrange)
    
final = finalize_clip(prefin, 10)


if is_preview():
    set_output(clip)
    set_output(crop)
    set_output(denoise_y)
    set_output(denoise_uv)
    set_output(grain)
    set_output(final)

else:    
    settings = sb265(
        crf=19,
        aq_strength=0.8, psy_rd=2, psy_rdoq=1.5,
        qcomp=0.7, rd=4,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=16,
        aq_mode=3,
        rect=False
    )
    zones = [(0, 2567, 0.5), (205333, 214895, 0.5)]
    enc = x265(settings, zones).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="und", default=True),
        tmdb=TmdbConfig(259720, movie=True, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )