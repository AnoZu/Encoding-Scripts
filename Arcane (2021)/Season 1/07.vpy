from vstools import core, vs, finalize_clip, replace_ranges
import awsmfunc as awf
import vsdehalo as vsdh
from vsmuxtools import src_file, GlobSearch, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


for i in range(7, 8):
    # Basic Setup for every episode without a config file
    setup = Setup(
        f"{i:02d}",  # Format to have padded zeros
        None,
        show_name="Arcane (2021)",
        out_dir=R".\premux",
        mkv_title_naming=R"$show$ S01E$ep$ $title$ (1080p Bluray DDP 5.1 x265) [AnoZu]",
        out_name=R"$show$ S01E$ep$ $title$ (1080p Bluray DDP 5.1 x265) [AnoZu]",
        clean_work_dirs=False,
        debug=True,
    )

    # Load clip
    clip = src_file(GlobSearch(f"*Arcane*.S01E{setup.episode}*.mkv", dir=R"D:\data\torrents"), force_bs=True)
    clip1 = clip.init()

    # Filter range
    flrange = (24, 52099)

    # Crop black bars
    crop = core.std.Crop(clip1, top=132, bottom=132)

    # Clean dirty borders
    bb = awf.bbmod(crop, top=2, bottom=1, thresh=128, blur=20)

    # Clean edges
    dh = vsdh.edge_cleaner(bb)

    prefin = replace_ranges(crop, dh, flrange)
    
    final = finalize_clip(prefin, 10)
    

    if __name__ == "__main__":
        settings = settings_builder_x265(
            crf=15,
            aq_strength=0.85, psy_rd=2.0, psy_rdoq=2,
            qcomp=0.72, rd=4,
            preset="slower",
            deblock=[-2, -2], ref=5, bframes=8,
            aq_mode=3,
            rect=False
        )
        enc = x265(settings).encode(final)
        mux(
            enc.to_track(name="Encoded by AnoZu", lang="en-US", default=True),
            tmdb=TmdbConfig(94605, season=1, language="en-US", write_ids=True, write_title=False, write_cover=True),
        )
    else:
        set_output(final)