## https://slow.pics/c/l0M0WHnW ##

## Dependencies: Allows vspreview to run (required; do not remove)
import vstools
import vapoursynth as vs
from vapoursynth import core
from awsmfunc import FrameInfo
from vspreview import set_output

## File paths: Hold shift and right-click your file, select copy as path, and paste it here
clip1 = core.lsmas.LWLibavSource(r"D:\data\torrents\My.Life.in.Ruins.2009.1080p.BluRay.AVC.DTS-HD.Remux-PTP.mkv")
clip2 = core.lsmas.LWLibavSource(r"D:\data\torrents\My Life in Ruins (2009) (1080p BluRay x265 SDR Opus 5.1 English - AnoZu).mkv")

## Source: Name of the source
source1 = "BluRay"
source2 = "AnoZu"

## Frameinfo: Displays the frame number, type, and group name in the top left corner (no modification required; add/remove lines as needed)
clip1 = FrameInfo(clip1, source1)
clip2 = FrameInfo(clip2, source2)

## FrameProp: Slowpoke Pics/file-name labeling (no modification required; add/remove lines as needed)
clip1 = clip1.std.SetFrameProp('Name', data = source1)
clip2 = clip2.std.SetFrameProp('Name', data = source2)

## Output: Comment/uncomment as needed depending on how many clips you're comparing
set_output(clip1, name=source1)
set_output(clip2, name=source2)