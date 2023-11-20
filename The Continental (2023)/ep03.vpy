from vstools import core, set_output, finalize_clip
from vskernels import Spline36
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, do_audio, mux
from vsdenoise import nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, PelType

core

setup = Setup("03")

### Source ###
web_dl = src_file(R"D:\data\torrents\The Continental - From the World of John Wick (2023) S01 (2160p AMZN WEB-DL H265 SDR DDP Atmos 5.1 English - HONE)\The Continental - From the World of John Wick (2023) S01E03 (2160p AMZN WEB-DL H265 SDR DDP Atmos 5.1 English - HONE).mkv", False)
src4k = web_dl.init()

### Downscale ###
spline36 = Spline36.descale(src4k, width=1920, height=800)

### Denoise ###
mvref = MVTools.denoise(spline36, thSAD=150, tr=2, prefilter=Prefilter.BM3D, block_size=32, overlap=16, pel_type=PelType.WIENER, motion=MotionMode.HIGH_SAD, sad_mode=SADMode.SPATIAL.same_recalc, search=SearchMode.DIAMOND.defaults)
den_uv = nlm.nl_means(spline36, ref=mvref, strength=0.8, tr=2, device_type=DeviceType.CUDA, planes=[1, 2])

### Final ###
final = finalize_clip(den_uv, 10)


if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=17.2, 
        aq_strength=1, psy_rd=2.1, psy_rdoq=3,
        qcomp=0.72, rd=4, 
        preset="slow",
        deblock=[-3, -3], bframes=12,
        aq_mode=5,
        rect=False
    )
    enc = x265(settings).encode(final)
    audio = do_audio(web_dl, 0).to_track("DDP Atmos 5.1")
    mux(enc, audio)
else:
    set_output(final)

#set_output(src4k)
#set_output(spline36)
#set_output(mvref)
#set_output(den_uv)
#set_output(final)