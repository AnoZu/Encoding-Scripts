from vstools import core, set_output, finalize_clip
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, do_audio, mux
from vsdenoise import nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, PelType, BM3DCudaRTC
import vsaa

core

setup = Setup("01")

### Source ###
web_dl = src_file(r"D:\data\torrents\Dosed.2019.1080p.AMZN.WEB-DL.DDP2.0.H.264-ZTR.mkv")
src = web_dl.init()

### AA ###
aa = vsaa.fine_aa(src, singlerater=vsaa.Eedi3(0.5, 0.5, 40))

### Final ###
final = finalize_clip(aa, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=18, 
        aq_strength=0.82, psy_rd=2, psy_rdoq=2,
        qcomp=0.73, rd=4, 
        preset="veryslow",
        deblock=[-3, -3],
        aq_mode=3,
        rect=False
    )
    enc = x265(settings).encode(final)
    audio = do_audio(web_dl, 0).to_track("DDP 2.0")
    mux(enc, audio)
else:
    set_output(final)

#set_output(src)
#set_output(den_y)
#set_output(den_uv)
#set_output(aa)