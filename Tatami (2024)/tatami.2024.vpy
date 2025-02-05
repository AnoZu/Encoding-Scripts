from vstools import core, replace_ranges, finalize_clip
import vstools
from rekt import rektlvls
from vsmuxtools import src_file, Setup, SourceFilter, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output

setup = Setup("movie")

# Clip
src = src_file(R".\Tatami.2023.1080p.Blu-ray.Remux.AVC.DTS-HD.MA.5.1-CiNEPHiLES.mkv", preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
clip = src.init()

# Filter ranges
dirty_bord_range = [(1214, 138583), (138743, 141145)]
deb_range = [(0, 264), (425, 623)]

# Clean dirty borders
cb = rektlvls(clip, colnum=[239, 240, 1679, 1680], colval=[-100, 13, 13, -100])
cbfin = replace_ranges(clip, cb, dirty_bord_range)

# Deband intro
clip32 = vstools.depth(cbfin, 32)
default_mpv_deband = core.placebo.Deband(clip32, planes=7, iterations=4, threshold=3.44, radius=16.0, grain=0.5)
deb16 = vstools.depth(default_mpv_deband, 16)
debfin = replace_ranges(cbfin, deb16, deb_range)

# Final
final = finalize_clip(debfin, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=18.8,
        aq_strength=0.75, psy_rd=1.3, psy_rdoq=1.5,
        qcomp=0.6, rd=4,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=16,
        aq_mode=3, chroma_qpoffsets=-2,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="fa", default=True),
        tmdb=TmdbConfig(1084066, movie=True, language="en-US", write_cover=True),
    )
else:
    set_output(final)