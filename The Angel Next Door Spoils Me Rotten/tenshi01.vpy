from vstools import vs, core, depth, replace_ranges, get_y
from jvsfunc import retinex_edgemask, ccdmod
from vsdeband import f3kdb
from vsdehalo import edge_cleaner, smooth_dering
from vsaa import antialiasers, transpose_aa

core = vs.core


fl_ranges = [(0, 17861), (17982, 31768), (33926, 34045)]


src = depth(core.lsmas.LWLibavSource(r'C:\Users\Hammad Ansari\Desktop\[SubsPlease] Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken - 01 (1080p) [9330289F].mkv'), 16)
src_luma = get_y(src)


#### Denoise ####
linemask = retinex_edgemask(src_luma, 1)
denoise32 = depth(src_luma, 32)
denoise_bm3d = core.bm3dcuda_rtc.BM3D(denoise32)
src_chroma = ccdmod(src, 4)
shuffle = core.std.ShufflePlanes([depth(denoise_bm3d, 16), src_chroma], [0, 1, 2], vs.YUV)
denoise_final = core.std.MaskedMerge(shuffle, src, linemask)


#### AA ####
aa_nnedi3 = antialiasers.Nnedi3()
aa = transpose_aa(denoise_final, aa_nnedi3)


#### Deband ####
deband = f3kdb.F3kdb.deband(aa, radius = 16)


#### Dehalo ####
dehalo = edge_cleaner(deband)
dehalo_final = smooth_dering(dehalo)


#### Grain ####
grain = core.grain.Add(dehalo_final, var = 0.2, seed = 1, constant = True)


#### Final ####
out = depth(replace_ranges(src, grain, fl_ranges), 10)


out.set_output()
#src.set_output(1)
#denoise_final.set_output(2)
#aa.set_output(3)
#deband.set_output(4)
#dehalo_final.set_output(5)
#grain.set_output(6)