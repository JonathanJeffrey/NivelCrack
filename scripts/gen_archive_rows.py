#!/usr/bin/env python3
"""Generate <li> rows for archive.html from titles + local images."""
from pathlib import Path

TITLES = [
    "NIVELCRACK X FRESH PATTERNS COLLECTIVE",
    "STONE ISLAND X NEW BALANCE EDITORIAL",
    "NIVELCRACK X PRATAMA ARHAN",
    "NIVELCRACK X PUMA X ATMOS AFTER PARTY",
    "NIVELCRACK X PUMA X ATMOS TOURNAMENT",
    "NIVELCRACK X PUMA X ATMOS",
    "ONLY NY TOURNAMENT 2025",
    "NSS SPORTS LVDF VOL.2 EDITORIAL",
    "NIVELCRACK X PAPERBOY PARIS 2025 NIKE TOMA SEOUL",
    "NEWCASTLE UNITED 2025 POP-UP SEOUL",
    "NIVELCRACK X CLUB AMÉRICA 2025 POP-UP TOKYO",
    "NIVELCRACK X CLUB AMÉRICA 2025",
    "ATMOSCON 2025",
    "EA FC 25 TOTY KIT PACKAGE",
    "CAFE NIVELCRACK BANDUNG",
    "NIVELCRACK X SEVMID",
    "COMPLEXCON 2024",
    "NIVELCRACK X POHANG STEELERS MATCH DAY",
    "NIVELCRACK X POHANG STEELERS X PUMA",
    "DIRT-ROOTS FC SEOUL",
    "FCRB X PAPERBOY PARIS CATERING",
    "ONLY NY TOURNAMENT 2024",
    "NIVELCRACK X PROGRESS",
    "ASIAN WIN TOURNAMENT",
    "NIVELCRACK X NSS SPORTS",
    "NIVELCRACK X CLUB AMERICA",
    "CAFE NIVELCRACK BANGKOK",
    "NIVELCRACK X VENEZIA FC",
    "ANAR FOOTBALL ARENA",
    "NIVELCRACK X SOHO WARRIORS",
    "JOGA BONITO",
    "WWC 2023 POP-UP TOKYO",
    "WWC 2023 POP-UP SEOUL",
    "NIVELCRACK X BLED FC",
    "NIVELCRACK X PAPERBOY PARIS",
    "FOOTBALL SUITE",
    "FIFA 23 CAPTAIN KOREA KIT",
    "NIVELCRACK X MIZUNO 22 AW",
    "FIFA 23 FUT KIT",
    "NIVELCRACK X MIZUNO 22 SS",
    "NIVELCRACK X MIZUNO KIT",
    "WAGMI UNITED KIT",
    "JEJU UNITED 22 SEASON BRANDING & VIDEO",
    "FIFA 22 TOTY MERCHANDISE",
    "REGAL FC TOURNAMENT",
    "NIVELCRACK X RYSE HOTEL",
    "NIVELCRACK X NEW BALANCE X BAITEZE",
    "NIVELCRACK X FIFA 21 VOLTA FOOTBALL",
    "FIFA 21 FUT KIT",
    "MIZUNO X NAGOYA GRAMPUS EDITORIAL",
    "NIVELCRACK X BALANSA",
    "FC GIRONDINS DE BORDEAUX KIT EDITORIAL",
    "NIVELCRACK X COMPASSION",
    "FIFA 21 GLOBAL TVC",
    "SEONGNAM FC MERCHANDISE & VIDEO",
    "PIZZA FOOTBALL CLUB",
    "FAR EAST DERBY TOURNAMENT",
    "NIVELCRACK X UMBRO",
    "NIVELCRACK X SOUNDS GOOD",
    "UMBRO FOOTBALL EDITORIAL & VIDEO",
    "NIVELCRACK X REEBOK KIT",
    "RED STAR FC MERCHANDISE",
    "NIKE FOOTBALL STUDIO SEOUL",
    "JEJU UNITED MERCHANDISE",
    "NIVELCRACK X NOWHERE FC KIT",
    "NIVELCRACK X JOMA SPORT KIT",
]

def classify(title: str) -> str:
    t = title.upper()
    if "POP-UP" in t:
        return "Popup"
    if "EDITORIAL" in t or t.endswith("TVC"):
        return "Editorial"
    return "Archive"

ASSETS = Path(__file__).parent.parent / "Assets" / "archive"

def find_img(i: int) -> str:
    for ext in ("jpg", "jpeg", "png"):
        p = ASSETS / f"{i:02d}.{ext}"
        if p.exists():
            return f"Assets/archive/{i:02d}.{ext}"
    return ""

rows = []
for i, title in enumerate(TITLES, 1):
    kind = classify(title)
    img = find_img(i)
    slug = f"archive-{((i - 1) % 8) + 1:02d}.html"
    rows.append(f"""          <li>
            <a href="{slug}" class="archive-row" data-type="{kind.lower()}">
              <div class="archive-row__label">
                <h3 class="archive-row__name">{title}</h3>
                <p class="archive-row__type">{kind}</p>
              </div>
              <span class="archive-row__num">{i:02d}</span>
              <div class="archive-row__media"><img src="{img}" alt="" /></div>
            </a>
          </li>""")

print("\n\n".join(rows))
