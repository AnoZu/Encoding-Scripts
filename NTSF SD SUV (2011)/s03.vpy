from vstools import core, join, finalize_clip
from vsdenoise import BM3DCudaRTC, nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, PelType, Profile
from vsmuxtools import src_file, GlobSearch, Setup, x265, settings_builder_x265, TmdbConfig, do_audio, mux
from vspreview import set_output


for i in range(1, 13):
    # Basic Setup for every episode without a config file
    setup = Setup(
        f"{i:02d}",  # Format to have padded zeros
        None,
        show_name="NTSF SD SUV (2011)",
        out_dir=R"C:\Users\AnoZu\Desktop\Encoding-Scripts\NTSF SD SUV (2011)\S03\premux",
        mkv_title_naming=R" NTSF:SD:SUV:: (2011) S03E$ep$ 1080p WEBRip x265 DDP 2.0 - AnoZu",
        out_name=R"NTSF.SD.SUV.2011.S03E$ep$ 1080p.WEBRip.DDP2.0.x265-AnoZu",
        clean_work_dirs=False,
        debug=True,
    )

    WEBDL = src_file(GlobSearch(f"*NTSF*.S03E{setup.episode}*.mkv", dir=R"D:\data\torrents\NTSF.SD.SUV.S03.1080p.AMZN.WEBRip.DDP5.1.x264-Cinefeel"), force_bs=True)
    webdl = WEBDL.init()

    mvref = MVTools.denoise(webdl, thSAD=100, tr=2, prefilter=Prefilter.BM3D, block_size=32, overlap=16, pel_type=PelType.WIENER, motion=MotionMode.HIGH_SAD, sad_mode=SADMode.SPATIAL.same_recalc, search=SearchMode.DIAMOND.defaults)
    den_y = BM3DCudaRTC.denoise(webdl, sigma=0.5, tr=2, profile=Profile.FAST, ref=mvref, planes=0)
    den_uv = nlm.nl_means(webdl, strength=0.8, tr=2, sr=2, device_type=DeviceType.CUDA, ref=mvref, planes=[1, 2])
    denf = join(den_y, den_uv)

    final = finalize_clip(denf, 10)

    if __name__ == "__main__":
        settings = settings_builder_x265(
            crf=20, #18 for E07, 19 for E10
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
            tmdb=TmdbConfig(39106, season=3, language="en-US", write_ids=True, write_title=True, write_cover=True),
        )
    else:
        set_output(final)