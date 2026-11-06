"""Render repository-native social artwork with Inkscape (optional asset rebuild)."""
from pathlib import Path
import base64, subprocess, tempfile
root=Path(__file__).resolve().parents[1]
a=root/'public/jimny/assets'
def data(name,mime):
 return 'data:'+mime+';base64,'+base64.b64encode((a/name).read_bytes()).decode()
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630" viewBox="0 0 1200 630">
<rect width="1200" height="630" fill="#111"/>
<image x="460" y="0" width="740" height="630" preserveAspectRatio="xMidYMid slice" xlink:href="{data('9fd0f.png','image/png')}"/>
<image x="54" y="58" width="300" height="62" xlink:href="{data('89c2d.svg','image/svg+xml')}"/>
<g fill="white" font-family="Noto Sans CJK JP" font-weight="bold" font-size="46"><text x="54" y="255">カスタムジムニー</text><text x="54" y="326">誕生。</text></g>
<text x="54" y="405" fill="#ff6900" font-family="sans-serif" font-size="18" letter-spacing="2">CUSTOM JIMNY</text>
<text x="54" y="450" fill="white" font-family="sans-serif" font-size="15" letter-spacing="1">FULL CUSTOM / LIGHT CUSTOM</text></svg>'''
with tempfile.TemporaryDirectory() as d:
 p=Path(d)/'card.svg';p.write_text(svg)
 subprocess.run(['inkscape',str(p),'--export-filename='+str(a/'ogp.png')],check=True)
for size,name in [(32,'favicon-32.png'),(180,'apple-touch-icon.png')]:
 subprocess.run(['inkscape',str(a/'favicon.svg'),'--export-width='+str(size),'--export-height='+str(size),'--export-filename='+str(a/name)],check=True)
