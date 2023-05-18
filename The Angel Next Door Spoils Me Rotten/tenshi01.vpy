from vstools import vs, core, depth, replace_ranges, get_y
from jvsfunc import retinex_edgemask, ccdmod
from vsdeband import F3kdb
from vsdehalo import edge_cleaner, smooth_dering
from vsaa import Nnedi3, fine_aa
from vsdeband import pfdeband
import vsmasktools as vsm

core = vs.core


fl_ranges = [(0, 1942), (2062, 17861), (17982, 31768), (33926, 34045)]


src = depth(core.lsmas.LWLibavSource(r'C:\Users\Hammad Ansari\Desktop\[SubsPlease] Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken - 01 (1080p) [9330289F].mkv'), 16)
src_luma = get_y(src)


#### Denoise ####
denoise32 = depth(src_luma, 32)
denoise_bm3d = core.bm3dcuda_rtc.BM3D(denoise32, sigma = 0.72)
src_chroma = ccdmod(src, 4)
denoise_final = core.std.ShufflePlanes([depth(denoise_bm3d, 16), src_chroma], [0, 1, 2], vs.YUV)


#### AA ####
nnedi3 = Nnedi3()
aa = fine_aa(denoise_final, False, nnedi3)


#### Deband ####
dbmask = vsm.detail_mask_neo(src_luma, 0.8)
deband = pfdeband(aa, radius = 16, thr = 15, debander = F3kdb)
deband_final = core.std.MaskedMerge(deband, aa, dbmask)


#### Dehalo ####
dehalo = edge_cleaner(deband)
dehalo_final = smooth_dering(dehalo)


#### Grain ####
grain = core.grain.Add(dehalo_final, var = 0.2, seed = 1, constant = True)


#### Final ####
out = depth(replace_ranges(src, grain, fl_ranges), 10)


out.set_output(2)
src.set_output(1)
#denoise_final.set_output(2)
#aa.set_output(3)
#deband_final.set_output(4)
#dehalo_final.set_output(5)
#grain.set_output(6)
#dbmask.set_output(7)