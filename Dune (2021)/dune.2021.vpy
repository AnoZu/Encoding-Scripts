from vstools import core, replace_ranges, finalize_clip
from vskernels import Hermite
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output

core

setup = Setup("00")

## Source ##
WEBDL_4K = src_file(r"D:\data\torrents\Dune (2021) (2160p MA WEB-DL H265 SDR DDP Atmos 5.1 English - HONE).mkv")
webdl_4k = WEBDL_4K.init()
ds4k_webdl = Hermite.descale(webdl_4k, 1920, 1080, linear=False)

crop = core.std.Crop(ds4k_webdl, top=140, bottom=140)

final = finalize_clip(crop, 10)

if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=19,
        aq_strength=1, psy_rd=2.0, psy_rdoq=2,
        qcomp=0.7, rd=4,
        preset="veryslow",
        deblock=[-3, -3], ref=5, bframes=12,
        aq_mode=4,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="en"),
        tmdb=TmdbConfig(438631, movie=True, language="en-US", write_date=False, write_cover=True),
    )
else:
    set_output(final, "DS4K MA WEB-DL")