from vstools import core, depth, finalize_clip
from vsmuxtools import src_file, SourceFilter, Setup, x265, sb265, do_audio, mux
from vspreview import is_preview, set_output

setup = Setup(
    "movie",
    config_file=None,
    show_name= "Influencer (2023)",
    out_name= "$show$ (1080p BluRay DDP 5.1 English x265) [AnoZu]",
    mkv_title_naming= "$show$ 1080p BluRay DDP 5.1 English x265 - AnoZu",
)

# Clip
src = src_file(R".\Influencer.2022.1080p.Blu-ray.Remux.AVC.DTS-HD.MA.5.1-CiNEPHiLES.mkv", preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
clip = src.init()

# Crop black bars
crop = core.std.Crop(clip, top=138, bottom=138)

# Clean dirty borders
cleaned = core.bore.SinglePlane(depth(crop, 32), left=0, right=0, top=2, bottom=2, weight_mask=None, plane=0)

# Final
final = finalize_clip(cleaned, 10)

if is_preview():
    set_output(clip)
    set_output(crop)
    set_output(cleaned)

else:    
    settings = sb265(
        crf=19.5,
        aq_strength=0.8, psy_rd=2, psy_rdoq=1.5,
        qcomp=0.7, rd=4,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=16,
        aq_mode=3, chroma_qpoffsets=-2,
        rect=False
    )
    enc = x265(settings).encode(final)
    comm1 = do_audio(src, 1)
    comm2 = do_audio(src, 2)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="und", default=True),
        comm1.to_track("Commentary by director/co-writer Kurtis David Harder and cinematographer David Schuurman", lang="en", default=False),
        comm2.to_track("Commentary by director/co-writer Kurtis David Harder, and actresses Emily Tennant and Cassandra Naud", lang="en", default=False),
    )