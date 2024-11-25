from vstools import core, finalize_clip
import awsmfunc as awf
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


setup = Setup("movie")


# Clip
src = src_file(r"D:\media\The.Wild.Robot.2024.1080p.Blu-ray.Remux.AVC.TrueHD.Atmos.7.1-CiNEPHiLES.mkv", force_bs=True)
clip = src.init()

# Crop black bars
crop = core.std.Crop(clip, top=138, bottom=138)

# Clean dirty border
bb = awf.bbmod(crop, top=1, bottom=1, thresh=128, blur=20)

final = finalize_clip(bb, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=19,
        aq_strength=0.85, psy_rd=2.0, psy_rdoq=2,
        qcomp=0.7, rd=4,
        preset="slower",
        deblock=[-2, -2], ref=5, bframes=12,
        aq_mode=3, chroma_qpoffsets=-3,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="en", default=True),
        tmdb=TmdbConfig(1184918, movie=True, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )
else:
    set_output(final)