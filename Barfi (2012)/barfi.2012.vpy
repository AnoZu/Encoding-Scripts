from vstools import core, finalize_clip
from vsmuxtools import src_file, SourceFilter, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output

setup = Setup("movie")

# Clip
src = src_file(R".\Barfi.2012.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv", preview_sourcefilter=SourceFilter.BESTSOURCE, sourcefilter=SourceFilter.BESTSOURCE)
clip = src.init()

src2 = src_file(R"D:\media\Barfi! (2012) (1080p BluRay DDP 5.1 Hindi x265) [AnoZu].mkv", preview_sourcefilter=SourceFilter.BESTSOURCE, sourcefilter=SourceFilter.BESTSOURCE)
clip2 = src2.init()

# Crop black bars
crop = core.std.Crop(clip, top=132, bottom=132)

# Final
final = finalize_clip(crop, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=20,
        aq_strength=0.75, psy_rd=1.3, psy_rdoq=1.5,
        qcomp=0.6, rd=4, cutree=True,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=16,
        aq_mode=3, chroma_qpoffsets=-2,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="hi-IN", default=True),
        tmdb=TmdbConfig(127501, movie=True, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )
#else:
    #set_output(final)

set_output(final, "BD")
set_output(clip2, "AnoZu")