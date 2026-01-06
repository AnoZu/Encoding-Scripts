import vstools
from vstools import vs, core, set_output
from vsmuxtools import src_file, GlobSearch, Setup, SourceFilter
from vspreview import set_output

### https://slow.pics/c/0UHZGnfu

setup = Setup(
    "movie",
    config_file=None,
    show_name= "Influencer (2023)",
    out_name= "$show$ (1080p BluRay DDP 5.1 English x265) [AnoZu]",
    mkv_title_naming= "$show$ 1080p BluRay DDP 5.1 English x265 - AnoZu",
)


# Clip
usbd = core.ffms2.Source(r".\Influencer.2022.1080p.Blu-ray.Remux.AVC.DTS-HD.MA.5.1-CiNEPHiLES.mkv")
anozu = core.ffms2.Source(r".\premux\Influencer (2023) (1080p BluRay DDP 5.1 English x265) [AnoZu].mkv")
hallowed = core.ffms2.Source(r".\Influencer_2023_BluRay_1080p_DDP_5_1_x264-hallowed.mkv")

# Crop
crop_usbd = core.std.Crop(usbd, top=138, bottom=138)

# Output
set_output(crop_usbd, "Shudder USBD")
set_output(anozu, "AnoZu (x265)")
set_output(hallowed, "hallowed (x264)")