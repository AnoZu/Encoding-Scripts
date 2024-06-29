## https://slow.pics/c/nnHIKDwA

import vstools
import vapoursynth as vs
from vapoursynth import core
from awsmfunc import FrameInfo
from vskernels import Hermite, EwaLanczos
from vspreview import set_output

## File paths: Hold shift and right-click your file, select copy as path, and paste it here
clip1 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.2160p.MA.WEB-DL.TrueHD.Atmos.7.1.H.265-FLUX.mkv")
clip2 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune - Part Two (2024) (1080p MA WEB-DL H264 SDR DDP Atmos 5.1 English - HONE).mkv")
clip3 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune - Part Two (2024) (1080p MA WEB-DL H265 SDR DDP Atmos 5.1 English - HONE).mkv")
clip4 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.BluRay.1080p.TrueHD.Atmos.7.1.AVC.REMUX-FraMeSToR\Dune.Part.Two.2024.BluRay.1080p.TrueHD.Atmos.7.1.AVC.REMUX-FraMeSToR.mkv")
clip5 = core.lsmas.LWLibavSource(r"C:\data\torrents\Dune - Part 2 (2024) (1080p DS4K MA WEBRip x265 SDR DDP Atmos 5.1 English - AnoZu).mkv")
clip6 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.1080p.AMZN.WEB-DL.DDP5.1.SDR.H.264-GRiMM.mkv")
clip7 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.1080p.AMZN.WEB-DL.DDP5.1.SDR.H.265-GRiMM.mkv")
clip8 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune - Part Two (2024) (1080p BDRip x265 10bit EAC3 7.1 English - JBENT)[TAoE].mkv")
clip9 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.1080p.BluRay.10Bit.X265.DDP.7.1-Chivaman.mkv")
clip10 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.1080p.Blu-ray.DDPA5.1.HEVC-YELLO.mkv")
clip11 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dune.Part.Two.2024.1080p.BluRay.DD+.7.1.X265-Ralphy.mkv")

## Source: Name of the source
source1 = "DS4K MA WEB"
source2 = "1080p MA WEB H264"
source3 = "1080p MA WEB H265"
source4 = "1080p BD FraMeSToR"
source5 = "DS4K MA WEBRip AnoZu"
source6 = "1080p AMZN WEB H264"
source7 = "1080p AMZN WEB H265"
source8 = "BDRip JBENT TAoE"
source9 = "BDRip Chivaman"
source10 = "BDRip YELLO"
source11 = "BDRip Ralphy"

## Downscaling: Decreases the resolution of clips to match the lowest resolution using Hermite (equivalent scaling to mpv's high-quality profile); not recommended
clip1 = Hermite.descale(clip1, 1920, 1080, linear=False)

## Trimming: Trim frames to match clips (calculate the frame difference and enter the number here)
clip1 = clip1[24:]
clip2 = clip2[24:]
clip3 = clip3[24:]
clip5 = clip5[24:]
clip6 = clip6[330:]
clip7 = clip7[330:]

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
clip10 = FrameInfo(clip10, source10)
clip11 = FrameInfo(clip11, source11)

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
clip10 = clip10.std.SetFrameProp('Name', data = source10)
clip11 = clip11.std.SetFrameProp('Name', data = source11)

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
set_output(clip10, name=source10)
set_output(clip11, name=source11)