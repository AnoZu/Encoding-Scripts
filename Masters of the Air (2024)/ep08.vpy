from vstools import core, finalize_clip
from vskernels import Hermite
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output


setup = Setup("08")


WEBDL = src_file(r"D:\data\torrents\Masters.of.the.Air.S01E08.Part.Eight.2160p.ATVP.WEB-DL.DDP5.1.Atmos.H.265-Kitsune.mkv")
webdl = WEBDL.init()
ds4k_webdl = Hermite.descale(webdl, 1918, 802, linear=False)


final = finalize_clip(ds4k_webdl, 10)


if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=17.5,
        aq_strength=1, psy_rd=2.0, psy_rdoq=2,
        qcomp=0.72, rd=4,
        preset="veryslow",
        deblock=[-3, -3], ref=5, bframes=12,
        aq_mode=5,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="en"),
        tmdb=TmdbConfig(46518, language="en-US", write_ids=True, write_cover=True),
    )
else:
    set_output(final)