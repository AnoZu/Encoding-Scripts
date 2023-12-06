## Boring stuff: Ignore me
from vstools import core, set_output
from awsmfunc import FrameInfo

core

## File paths: Hold shift and right-click your file, select copy as path, and paste it here
clip1 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dosed.2019.1080p.AMZN.WEB-DL.DDP2.0.H.264-ZTR.mkv")
clip2 = core.lsmas.LWLibavSource(r"D:\data\torrents\Dosed (2019) (1080p AMZN WEBRip x265 SDR DDP 2.0 English - AnoZu).mkv")
#clip3 = core.lsmas.LWLibavSource(r"C:\Paste\File\Path\Here.mkv")

## Source: Name of the source
source1 = "WEB-DL"
source2 = "Encode"
#source3 = "ThirdSourceName"

## FieldBased: Sets the content as either progressive (0) or interlaced (1/2), required for progressive content tagged as interlaced
##clip1 = core.std.SetFieldBased(clip1, 0)
##clip2 = core.std.SetFieldBased(clip2, 1)
##clip3 = core.std.SetFieldBased(clip3, 2)

## Convert: Convert clip to 16bit 444 (Only for filters that need it such as tonemapping and gamma fixing)
##clip1 = core.resize.Bicubic(clip1, format=vs.YUV444P16)
##clip2 = core.resize.Bicubic(clip2, format=vs.YUV444P16)
##clip3 = core.resize.Bicubic(clip3, format=vs.YUV444P16)

## Cropping: Removes letterboxing (Black bars) [16 BIT REQUIRED FOR ODD NUMBERS]
##clip1 = core.std.Crop(clip1, left=240, right=240, top=0, bottom=0)
##clip2 = core.std.Crop(clip2, left=0, right=0, top=276, bottom=276)
##clip3 = core.std.Crop(clip3, left=0, right=0, top=21, bottom=21)

## Scaling: Up/downscale clips to match, recommended to scale to the highest resolution
##clip1 = core.resize.Spline36(clip1, 1920, 1080)
##clip2 = core.resize.Spline36(clip2, 1920, 1080)
##clip3 = core.resize.Spline36(clip3, 3840, 2160)

## Trimming: Trim frames to match clips (Calculate the frame difference and enter the number here)
##clip1 = clip1[0:]
##clip2 = clip2[24:]
##clip3 = clip3[0:]

## Set FPS: Change fps to match other sources, only needed when the previewer doesn't automatically keep them in sync
##clip1 = core.std.AssumeFPS(clip1, fpsnum=24000, fpsden=1001)
##clip2 = core.std.AssumeFPS(clip2, fpsnum=25000, fpsden=1000)
##clip3 = core.std.AssumeFPS(clip3, fpsnum=24000, fpsden=1000)

## Tonemapping: For HDR/DV content only, src_csp=1 is for HDR (and DV Profile 8), src_csp=3 is for DV (Profile 5) [16 BIT REQUIRED]
##clip1 = core.placebo.Tonemap(clip1, dynamic_peak_detection=1, tone_mapping_function=2, tone_mapping_mode=3, src_csp=1, dst_csp=0, gamut_mode=2, intent=0, use_dovi=1)
##clip2 = core.placebo.Tonemap(clip2, dynamic_peak_detection=1, tone_mapping_function=2, tone_mapping_mode=3, src_csp=3, dst_csp=0, gamut_mode=2, intent=0, use_dovi=1)
##clip3 = core.placebo.Tonemap(clip3, dynamic_peak_detection=1, tone_mapping_function=2, tone_mapping_mode=3, src_csp=1, dst_csp=0, gamut_mode=2, intent=0, use_dovi=1, dst_max=120)

## Retagging video to 709 after tonemapping (Otherwise you'll get horrible blue images)
##clip1 = core.std.SetFrameProps(clip1, _Matrix=1, _Transfer=1, _Primaries=1)
##clip2 = core.std.SetFrameProps(clip2, _Matrix=1, _Transfer=1, _Primaries=1)
##clip3 = core.std.SetFrameProps(clip3, _Matrix=1, _Transfer=1, _Primaries=1)

##Set Colour Range: Marks the clip as limited (0) or full (1) range, DV clips will need to be set to limited after tonemapping.
##clip1 = core.resize.Bicubic(clip1, format=vs.YUV444P16, range=0)
##clip2 = core.resize.Bicubic(clip2, format=vs.YUV444P16, range=0)
##clip3 = core.resize.Bicubic(clip3, format=vs.YUV444P16, range=1)

## Gamma: Fix Gamma bug (When one source is much brighter than others) [16 BIT REQUIRED]
##clip1 = core.std.Levels(clip1, gamma=0.88, min_in=4096, max_in=60160, min_out=4096, max_out=60160, planes=0)
##clip2 = core.std.Levels(clip2, gamma=0.88, min_in=4096, max_in=60160, min_out=4096, max_out=60160, planes=0)
##clip3 = core.std.Levels(clip3, gamma=0.88, min_in=4096, max_in=60160, min_out=4096, max_out=60160, planes=0)

## Set Matrix: If source has incorrect/missing metadata, usually applies to 4K SDR and content you're up/downscaling. (Colours will be off, particularly reds, greens, and blues)
##clip1 = core.std.SetFrameProp(clip1, prop="_Matrix", intval=1)
##clip2 = core.std.SetFrameProp(clip2, prop="_Matrix", intval=6)
##clip3 = core.std.SetFrameProp(clip3, prop="_Matrix", intval=5)

## Correct Matrix: If the colours cannot be corrected with the above command [16 BIT REQUIRED]
##clip1 = core.resize.Point(clip1, matrix=5)
##clip1 = core.std.SetFrameProp(clip1, prop="_Matrix", intval=1)
##clip2 = core.resize.Point(clip2, matrix=6)
##clip2 = core.std.SetFrameProp(clip2, prop="_Matrix", intval=1)
##clip3 = core.resize.Point(clip3, matrix=4)
##clip3 = core.std.SetFrameProp(clip3, prop="_Matrix", intval=1)

## Fix Double range compression: When one source looks very washed out
##clip1 = core.resize.Point(clip1, range_in=0, range=1, dither_type="error_diffusion")
##clip1 = core.std.SetFrameProp(clip1, prop="_ColorRange", intval=1)

## Frameinfo: Displays the frame number, type, and group name in the top left corner (Leave these lines untouched, it reads the source from the top)
clip1= FrameInfo(clip1, source1)
clip2= FrameInfo(clip2, source2)
#clip3= FrameInfo(clip3, source3)

## FrameProp: Slow.pics/file name labelling (Leave these lines untouched, it reads the source from the top)
clip1 = clip1.std.SetFrameProp('Name', data = source1)
clip2 = clip2.std.SetFrameProp('Name', data = source2)
#clip3 = clip3.std.SetFrameProp('Name', data = source3)

## Output: Comment/Uncomment as needed depending on how many clips you're comparing
set_output(clip1, name=source1)
set_output(clip2, name=source2)
#set_output(clip3, name=source3)