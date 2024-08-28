from vstools import core, finalize_clip
from vsmuxtools import src_file, GlobSearch, Setup, x265, settings_builder_x265, TmdbConfig, do_audio, mux
from vspreview import set_output


for i in range(13, 15):
    # Basic Setup for every episode without a config file
    setup = Setup(
        f"{i:02d}",  # Format to have padded zeros
        None,
        show_name="NTSF SD SUV (2011)",
        out_dir=R"C:\Users\AnoZu\Desktop\Encoding-Scripts\NTSF SD SUV (2011)\S00\premux",
        mkv_title_naming=R"NTSF:SD:SUV:: (2011) S00E$ep$ 1080p WEBRip x265 DDP 2.0 - AnoZu",
        out_name=R"NTSF.SD.SUV.2011.S00E$ep$ 1080p.WEBRip.DDP2.0.x265-AnoZu",
        clean_work_dirs=False,
        debug=True,
    )

    WEBDL = src_file(GlobSearch(f"*NTSF*.S00E{setup.episode}*.mkv", dir=R"D:\data\torrents"), force_bs=True)
    webdl = WEBDL.init()

    final = finalize_clip(webdl, 10)

    if __name__ == "__main__":
        settings = settings_builder_x265(
            crf=20, #22 for E14
            aq_strength=1, psy_rd=2.0, psy_rdoq=2,
            qcomp=0.7, rd=4,
            preset="veryslow",
            deblock=[-3, -3], ref=5, bframes=12,
            aq_mode=4,
            rect=False
        )
        enc = x265(settings).encode(final)
        audio = do_audio(WEBDL, 0)
        mux(
            enc.to_track(name="Encoded by AnoZu", lang="en-US", default=True),
            audio.to_track(name="English", lang="en-US", default=True),
            tmdb=TmdbConfig(39106, season=0, language="en-US", write_ids=True, write_title=True, write_cover=True),
        )
    else:
        set_output(final)