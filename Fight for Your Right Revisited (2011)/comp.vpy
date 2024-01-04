## Dependencies: Allows vspreview to run (required; do not remove)
import vapoursynth as vs
from vapoursynth import core
from awsmfunc import FrameInfo
from vskernels import Hermite, EwaLanczos
from vspreview import set_output
from awsmfunc.types.placebo import PlaceboColorSpace as csp
from awsmfunc.types.placebo import PlaceboTonemapMode as TMmode
from awsmfunc.types.placebo import PlaceboTonemapFunction as TMfunc
from awsmfunc.types.placebo import PlaceboGamutMode as GMTmode
from awsmfunc.types.placebo import PlaceboTonemapOpts as TMopts

## <Additional dependencies>
## Place any additional dependencies you want to use in your comp here
## <End of additional dependencies>

## File paths: Hold shift and right-click your file, select copy as path, and paste it here
clip1 = core.lsmas.LWLibavSource(r"D:\data\torrents\Fight for Your Right Revisted (2011) 1080p BluRay x264 DTS 5.1.mkv")
clip2 = core.lsmas.LWLibavSource(r"D:\data\torrents\Fight for Your Right Revisited (2011) (1080p BluRay x265 SDR Opus 5.1 English - AnoZu).mkv")
#clip3 = core.lsmas.LWLibavSource(r"C:\Paste\File\Path\Here.mkv")

## Source: Name of the source
source1 = "BluRay"
source2 = "Encode"
#source3 = "ThirdSourceName"

## Depth: Convert clip to 16-bit 4:4:4 for greater precision
#clip1 = core.resize.Bicubic(clip1, format=vs.YUV444P16)
#clip2 = core.resize.Bicubic(clip2, format=vs.YUV444P16)
#clip3 = core.resize.Bicubic(clip3, format=vs.YUV444P16)

## <Additional comp settings>

## Frame rate: Change fps to match other sources (needed for when the previewer is unable to automatically keep them in sync)
##clip1 = core.std.AssumeFPS(clip1, fpsnum=24000, fpsden=1001)
##clip2 = core.std.AssumeFPS(clip2, fpsnum=25000, fpsden=1000)
##clip3 = core.std.AssumeFPS(clip3, fpsnum=24000, fpsden=1000)

## FieldBased: Tags the content as progressive (0); used for progressive content tagged as interlaced
##clip1 = core.std.SetFieldBased(clip1, 0)
##clip2 = core.std.SetFieldBased(clip2, 0)
##clip3 = core.std.SetFieldBased(clip3, 0)

## Inverse telecine: Fixes telecined video
##clip1 = core.vivtc.VFM(clip1, 1)
##clip1 = core.vivtc.VDecimate(clip1)

## Cropping: Removes letterboxing (black bars) [16-bit required for odd numbers]
##clip1 = core.std.Crop(clip1, left=240, right=240, top=0, bottom=0)
##clip2 = core.std.Crop(clip2, left=0, right=0, top=276, bottom=276)
##clip3 = core.std.Crop(clip3, left=0, right=0, top=21, bottom=21)

## Upscaling: Increases the resolution of clips to match the highest resolution using EwaLanczos (equivalent scaling to mpv's high-quality profile); recommended
##clip1 = EwaLanczos.scale(clip1, 1920, 1080, sigmoid=True)
##clip2 = EwaLanczos.scale(clip2, 1920, 1080, sigmoid=True)
##clip3 = EwaLanczos.scale(clip3, 3840, 2160, sigmoid=True)

## Downscaling: Decreases the resolution of clips to match the lowest resolution using Hermite (equivalent scaling to mpv's high-quality profile); not recommended
##clip1 = Hermite.scale(clip1, 1920, 1080, linear=True)
##clip2 = Hermite.scale(clip2, 1920, 1080, linear=True)
##clip3 = Hermite.scale(clip3, 3840, 2160, linear=True)

## Trimming: Trim frames to match clips (calculate the frame difference and enter the number here)
##clip1 = clip1[0:]
##clip2 = clip2[24:]
##clip3 = clip3[0:]

