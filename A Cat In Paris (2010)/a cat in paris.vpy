from vstools import vs, core, get_y, depth, replace_ranges
import vsdenoise
import jvsfunc
import vsmasktools
import vsaa
import vsdehalo


core = vs.core


src = core.lsmas.LWLibavSource(r'D:\A Cat In Paris.mkv')


fl_ranges = [(966, 4399), (5600, 67767), (70083, 70332), (70683, 85282)]


### Denoise ###
src_y = get_y(src)
src_UV = jvsfunc.ccdmod(src, 4)
den_mask = vsmasktools.detail_mask_neo(src_y)
denoise = vsdenoise.BM3DCudaRTC.denoise(src_y, sigma=1)
denoise2 = core.std.ShufflePlanes([denoise, src_UV], [0, 1, 2], vs.YUV)
denoise_final = core.std.MaskedMerge(denoise2, src, den_mask)


### AA ###
aa = vsaa.based_aa(denoise_final, 2, 30)


### Dehalo ###
dehalo_mask = vsdehalo.base_dehalo_mask(aa)
dehalo = vsdehalo.edge_cleaner(aa)
dehalo_final = core.std.MaskedMerge(dehalo, aa, dehalo_mask)


### Grain ###
grain = core.grain.Add(dehalo_final, var=0.3, uvar=0.3, seed=1, constant=True)


### Final ###
out = depth(replace_ranges(src, grain, fl_ranges), 10)


out.set_output()
#src.set_output(1)
#crop.set_output(2)
#denoise_final.set_output(3)
#den_mask.set_output(4)
#aa.set_output(5)
#dehalo_final.set_output(6)
#grain.set_output(7)