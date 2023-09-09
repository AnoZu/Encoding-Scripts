from vstools import core, set_output, join, finalize_clip, replace_ranges
from vsmuxtools import src_file
from vsdenoise import BM3DCudaRTC, nlm, MVTools, Prefilter, MotionMode, SADMode, SearchMode, WeightMode
from vsdeband import AddGrain
from vsdehalo import base_dehalo_mask, edge_cleaner

fl_range = [(74, 574), (1004, 27700), (27753, 27757), (27759, 27761), (27764, 27767), (27893, 27895), (27903, 27910), (27974, 109588), (119931, 120068)]

core

#Source
web_dl = src_file(R"D:\data\torrents\Spirit.Stallion.Of.The.Cimarron.2002.1080p.BluRay.REMUX.AVC.TrueHD.5.1-EPSiLON.mkv")
src = web_dl.src

#Denoise
mv_ref = MVTools.denoise(src, thSAD=150, prefilter=Prefilter.DFTTEST, block_size=32, overlap=16, motion=MotionMode.HIGH_SAD, sad_mode=(SADMode.ADAPTIVE_SPATIAL_MIXED, SADMode.ADAPTIVE_SATD_MIXED), search=SearchMode.DIAMOND)
den_y = BM3DCudaRTC.denoise(src, ref=mv_ref , sigma=1, tr=2, planes=0)
den_uv = nlm.nl_means(src, ref=mv_ref, strength=0.4, tr=2, wmode=WeightMode.BISQUARE_HR, sr=3, planes=[1, 2])
den_final = join(den_y, den_uv)

#Dehalo
deh_mask = base_dehalo_mask(den_final, expand=0.2, iterations=2, brz0=0.2)
edge_clean = edge_cleaner(den_final, strength=10, rmode=16)
dehalo_fin = edge_clean.std.MaskedMerge(den_final, deh_mask)

#Regrain
grain_static = AddGrain.grain(dehalo_fin, 0.08, dynamic=False)
grain_dyn = AddGrain.grain(grain_static, 0.2, dynamic=True)

#Final
final = replace_ranges(src, grain_dyn, fl_range)
encode = finalize_clip(final, 10)

set_output(encode)