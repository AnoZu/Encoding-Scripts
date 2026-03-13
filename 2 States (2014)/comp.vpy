from vstools import core, set_output
from vsmuxtools import Setup
from vspreview import set_output

## https://slow.pics/c/0UHZGnfu

setup = Setup(
    "movie",
    None,
    show_name="2 States (2014)",
    out_dir=R".\premux",
    mkv_title_naming=R"$show$ (1080p Bluray DDP 5.1 Hindi x265) [AnoZu]",
    out_name=R"$show$ (1080p Bluray DDP 5.1 Hindi x265) [AnoZu]",
    clean_work_dirs=False,
    debug=True,
)


# Clip
bd = core.ffms2.Source(r".\2.States.2014.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv")
anozu = core.ffms2.Source(r".\premux\2 States (2014) (1080p Bluray DDP 5.1 Hindi x265) [AnoZu].mkv")

# Crop
crop_bd = core.std.Crop(bd, top=132, bottom=132)

# Output
set_output(crop_bd, "BD")
set_output(anozu, "AnoZu (x265)")