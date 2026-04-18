# NVLCRK Mobile Adaptation — Engineer Handoff

Mobile (≤768px) adaptation of the existing desktop NVLCRK site. Everything lives in `mobile/` alongside the original desktop tokens/components CSS. The design approach: **keep desktop intact; layer a single `mobile-overrides.css` that only fires under `@media (max-width: 768px)`**. Nothing has been forked or rewritten.

---

## What's in here

```
mobile/
  tokens.css              ← unchanged from desktop
  components.css          ← unchanged from desktop
  mobile-overrides.css    ← NEW — all ≤768px rules live here
  nav.js                  ← shared hamburger / cart-drawer / filter behavior
  Assets/                 ← product, model, archive, cafe imagery
  index.html              ← 01 — Cover / TOC
  shop.html               ← 02 — Shop grid
  product.html            ← 03 — PDP
  about.html              ← 04 — About
  archive.html            ← 05 — Archive list
  archive-01.html         ← 06 — Archive detail (template; 01-08 follow same shape)
  cafe.html               ← 07 — Cafe
  contact.html            ← 08 — Stockists

Mobile Preview.html       ← dev harness (page switcher + device-width buttons)
```

Every page includes the three stylesheets in this exact order:

```html
<link rel="stylesheet" href="tokens.css">
<link rel="stylesheet" href="components.css">
<!-- page-specific <style> block (inline) -->
<link rel="stylesheet" href="mobile-overrides.css">
```

`mobile-overrides.css` is loaded last so it wins via source order without needing `!important` (with one or two exceptions, marked inline with a comment).

---

## Conventions

- **Breakpoint.** Single breakpoint at `max-width: 768px`. No tablet tier. Everything inside the one `@media` block.
- **Design tokens.** All overrides use the existing `--space-*`, `--text-*`, and color tokens from `tokens.css`. No magic numbers except viewport-relative values (`50vh`, `100dvh`) and the breakpoint itself.
- **Source order.** The overrides file is structured top-down by page, matching the nav order. Find rules by searching for the page's section header comment (e.g. `/* ---------- shop.html ---------- */`).
- **No hover on touch.** `.specimen-card` name/price hover-swap is disabled ≤768px; the name is always visible. Archive row hover-image is likewise disabled — the label stays visible, tap opens the detail page.
- **Nav.** The desktop left rail becomes a top bar with a hamburger. `nav.js` handles toggle; the expanded menu pushes content down (in-flow, not overlay). No fixed/sticky header.
- **Cart drawer.** Full-viewport (`width: 100vw`) on mobile instead of the desktop side-slide.

---

## Per-page notes

| # | Page | Mobile pattern |
|---|---|---|
| 01 | `index.html` — Cover / TOC | Stacks to 1 column: 50vh hero photo on top, TOC contents below with logo pinned top-right. |
| 02 | `shop.html` — Shop | 2-col grid. Filter row wraps above. Card name always visible (no hover swap). |
| 03 | `product.html` — PDP | Images stack full-width, then info block. Sticky sidebar is dropped; content flows naturally. ATC button is `btn--block`. Cart drawer is full-screen. |
| 04 | `about.html` — About | Intro paragraphs use `--text-small` at secondary color. Gallery stays 2-col with 4px gap. |
| 05 | `archive.html` — Archive list | Each row is a full-width labeled block; tap opens detail. Hover image suppressed. |
| 06 | `archive-0*.html` — Archive detail | Text block spans full width at top (`grid-column: 1 / -1`), images tile below in 2-col square grid in source order. Explicit `.pos-*-*` positioning cleared at mobile so the 3-col desktop layout doesn't leak. |
| 07 | `cafe.html` — Cafe | Photo first, then info. 1-col info stack. |
| 08 | `contact.html` — Stockists | 1-col list with image thumbnails capped at 120px. |

---

## Known considerations / watch items

1. **Archive detail positioning.** Desktop uses explicit `.text-R-C` / `.pos-R-C` grid placements in `mobile-overrides.css`. I reset those at mobile to let cells auto-flow. If new archive entries are added, ensure the text block is the FIRST child inside `.archive-detail__grid` so it lands at the top.
2. **`!important` usage.** Used in two places only — both on the nav's `border-right`/`border-bottom` to beat inline page-level styles. Marked with a comment.
3. **Image cache.** The preview harness (`Mobile Preview.html`) cache-busts stylesheets and images on every reload. In production the existing HTTP caching is fine; no changes needed.
4. **Viewport meta.** Every page already ships `<meta name="viewport" content="width=device-width, initial-scale=1">`. Don't remove.

---

## Running locally

Serve the project root with any static server (`python -m http.server`, `npx serve`, etc.) and open `Mobile Preview.html` to switch pages and simulated device widths. Or open any file under `mobile/` directly in a mobile-simulated browser tab (DevTools → device toolbar → iPhone 14 / 390×844).

---

## Scope of the adaptation

In: responsive layout + nav + cart for all 8 page types above. Typography scale, spacing, and component patterns sourced from existing tokens — no new tokens introduced.

Out: perf/bundling (unchanged), analytics (unchanged), accessibility audit beyond baseline semantics, localized currency/unit toggles.
