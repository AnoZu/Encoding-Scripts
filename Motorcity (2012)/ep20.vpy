from vstools import core, set_output, join, finalize_clip, replace_ranges
from vsmuxtools import src_file
from vsdenoise import BM3DCudaRTC, nlm
from vsdeband import AddGrain, Placebo
from vsmasktools import dre_edgemask

#Deband Range
deb_range = [(121, 31468)]

core

#Source
web_dl = src_file(R"D:\torrents\Motorcity.S01.1080p.WEB-DL.Rus.Eng_THD\Motorcity.S01E20.Finale.Part.2.A.Better.Tomorrow.1080p.WEB-DL.Rus.Eng_THD.mkv", force_lsmas=True)
src = web_dl.src

#Denoise
den_y = BM3DCudaRTC.denoise(src, 0.8, tr=3, planes=0)
den_uv = nlm.nl_means(src, 0.35, tr=3, planes=[1, 2])
den_final = join(den_y, den_uv)

#Deband
deb_mask = dre_edgemask(den_final)
deb = Placebo.deband(den_final, radius=14.5, thr=3.6, grain=0)
deb_merge = deb.std.MaskedMerge(den_final, deb_mask)
deb_final = replace_ranges(den_final, deb_merge, deb_range)

#Regrain
grain_dyn = AddGrain.grain(deb_final, 0.48, dynamic=True)

#Final
final = finalize_clip(grain_dyn, 10)
set_output(final)