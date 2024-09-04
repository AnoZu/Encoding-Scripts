from vstools import core, vs, depth, finalize_clip
from vskernels import Hermite
from vsmuxtools import src_file, GlobSearch, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


for i in range(1, 7):
    # Basic Setup for every episode without a config file
    setup = Setup(
        f"{i:02d}",  # Format to have padded zeros
        None,
        show_name="Shekhar.Home.2024",
        out_dir=R"C:\Users\AnoZu\Desktop\Encoding-Scripts\Shekhar Home (2024)\premux",
        mkv_title_naming=R"Shekhar Home (2024) S01E$ep$ 1080p DS4K JC WEBRip x265 AAC 2.0 - AnoZu",
        out_name=R"$show$ S01E$ep$ 1080p.DS4K.JC.WEBRip.AAC2.0.x265-AnoZu",
        clean_work_dirs=False,
        debug=True,
    )

    WEBDL = src_file(GlobSearch(f"*Shekhar* S01E{setup.episode}*.mkv", dir=R"D:\data\torrents\Shekhar Home (2024) Complete Season S01 2160p WEB-DL x264 Multi AAC DD+ 5.1 ESub-JA"), force_bs=True)
    webdl = WEBDL.init()

    ds4k = Hermite.descale(clip=webdl, width=1920, height=1080, linear=False)
    
    crop = core.std.Crop(ds4k, top=30, bottom=30)
    frameprops = core.std.SetFrameProps(crop, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)
    frameprops32 = depth(frameprops, 32)
    gamma = core.std.Levels(frameprops32, gamma=0.98, planes=0)

    final = finalize_clip(gamma, 10)

    if __name__ == "__main__":
        settings = settings_builder_x265(
            crf=21,
            aq_strength=1, psy_rd=2.0, psy_rdoq=1.5,
            qcomp=0.7, rd=4,
            preset="slow",
            deblock=[-3, -3], ref=5, bframes=16,
            aq_mode=4,
            rect=False
        )
        enc = x265(settings).encode(final)
        mux(
            enc.to_track(name="Encoded by AnoZu", lang="hi-IN", default=True),
            tmdb=TmdbConfig(260203, season=1, language="en-US", write_ids=True, write_title=True, write_cover=True),
        )
    else:
        set_output(final)