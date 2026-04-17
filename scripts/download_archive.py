#!/usr/bin/env python3
"""Download archive thumbnails from nivelcrack.com to Assets/archive/."""
import os
import urllib.request
import urllib.error
from pathlib import Path

URLS = [
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1766019634144_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1766020469308_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/88608/blogPost/image_1766017903984_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1765957872718_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1765957821012_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1765957732283_300.jpeg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1756802572979_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1756802541058_300.jpeg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1756802496565_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1756802464376_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1756802419462_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1756802334684_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1745375527847_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1741751180360_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736929682381_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736927633962_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736924281277_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736924017061_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736923925873_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736990810739_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736992933578_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736931584313_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736842351723_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736841729406_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736840907177_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1736840293820_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1709005643552_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702095600997_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702095515092_300.jpeg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702095455618_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702095229012_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702095146458_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702094868048_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1702094719546_300.jpeg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1685415987288_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677805669652_300.jpeg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677911934330_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677911953440_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677911969575_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912035877_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912058169_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912102560_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912118765_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912190645_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912203648_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912220827_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912244329_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912368498_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912387923_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912411747_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912427498_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912440166_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912451359_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677912498812_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900552083_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900479477_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900460833_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900448708_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900434202_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900420856_300.png",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900365374_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900347558_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900332470_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900297859_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900275806_300.jpg",
    "https://contents.sixshop.com/thumbnails/uploadedFiles/154434/blogPost/image_1677900245648_300.jpg",
]

OUT_DIR = Path(__file__).parent.parent / "Assets" / "archive"
OUT_DIR.mkdir(parents=True, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0"}

for i, url in enumerate(URLS, 1):
    ext = url.rsplit(".", 1)[-1].lower()
    if ext not in {"jpg", "jpeg", "png", "webp"}:
        ext = "jpg"
    name = f"{i:02d}.{ext}"
    out = OUT_DIR / name
    if out.exists():
        print(f"skip {name}")
        continue
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            out.write_bytes(r.read())
        print(f"ok   {name}  ({url.rsplit('/',1)[-1]})")
    except urllib.error.HTTPError as e:
        print(f"fail {name}  {e.code} {url}")
    except Exception as e:
        print(f"fail {name}  {e}")
