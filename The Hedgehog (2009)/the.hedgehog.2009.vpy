from vstools import core, replace_ranges, join, finalize_clip
import vsdeband as vsdb
from vsdenoise import BM3DCudaRTC, nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, PelType, Profile, temporal_degrain
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output

setup = Setup("movie")

# Clip
src = src_file(r"D:\media\Le.hérisson.AKA.The.Hedgehog.2009.1080p.BluRay.Remux.AVC.DTS-HD.MA.5.1-SwRd.mkv", force_bs=True)
clip = src.init()

fl_range = [(48, 334), (1094, 133170)]

# Crop black bars
crop = core.std.Crop(clip, top=132, bottom=132)

# Denoise
mvref = MVTools.denoise(crop, thSAD=150, tr=2, prefilter=Prefilter.BM3D, block_size=32, overlap=16, pel_type=PelType.WIENER, motion=MotionMode.HIGH_SAD, sad_mode=SADMode.SPATIAL.same_recalc, search=SearchMode.DIAMOND.defaults)
den_y = BM3DCudaRTC.denoise(crop, sigma=2.5, tr=2, refine=2, profile=Profile.FAST, ref=mvref, planes=0)
den_uv = nlm.nl_means(crop, strength=0.8, tr=2, sr=2, device_type=DeviceType.CUDA, ref=mvref, planes=[1, 2])
denf = join(den_y, den_uv)

# Regrain
grains = core.grain.Add(denf, var=0.2, uvar=0.1, seed=1, constant=True)
graind = core.grain.Add(grains, var=0.4, uvar=0.1, seed=2, constant=False)

# Final
final = finalize_clip(replace_ranges(crop, graind, fl_range), bits=10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=20,
        aq_strength=0.8, psy_rd=2, psy_rdoq=2,
        qcomp=0.7, rd=4,
        preset="slower", tu_inter_depth=4, tu_intra_depth=4,
        deblock=[-3, -3], ref=5, bframes=10,
        aq_mode=3, chroma_qpoffsets=-2,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="fr", default=True),
        tmdb=TmdbConfig(19597, movie=True, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )
else:
    set_output(final)

#set_output(clip)
#set_output(crop)
#set_output(denf)
#set_output(grains)
#set_output(graind)