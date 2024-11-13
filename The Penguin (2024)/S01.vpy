from vstools import core, vs, finalize_clip
from vskernels import Hermite
from vsmuxtools import src_file, GlobSearch, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


for i in range(1, 9):
    # Basic Setup for every episode without a config file
    setup = Setup(
        f"{i:02d}",  # Format to have padded zeros
        None,
        show_name="The Penguin (2024)",
        out_dir=R".\premux",
        mkv_title_naming=R"$show$ S01E$ep$ $title$ 1080p - AnoZu",
        out_name=R"$show$ S01E$ep$ $title$ (1080p DS4K MAX WEBRip x265 SDR DDP 5.1 Atmos English -AnoZu)",
        clean_work_dirs=False,
        debug=True,
    )

    WEBDL_4K = src_file(GlobSearch(f"*Penguin.S01E{setup.episode}*.mkv", dir=r"D:\media\The.Penguin.S01.2160p.MAX.WEB-DL.DDP5.1.Atmos.DV.H.265-Kitsune"), force_bs=True)
    webdl_4k = WEBDL_4K.init()

    yuv444p16 = core.resize.Lanczos(webdl_4k, format=vs.YUV444P16)
    tnmp = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=4, metadata=0, use_dovi=True, contrast_recovery=0.0)

    yuv420p16 = core.resize.Bicubic(tnmp, format=vs.YUV420P16, range=0)

    frameprops = core.std.SetFrameProps(yuv420p16, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)

    ds4k = Hermite.scale(frameprops, width=1920, height=960, linear=True)

    final = finalize_clip(ds4k, 10)

    if __name__ == "__main__":
        settings = settings_builder_x265(
            crf=18,
            aq_strength=0.75, psy_rd=2.0, psy_rdoq=2,
            qcomp=0.7, rd=4,
            preset="slower",
            deblock=[-3, -3], ref=5, bframes=12,
            aq_mode=5,
            rect=False
        )
        enc = x265(settings).encode(final)
        mux(
            enc.to_track(name="Encoded by AnoZu", lang="en-US", default=True),
            tmdb=TmdbConfig(194764, season=1, language="en-US", write_ids=True, write_title=True, write_cover=True),
        )
    else:
        set_output(final)