## Tonemapping: Converts the dynamic range of the source [16-bit required]
## Specify the arguments based on your sources; ideally play around with different values when comparing against an SDR source to best match it
##clip1args = TMopts(source_colorspace=csp.DOVI, target_colorspace=csp.SDR, tone_map_mode=TMmode.RGB, tone_map_function=TMfunc.ST2094_40, gamut_mode=GMTmode.Clip, peak_detect=True, use_dovi=True)
##clip2args = TMopts(source_colorspace=csp.HDR10, target_colorspace=csp.SDR, tone_map_mode=TMmode.RGB, tone_map_function=TMfunc.ST2094_40, gamut_mode=GMTmode.Clip, peak_detect=True, use_dovi=True)
##clip3args = TMopts(source_colorspace=csp.HDR10, target_colorspace=csp.SDR, tone_map_mode=TMmode.Hybrid, tone_map_function=TMfunc.Spline, gamut_mode=GMTmode.Darken, peak_detect=True, use_dovi=True, dst_max=120)
## Apply tonemapping
##clip1 = core.placebo.Tonemap(clip1, **clip1args.vsplacebo_dict())
##clip2 = core.placebo.Tonemap(clip2, **clip2args.vsplacebo_dict())
##clip3 = core.placebo.Tonemap(clip3, **clip3args.vsplacebo_dict())
## Retag video to 709 after tonemapping [required]
##clip1 = core.std.SetFrameProps(clip1, _Matrix=1, _Transfer=1, _Primaries=1)
##clip2 = core.std.SetFrameProps(clip2, _Matrix=1, _Transfer=1, _Primaries=1)
##clip3 = core.std.SetFrameProps(clip3, _Matrix=1, _Transfer=1, _Primaries=1)

## Color range: Marks the clip's range as limited (0) or full (1); DV clips will need to be set to limited (0) after tonemapping
##clip1 = core.resize.Bicubic(clip1, format=vs.YUV444P16, range=0)
##clip2 = core.resize.Bicubic(clip2, format=vs.YUV444P16, range=0)
##clip3 = core.resize.Bicubic(clip3, format=vs.YUV444P16, range=1)

## Gamma: Fixes gamma bug (i.e. one source is significantly brighter than the others) [16-bit required]
##clip1 = core.std.Levels(clip1, gamma=0.88, min_in=4096, max_in=60160, min_out=4096, max_out=60160, planes=0)
##clip2 = core.std.Levels(clip2, gamma=0.88, min_in=4096, max_in=60160, min_out=4096, max_out=60160, planes=0)
##clip3 = core.std.Levels(clip3, gamma=0.88, min_in=4096, max_in=60160, min_out=4096, max_out=60160, planes=0)

## Matrix: Repairs sources with incorrect/missing metadata; typically used for 4K SDR and upscaled/downscaled content (colors will be off, particularly reds, greens, and blues)
##clip1 = core.std.SetFrameProp(clip1, prop="_Matrix", intval=1)
##clip2 = core.std.SetFrameProp(clip2, prop="_Matrix", intval=6)
##clip3 = core.std.SetFrameProp(clip3, prop="_Matrix", intval=5)

## Correct matrix: If the colors cannot be corrected with the initial matrix command [16-bit required]
##clip1 = core.resize.Point(clip1, matrix=5)
##clip1 = core.std.SetFrameProp(clip1, prop="_Matrix", intval=1)
##clip2 = core.resize.Point(clip2, matrix=6)
##clip2 = core.std.SetFrameProp(clip2, prop="_Matrix", intval=1)
##clip3 = core.resize.Point(clip3, matrix=4)
##clip3 = core.std.SetFrameProp(clip3, prop="_Matrix", intval=1)

## Fix DRC: Repairs sources with very washed out colors
##clip1 = core.resize.Point(clip1, range_in=0, range=1, dither_type="error_diffusion")
##clip1 = core.std.SetFrameProp(clip1, prop="_ColorRange", intval=1)

## <End of additional comp settings>

## Frameinfo: Displays the frame number, type, and group name in the top left corner (no modification required; add/remove lines as needed)
clip1 = FrameInfo(clip1, source1)
clip2 = FrameInfo(clip2, source2)
#clip3 = FrameInfo(clip3, source3)

## FrameProp: Slowpoke Pics/file-name labeling (no modification required; add/remove lines as needed)
clip1 = clip1.std.SetFrameProp('Name', data = source1)
clip2 = clip2.std.SetFrameProp('Name', data = source2)
#clip3 = clip3.std.SetFrameProp('Name', data = source3)

## Output: Comment/uncomment as needed depending on how many clips you're comparing
set_output(clip1, name=source1)
set_output(clip2, name=source2)
#set_output(clip3, name=source3)