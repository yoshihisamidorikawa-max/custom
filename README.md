# BUDDICA × C.L.LINK Custom Jimny

After_04 adopted Figma LP implementation.

Preview branch: `preview/jimny-after04`.
Cloudflare Pages output: `public`; no build step.
Planned production path: `https://lp.buddica.online/jimny/`.
Production auto-deploy is disabled. Contact destination is pending.

## Editing

- `public/jimny/` contains the deployable page, stylesheet, script, and original Figma assets.
- `scripts/build.py` regenerates the static HTML with Python 3 (no external dependencies).
- Figma reference: https://www.figma.com/design/5YcFLwJpblmc6BP1seGJsj?node-id=59-489 (PC), node 59:632 (SP).
- All consultation buttons open an accessible preview-only dialog. Replace these with the approved destination before production release.
- Preview indexing is disabled using both HTML robots metadata and Cloudflare `_headers`.
- The domain route `/jimny/` must be connected separately after design review; this branch does not change production routing.

## Favicon and social sharing

- Favicon: original vector emblem, SVG plus 32px PNG and 180px Apple touch icon.
- OGP / Twitter card: `public/jimny/assets/ogp.png` (1200 × 630), composed from existing Figma assets.
- `python scripts/build.py` regenerates metadata. The default absolute URL targets the stable `preview/jimny-after04` Pages alias, not an immutable deployment URL.
- Merge this change into `preview/jimny-after04` to make the default OGP image URL available. Before production deployment, run `SITE_URL=https://lp.buddica.online python scripts/build.py` and commit the generated HTML (Pages currently has no build step).
- Optional artwork regeneration: `python scripts/render-social.py` requires Inkscape and Noto Sans CJK JP. Deployment uses checked-in images and does not require these tools.
