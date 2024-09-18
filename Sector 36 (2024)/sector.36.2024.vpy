from vstools import vs, core, finalize_clip
from vskernels import Hermite
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


setup = Setup("movie")

WEBDL_4K = src_file(r"D:\data\torrents\Sector.36.2024.2160p.NF.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-Tyrell.mkv", force_bs=True)
webdl_4k = WEBDL_4K.init()

yuv444p16 = core.resize.Lanczos(webdl_4k, format=vs.YUV444P16)

tnmphdr = core.placebo.Tonemap(yuv444p16, src_csp=1, dst_csp=0, dst_prim=3, src_max=1000, src_min=0.0001, dst_max=100, dst_min=0.1, dynamic_peak_detection=True, gamut_mapping=1, tone_mapping_function=3, metadata=2, use_dovi=False, contrast_recovery=0.3)

yuv420p16hdr = core.resize.Lanczos(tnmphdr, format=vs.YUV420P16, range=0)

hdrprops = core.std.SetFrameProps(yuv420p16hdr, _Matrix=vs.MATRIX_BT709, _Transfer=vs.TRANSFER_BT709, _Primaries=vs.PRIMARIES_BT709)

ds4khdr = Hermite.scale(hdrprops, width=1920, height=1080, linear=True)

crophdr = core.std.Crop(ds4khdr, top=60, bottom=60)

finalhdr = finalize_clip(crophdr, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=18,
        aq_strength=0.75, psy_rd=2.0, psy_rdoq=1.5,
        qcomp=0.7, rd=4,
        preset="slower",
        deblock=[-3, -3], ref=5, bframes=16,
        aq_mode=5,
        rect=False
    )
    enc = x265(settings).encode(finalhdr)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="hi-IN"),
        tmdb=TmdbConfig(1245700, movie=True, language="en-US", write_date=False, write_cover=True),
    )
else:
    set_output(finalhdr, "DS4K NF WEB-DL")