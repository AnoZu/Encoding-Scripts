from vstools import core, set_output
from vsmuxtools import Setup
from vspreview import set_output

### https://slow.pics/c/jWOnPe8C

setup = Setup(
    "01",
    None,
    show_name="Arcane (2021)",
    out_dir=R".\premux",
    mkv_title_naming=R"$show$ S02E$ep$ $title$ (1080p Bluray DDP Atmos 7.1 x265) [AnoZu]",
    out_name=R"$show$ S02E$ep$ $title$ (1080p Bluray DDP Atmos 7.1 x265) [AnoZu]",
    clean_work_dirs=False,
    debug=True,
)


# Clip
gbbd = core.ffms2.Source(r".\Arcane S02E01 Heavy Is the Crown 1080p Blu-ray Remux AVC Atmos-E.N.D.mkv")
web = core.ffms2.Source(r".\Arcane (2021) S02E01 (1080p NF WEB-DL H264 SDR DDP Atmos 5.1 English - HONE).mkv")[120:]
anozu = core.ffms2.Source(r".\Arcane (2021) S02E01 Heavy Is the Crown (1080p Bluray DDP Atmos 7.1 x265) [AnoZu].mkv")
zorosenpai = core.ffms2.Source(r".\Arcane.S02E01.Heavy.Is.the.Crown.1080p.BluRay.DDP7.1.x264-ZoroSenpai.mkv")

# Crop
crop_usbd = core.std.Crop(gbbd, top=132, bottom=132)
crop_web = core.std.Crop(web, top=132, bottom=132)

# Output
set_output(crop_usbd, "GBR BD")
set_output(crop_web, "NF (H264)")
set_output(anozu, "AnoZu (x265)")
set_output(zorosenpai, "ZoroSenpai (x264)")