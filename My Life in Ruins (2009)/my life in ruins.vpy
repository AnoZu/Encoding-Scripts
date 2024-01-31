from vstools import core, finalize_clip
from vsdenoise import nlm, MVTools, BM3DCudaRTC, Profile, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, PelType
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, do_audio, Opus, TmdbConfig, mux
from vspreview import set_output
from vsaa import fine_aa, Eedi3

setup = Setup("00")

src = src_file(r"D:\data\torrents\My.Life.in.Ruins.2009.1080p.BluRay.AVC.DTS-HD.Remux-PTP.mkv")
video = src.init()

mvref = MVTools.denoise(video, thSAD=150, tr=2, prefilter=Prefilter.DFTTEST, block_size=32, overlap=16, pel_type=PelType.WIENER, motion=MotionMode.HIGH_SAD, sad_mode=SADMode.SPATIAL.same_recalc, search=SearchMode.DIAMOND.defaults)
denc = nlm.nl_means(video, ref=mvref, strength=0.6, tr=2, device_type=DeviceType.CUDA, planes=[1, 2])

final = finalize_clip(denc, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=23,
        aq_strength=0.75, psy_rd=2.0, psy_rdoq=1,
        qcomp=0.7, rd=4,
        preset="veryslow",
        deblock=[-3, -3], ref=5, bframes=12,
        aq_mode=3,
        rect=False
    )
    enc = x265(settings).encode(final)
    audio = do_audio(src, 0, encoder=Opus(bitrate=512, vbr=True))
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="en"),
        audio.to_track(name="Opus 5.1 English", lang="en", default=True),
        tmdb=TmdbConfig(23049, movie=True, language="en-US", write_date=False, write_cover=True),
    )
else:
    set_output(final)