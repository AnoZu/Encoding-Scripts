from vsmuxtools import src_file, GlobSearch, Setup, SourceFilter
from vspreview import set_output


setup = Setup("02")


# Clip
debd = src_file(GlobSearch(f"*Jigokuraku - {setup.episode}*.mkv"), preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
debd_init = debd.init()
bd = debd_init[360:]

usbd = src_file(GlobSearch(f"*Paradise.S01E{setup.episode}*.mkv"), preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
usbd_init = usbd.init()

vodes = src_file(GlobSearch(f"*Jigokuraku - S01E{setup.episode} v2*.mkv"), preview_sourcefilter=SourceFilter.FFMS2, sourcefilter=SourceFilter.BESTSOURCE)
vodes_init = vodes.init(bits=10)
vodes = vodes_init[360:]

anozu = src_file(R"D:\media\Hell's Paradise (2023) S01 (1080p BluRay Dual-Audio Opus 2.0 x265) [AnoZu]\Hell's Paradise (2023) S01E02 Screening and Choosing (1080p BluRay Dual-Audio Opus 2.0 x265) [AnoZu].mkv")
anozu_init = anozu.init(bits=10)

set_output(usbd_init, "USBD")
set_output(bd, "DEBD")
set_output(anozu_init, "AnoZu")
set_output(vodes, "Vodes")