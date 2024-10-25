from vstools import core, finalize_clip
import awsmfunc as awf
import vsdehalo as vsdh
from vsmuxtools import src_file, Setup, x265, settings_builder_x265, TmdbConfig, mux
from vspreview import set_output

setup = Setup("movie")

src = src_file(r"D:\media\Maronas.Fantastic.Tale.2019.1080p.BluRay.Remux.AVC.DTS-HD.MA.5.1-PmP.mkv", force_bs=True)
clip = src.init()

# Crop black bars
crop = core.std.Crop(clip, top=20, bottom=20)

# Clean dirty borders
bb = awf.bbmod(crop, top=1, bottom=1, thresh=128, blur=20)

# Clean edges and dehalo
ec = vsdh.edge_cleaner(bb)
dh_mask = vsdh.fine_dehalo.mask(bb, thmi=75)
dh = vsdh.dehalo_sigma(ec, pre_ss=2)
dhfin = core.std.MaskedMerge(ec, dh, dh_mask)

final = finalize_clip(dhfin, 10)


if __name__ == "__main__":
    settings = settings_builder_x265(
        crf=18,
        aq_strength=0.8, psy_rd=2.0, psy_rdoq=2,
        qcomp=0.72, rd=4,
        preset="slower",
        deblock=[-2, -2], ref=5, bframes=12,
        aq_mode=3, chroma_qpoffsets=-3,
        rect=False
    )
    enc = x265(settings).encode(final)
    mux(
        enc.to_track(name="Encoded by AnoZu", lang="fr", default=True),
        tmdb=TmdbConfig(568381, movie=True, language="en-US", write_ids=True, write_title=False, write_cover=True),
    )
else:
    set_output(final)