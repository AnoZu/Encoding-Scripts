from vstools import core, vs, finalize_clip
from vskernels import Hermite
from vsmuxtools import src_file, GlobSearch, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


for i in range(4, 5):
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

    #WEBDL = src_file(GlobSearch(f"*Shekhar* S01E{setup.episode}*.mkv", dir=R"D:\data\torrents\Shekhar Home (2024) Complete Season S01 2160p WEB-DL x264 Multi AAC DD+ 5.1 ESub-JA"), force_bs=True)
    WEBDL_4K = src_file(r"D:\data\torrents\The.Penguin.S01E04.Centanni.2160p.MAX.WEB-DL.DDP5.1.Atmos.DV.H.265-Kitsune.mkv", force_bs=True)
    webdl_4k = WEBDL_4K.init()

    yuv444p16 = core.resize.Lanczos(webdl_4k, format=vs.YUV444P16)
    #tnmp0 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=0, metadata=0, use_dovi=True, contrast_recovery=0.3)
    #tnmp1 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=1, metadata=0, use_dovi=True, contrast_recovery=0.3)
    #tnmp2 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=2, metadata=0, use_dovi=True, contrast_recovery=0.3)
    #tnmp3 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=3, metadata=0, use_dovi=True, contrast_recovery=0.3)
    tnmp4 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=4, metadata=0, use_dovi=True, contrast_recovery=0.0)
    #tnmp5 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=5, metadata=0, use_dovi=True, contrast_recovery=0.3)
    #tnmp6 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=6, metadata=0, use_dovi=True, contrast_recovery=0.3)
    #tnmp10 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=10, metadata=0, use_dovi=True, contrast_recovery=0.3)
    #tnmp11 = core.placebo.Tonemap(yuv444p16, src_csp=3, dst_csp=0, dst_prim=3, src_max=10000, src_min=0.005, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=0, tone_mapping_function=11, metadata=0, use_dovi=True, contrast_recovery=0.3)


    #yuv420p161 = core.resize.Bicubic(tnmp1, format=vs.YUV420P16, range=0)
    #yuv420p162 = core.resize.Bicubic(tnmp2, format=vs.YUV420P16, range=0)
    #yuv420p163 = core.resize.Bicubic(tnmp3, format=vs.YUV420P16, range=0)
    yuv420p164 = core.resize.Bicubic(tnmp4, format=vs.YUV420P16, range=0)
    #yuv420p165 = core.resize.Bicubic(tnmp5, format=vs.YUV420P16, range=0)
    #yuv420p166 = core.resize.Bicubic(tnmp6, format=vs.YUV420P16, range=0)
    #yuv420p1610 = core.resize.Bicubic(tnmp10, format=vs.YUV420P16, range=0)
    #yuv420p1611 = core.resize.Bicubic(tnmp11, format=vs.YUV420P16, range=0)

    #frameprops1 = core.std.SetFrameProps(yuv420p161, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    #frameprops2 = core.std.SetFrameProps(yuv420p162, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    #frameprops3 = core.std.SetFrameProps(yuv420p163, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    frameprops4 = core.std.SetFrameProps(yuv420p164, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    #frameprops5 = core.std.SetFrameProps(yuv420p165, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    #frameprops6 = core.std.SetFrameProps(yuv420p166, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    #frameprops10 = core.std.SetFrameProps(yuv420p1610, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    #frameprops11 = core.std.SetFrameProps(yuv420p1611, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)

    #ds4k1 = Hermite.scale(frameprops1, width=1920, height=960, linear=True)
    #ds4k2 = Hermite.scale(frameprops2, width=1920, height=960, linear=True)
    #ds4k3 = Hermite.scale(frameprops3, width=1920, height=960, linear=True)
    ds4k4 = Hermite.scale(frameprops4, width=1920, height=960, linear=True)
    #ds4k5 = Hermite.scale(frameprops5, width=1920, height=960, linear=True)
    #ds4k6 = Hermite.scale(frameprops6, width=1920, height=960, linear=True)
    #ds4k10 = Hermite.scale(frameprops10, width=1920, height=960, linear=True)
    #ds4k11 = Hermite.scale(frameprops11, width=1920, height=960, linear=True)

    #crop = core.std.Crop(ds4k, top=60, bottom=60)

    #final1 = finalize_clip(ds4k1, 10)
    #final2 = finalize_clip(ds4k2, 10)
    #final3 = finalize_clip(ds4k3, 10)
    final4 = finalize_clip(ds4k4, 10)
    #final5 = finalize_clip(ds4k5, 10)
    #final6 = finalize_clip(ds4k6, 10)
    #final10 = finalize_clip(ds4k10, 10)
    #final11 = finalize_clip(ds4k11, 10)

    #WEB = src_file(r"D:\data\torrents\The.Penguin.S01E02.Inside.Man.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-Kitsune.mkv", force_bs=True)
    #web = WEB.init()

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
        enc = x265(settings).encode(final4)
        mux(
            enc.to_track(name="Encoded by AnoZu", lang="en", default=True),
            tmdb=TmdbConfig(194764, season=1, language="en-US", write_ids=True, write_title=True, write_cover=True),
        )
    else:
        set_output(final4)


#set_output(webdl_4k)
#set_output(web)
#set_output(final1)
#set_output(final2)
#set_output(final3)
#set_output(final4)
#set_output(final5)
#set_output(final6)
#set_output(final10)
#set_output(final11)