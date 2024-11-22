from vstools import core, replace_ranges, finalize_clip
import vsdeband as vsdb
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output

setup = Setup("movie")

# Clip
src = src_file(r"D:\media\Next.Sohee.2022.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-RMS.mkv", force_bs=True)
clip = src.init()

deb_range = (0, 134)

# Crop black bars
crop = core.std.Crop(clip, top=22, bottom=22)

# Deband intro
deb = vsdb.Placebo.deband(crop, radius=32, thr=6, iterations=4)

prefin = replace_ranges(crop, deb, deb_range)

final = finalize_clip(prefin, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=20,
        aq_strength=0.76, psy_rd=2.0, psy_rdoq=1.5,
        qcomp=0.7, rd=4,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=12,
        aq_mode=3, chroma_qpoffsets=-2,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="ko", default=True),
        tmdb=TmdbConfig(923344, movie=True, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )
else:
    set_output(final)