from vstools import core, finalize_clip
from vsmuxtools import src_file, SourceFilter, Setup, x265, settings_builder_x265, do_audio, Opus, mux
from vspreview import set_output

setup = Setup("movie")

# Clip
src = src_file(R"D:\data\usenet\complete\Lion.2016.Hybrid.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-BLURANiUM\Lion.2016.Hybrid.1080p.BluRay.REMUX.AVC.DTS-HD.MA.5.1-BLURANiUM.mkv", preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
clip = src.init()

# Crop black bars
crop = core.std.Crop(clip, top=140, bottom=140)

# Final
final = finalize_clip(crop, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=17.5,
        aq_strength=0.8, psy_rd=2, psy_rdoq=1.5,
        qcomp=0.7, rd=4,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=16,
        aq_mode=3, chroma_qpoffsets=-2,
        rect=False
    )
    enc = x265(settings).encode(final)
    comm1 = do_audio(src, 1, encoder=Opus(bitrate=192, vbr=True))
    comm2 = do_audio(src, 2, encoder=Opus(bitrate=192, vbr=True))
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="en", default=True),
        comm1.to_track(name="Commentary by director Garth Davis", lang="en", default=False),
        comm2.to_track(name="Commentary by Sargoo Brierley and Sue Brierley", lang="en", default=False),
    )
else:
   set_output(final)