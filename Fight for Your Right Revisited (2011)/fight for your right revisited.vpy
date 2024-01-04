from vstools import core, set_output, finalize_clip
from vsmuxtools import src_file, Setup, x265, settings_builder_x265
from vsdenoise import nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, DeviceType, PelType

core

setup = Setup("01")

### Source ###
file = src_file(r"D:\data\torrents\Fight for Your Right Revisted (2011) 1080p BluRay x264 DTS 5.1.mkv")
src = file.init()

### Denoise ###
mvref = MVTools.denoise(src, thSAD=150, tr=2, prefilter=Prefilter.AUTO, block_size=32, overlap=16, pel_type=PelType.WIENER, motion=MotionMode.HIGH_SAD, sad_mode=SADMode.SPATIAL.same_recalc, search=SearchMode.DIAMOND.defaults)
den_uv = nlm.nl_means(src, ref=mvref, strength=1.5, tr=2, device_type=DeviceType.CUDA, planes=[1, 2])

### Final ###
final = finalize_clip(den_uv, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=23.5,
        aq_strength=1, psy_rd=2.0, psy_rdoq=1.5,
        qcomp=0.60, rd=4, 
        preset="slow",
        deblock=[-2, -2], ref=6, bframes=12,
        aq_mode=3, cutree=True,
        rect=False
    )
    enc = x265(settings).encode(final)
else:
    set_output(final)