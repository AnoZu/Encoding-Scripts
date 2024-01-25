## Dependencies: Allows vspreview to run (required; do not remove)
import vstools
import vapoursynth as vs
from vapoursynth import core
from awsmfunc import FrameInfo
from vskernels import Hermite
from vspreview import set_output

## File paths: Hold shift and right-click your file, select copy as path, and paste it here
clip1 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer (2023) (1080p MA WEB-DL H265 SDR DDP 5.1 English - HONE).mkv")
clip2 = core.lsmas.LWLibavSource(r"D:\data\media\movies\Oppenheimer (2023) [tmdbid-872585]\Oppenheimer (2023) (2160p MA WEB-DL H265 SDR DDP 5.1 English - HONE).mkv")
clip3 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer.2023.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv")
clip4 = core.lsmas.LWLibavSource(r"D:\data\media\movies\Oppenheimer (2023) [tmdbid-872585]\Oppenheimer (2023) IMAX (1080p DS4K MA WEBRip Hybrid x265 SDR DDP 5.1 English - AnoZu).mkv")
clip5 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer (2023) IMAX (1080p BluRay x265 SDR DDP 5.1 English - Weasley HONE).mkv")
clip6 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer (2023) (1080p BDRip x265 10bit EAC3 5.1 English - JBENT)[TAoE].mkv")
clip7 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer (2023) (1080p BDRip x265 10bit AC3 5.1 - DNU)[TAoE].mkv")
clip8 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer.2023.1080p.BluRay.x265.10bit.EAC3.5.1-TimeDistortion.mkv")
clip9 = core.lsmas.LWLibavSource(r"D:\data\torrents\Oppenheimer.2023.IMAX.1080p.BluRay.10Bit.X265.DD.5.1-Chivaman.mkv")

## Source: Name of the source
source1 = "1080p MA WEB-DL"
source2 = "DS4K MA WEB-DL"
source3 = "1080p BD FraMeSToR"
source4 = "AnoZu"
source5 = "Weasley HONE"
source6 = "JBENT TAoE"
source7 = "DNU TAoE"
source8 = "TimeDistortion"
source9 = "Chivaman"

## Downscaling: Decreases the resolution of clips to match the lowest resolution using Hermite (equivalent scaling to mpv's high-quality profile); not recommended
clip2 = Hermite.descale(clip2, 1920, 1080, linear=True)

## Trimming: Trim frames to match clips (calculate the frame difference and enter the number here)
clip1 = clip1[24:]
clip2 = clip2[24:]
#clip4 = clip4[24:]

## Frameinfo: Displays the frame number, type, and group name in the top left corner (no modification required; add/remove lines as needed)
clip1 = FrameInfo(clip1, source1)
clip2 = FrameInfo(clip2, source2)
clip3 = FrameInfo(clip3, source3)
clip4 = FrameInfo(clip4, source4)
clip5 = FrameInfo(clip5, source5)
clip6 = FrameInfo(clip6, source6)
clip7 = FrameInfo(clip7, source7)
clip8 = FrameInfo(clip8, source8)
clip9 = FrameInfo(clip9, source9)

## FrameProp: Slowpoke Pics/file-name labeling (no modification required; add/remove lines as needed)
clip1 = clip1.std.SetFrameProp('Name', data = source1)
clip2 = clip2.std.SetFrameProp('Name', data = source2)
clip3 = clip3.std.SetFrameProp('Name', data = source3)
clip4 = clip4.std.SetFrameProp('Name', data = source4)
clip5 = clip5.std.SetFrameProp('Name', data = source5)
clip6 = clip6.std.SetFrameProp('Name', data = source6)
clip7 = clip7.std.SetFrameProp('Name', data = source7)
clip8 = clip8.std.SetFrameProp('Name', data = source8)
clip9 = clip9.std.SetFrameProp('Name', data = source9)

## Output: Comment/uncomment as needed depending on how many clips you're comparing
set_output(clip1, name=source1)
set_output(clip2, name=source2)
set_output(clip3, name=source3)
set_output(clip4, name=source4)
set_output(clip5, name=source5)
set_output(clip6, name=source6)
set_output(clip7, name=source7)
set_output(clip8, name=source8)
set_output(clip9, name=source9)