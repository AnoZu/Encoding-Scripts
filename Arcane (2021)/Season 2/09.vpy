from vstools import core, vs, depth, finalize_clip, replace_ranges
import vsdehalo as vsdh
from vsmuxtools import src_file, GlobSearch, SourceFilter, Setup, x265, sb265, TmdbConfig, mux
from vspreview import is_preview, set_output


setup = Setup(
    "09",
    None,
    show_name="Arcane (2021)",
    out_dir=R".\premux",
    mkv_title_naming=R"$show$ S02E$ep$ $title$ (1080p Bluray DDP Atmos 7.1 x265) [AnoZu]",
    out_name=R"$show$ S02E$ep$ $title$ (1080p Bluray DDP Atmos 7.1 x265) [AnoZu]",
    clean_work_dirs=False,
    debug=True,
)

# Load clip
clip = src_file(GlobSearch(f"*S02E{setup.episode}*.mkv"))
clip1 = clip.init()

# Filter range
flrange = (24, 67665)

# Crop black bars
crop = core.std.Crop(clip1, top=132, bottom=132)

# Clean edges
dh = vsdh.edge_cleaner(crop, 2, 12)

prefin = replace_ranges(crop, dh, flrange)
    
final = finalize_clip(prefin, 10)


if is_preview():
    set_output(clip1)
    set_output(crop)
    set_output(final)

else:    
    settings = sb265(
        crf=15,
        aq_strength=0.85, psy_rd=2, psy_rdoq=2,
        qcomp=0.72, rd=4,
        preset="slower",
        deblock=[-2, -2], ref=5, bframes=8,
        aq_mode=3,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="en-US", default=True),
        tmdb=TmdbConfig(94605, season=2, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )