# NivelCrack Web Redesign — Design Direction

## References
- **Moodboard:** [Figma Moodboard](https://www.figma.com/design/idZqqqigVspQBNAD5zhsIY/NivelCrack?node-id=17-267&t=oEBhDuZtwDGKamti-1) — kept for inspiration only; design work happens in code.
- **Current Site:** [https://en.nivelcrack.com/](https://en.nivelcrack.com/)

## Brand Assets
- **Display font:** `Assets/EurostileLTStd-BoldEx2.otf` — Eurostile LT Std Bold Extended 2. Used for the logo AND as the primary display typeface across the site.
- **Logo monogram:** `Assets/NC_Logo_Monogram.ai` — NivelCrack monogram mark (Adobe Illustrator source file)

## Workflow
All design mockups are built directly in HTML/CSS — no Figma. Mockups are structured to translate cleanly into Shopify Liquid later: semantic markup, CSS custom properties for tokens, no build tools or JS frameworks. Magazine layout references (provided as images) get adapted through the NivelCrack design system rather than copied literally.

## Overview
NivelCrack is a Korean soccer fashion and culture brand. This redesign reimagines the site as a modern, minimalist e-commerce experience rooted in the concept of a vintage soccer magazine — but executed with clean, contemporary UI. The magazine metaphor provides the conceptual structure (cover, editorial spreads, collectible cards), while the actual design language stays restrained, functional, and minimal.

The site should feel like a beautifully edited magazine that happens to sell products — not a novelty throwback or a literal vintage recreation.

---

## Concept

### The Magazine Metaphor
- **Homepage** = magazine cover. The NVLCRK logo centered at the top like a masthead. Hero imagery treated like a cover story.
- **Product Grid (Shop)** = editorial spread / sticker book page. Products laid out in a grid that evokes the feel of a Panini sticker collection page — structured, collectible, organized by collection.
- **Product Page** = modern trading card. Each product presented in a card-like container — clean borders, structured data layout, minimal detail. Not a replica of any specific trading card, but unmistakably card-inspired. Think: modern minimalist collectible card with tight typography and clean lines.
- **Interior pages** (About, Cafe, Archive) = magazine interior editorial pages. Clean layouts, generous whitespace, editorial photography treatment.

### Editorial Devices (the magazine vocabulary)
These are the recurring editorial mechanisms we pull from print magazines. They're how the magazine feel actually shows up on the page:

- **Drop caps** — oversized first letter on editorial/long-form openings (About, Archive entries, collection stories).
- **Pull quotes** — large serif quotes breaking up long text, used on About and editorial pages.
- **Bylines & datelines** — small-caps labels (e.g., `ISSUE 01 · SS26 · SEOUL`) placed under headlines and above sections to feel like a masthead.
- **Section numbers / dividers** — numbered section markers (`01 / COLLECTION`, `02 / ARCHIVE`) acting as editorial wayfinding.
- **Multi-column text** — two- or three-column body text on editorial pages where appropriate.
- **Asymmetric grids** — Home, About, and Archive can break the strict 12-column grid. Large image on one side, tight text column on the other; overlapping elements; intentional imbalance. Shop and Product pages stay tidier for scannability.
- **Issue/masthead framing** — Homepage treated like a cover with an issue number, date, and cover line.

### How Far to Push the Metaphor
The magazine concept is a structural and tonal reference — it should inform layout decisions and the overall feel, but never compromise clean e-commerce usability. Navigation should not literally look like a table of contents. Product grids should not sacrifice scannability for editorial flair. Editorial devices (drop caps, pull quotes, asymmetric grids) belong on editorial pages — Home, About, Archive, collection stories. Shop, Product, Cart, and Account stay clean and utilitarian. The metaphor is the vibe, not the UI pattern.

---

## Color

### Palette
- **Neutral foundation only.** No brand accent colors in the base design system.
- Black, white, and warm grays as the core palette.
- Avoid pure stark black (#000) and pure white (#FFF) — use slightly warm or off-tones to add depth without adding color.

### Accent Color Strategy
- Accent colors are introduced per-collection or per-collaboration, not as a permanent part of the system.
- The design system should include a mechanism for swapping in a single accent color that can cascade through collection-specific pages (e.g., a collaboration drops with a specific team color that tints buttons, borders, or highlights on that collection's pages).
- The base/default state of the site is entirely neutral.

### Suggested Neutrals
- Background: `#FAFAFA` (warm off-white)
- Surface/Card: `#FFFFFF`
- Primary text: `#1A1A1A` (near-black)
- Secondary text: `#6B6B6B`
- Borders/dividers: `#E5E5E5`
- Subtle hover/active states: `#F0F0F0`

---

## Typography

The type system uses **two** typefaces. Eurostile for display. Inter for everything else. Serifs were considered and rejected — they don't fit the NivelCrack aesthetic, which is cleaner and more technical than classic editorial.

### 1. Display — Eurostile LT Std Bold Extended 2
- **File:** `Assets/EurostileLTStd-BoldEx2.otf` (loaded via `@font-face`, served as `/assets/EurostileLTStd-BoldEx2.otf` in Shopify)
- Wide, geometric, bold sans with a technical/futuristic edge. All-caps, tight tracking.
- **Used for:** the NVLCRK wordmark/masthead, hero headlines, section titles, cover lines, issue numbers, pull quotes, any moment where the brand needs to feel bold and authoritative.
- Always uppercase. Letter-spacing varies by size: tighter on huge display (`-0.01em` to `0`), slightly open on smaller titles (`0.02em`).
- **Fallback stack:** `"Eurostile LT Std", "Oswald", "Arial Narrow", sans-serif` — Oswald Bold is the Google Fonts fallback if the OTF fails to load.

### 2. Everything Else — Inter
- **[Inter](https://fonts.google.com/specimen/Inter)** (Google Fonts, free, variable weight)
- The site's workhorse — body copy, editorial long-form, UI labels, buttons, navigation, metadata, captions, product descriptions, prices, form fields, pull quote attribution, drop caps, footnotes.
- Weights to use: Regular (400) for body and long-form, Medium (500) for UI labels and buttons, SemiBold (600) for subheads and emphasis, Bold (700) for drop caps and pull quote fallbacks.
- **Two modes of Inter:**
  - **Editorial mode** — sentence case, tight-to-default letter-spacing, line-height 1.55, used for body/lede/long-form.
  - **UI mode** — uppercase, letter-spacing 0.05em, Medium weight, used for labels, buttons, metadata, and masthead chrome.
- The contrast between these two modes is what gives Inter enough range to replace both a body serif and a UI sans.

### Why two fonts
The magazine feel comes from layout, hierarchy, editorial devices, and photography — not from mixing typefaces. A tight two-font system (one loud display + one disciplined workhorse) is more modern, more brand-aligned, and performs better. Eurostile is the voice; Inter is the substrate everything else is printed on.

### Type Scale
- **Micro/Caption:** 11–12px / Inter Medium / uppercase / letter-spacing 0.05em
- **Small/Meta:** 13px / Inter Regular
- **Body:** 16–17px / Inter Regular / line-height 1.55
- **Body Large / Lede:** 19–21px / Inter Regular / line-height 1.5
- **Subhead:** 22–28px / Inter SemiBold or Eurostile
- **Section Title:** 32–48px / Eurostile / uppercase
- **Hero / Cover Line:** `clamp(3rem, 8vw, 7rem)` / Eurostile / uppercase
- **Pull Quote:** 28–40px / Eurostile uppercase OR Inter SemiBold (decide per page)
- **Drop Cap:** `4em` / Inter Bold / float left

### Typography Principles
- **Two faces, clear roles. Never blur.** Eurostile is never used for body. Inter is never used for hero headlines or the masthead.
- Uppercase is intentional — display headlines and UI labels only. Body and editorial text are always sentence case.
- Generous letter-spacing on uppercase (Eurostile display: `0–0.02em`, Inter labels: `0.05em`). Tight or default on body.
- Line-height is generous on body (`1.5–1.6`) for readability; tight on display (`0.95–1.1`) for impact.

---

## Layout

### Grid
- **Baseline: 12-column grid** for desktop, collapsing to 4 columns on mobile. Generous margins and gutters — the site should breathe.
- Max content width: ~1200–1400px, centered.
- **Permission to break the grid:** Home, About, Archive, and editorial/collection story pages can use asymmetric layouts — large image hugging one edge, tight text column opposite, intentional imbalance, overlapping elements, off-center type. This is where the magazine feel comes from.
- **Pages that stay on-grid:** Shop, Product, Cart, Account, Search. These are transactional and need scannable structure.

### Spacing
- Use a consistent 8px spacing scale (8, 16, 24, 32, 48, 64, 96).
- Sections should have significant vertical padding (64–96px) to reinforce the editorial, magazine-like pacing.

### General Principles
- Clean, uncluttered layouts with ample whitespace.
- Imagery should be large and given room — products are the content, not decoration.
- Minimal UI chrome. Borders and dividers used sparingly.
- No unnecessary motion or animation. If something moves, it should have a functional reason.

---

## Components

### Navigation
- Clean top nav bar. NVLCRK logo centered (magazine masthead style). Navigation links flanking or below.
- Utility icons (search, cart, account) aligned right.
- Mobile: hamburger menu, logo centered.
- Nav should feel minimal — not heavy or complex.

### Collection Row (Shop / Grid View)
The Shop page is organized as a series of horizontal **collection rows**, not a flat grid of products. Each collection — West Ham United, Club America, Fresh Patterns Collective, Classic Football Shirts, etc. — gets its own row. A row is a three-zone horizontal spread:

1. **Collection name (far left)** — large Eurostile uppercase title. Supporting metadata underneath (issue number, year, short descriptor) in small-caps Inter.
2. **Items list (middle)** — vertical list of the individual products in that collection, rendered as plain text in 11px Inter Medium uppercase. This is the textual catalogue of the collection — readable at a glance before you look at the images.
3. **Product images (right)** — tight grid of product tiles, unlabeled by default. On hover, each tile reveals the product name and the associated club crest or flag as an overlay.

This structure turns the Shop page into a series of magazine spreads — each collection is its own editorial unit, with a written catalogue running parallel to the visual one. It scales: add collections by adding rows; rows stack vertically with hairline dividers between them.

**Principles:**
- Rows are divided by thin horizontal hairlines, same treatment as the nav sections.
- Image tiles have no visible label until hover, keeping the visual catalogue clean.
- Hover reveals are subtle — a neutral overlay with the product name and crest, fading in.
- Each row can hold any number of product tiles; the images grid wraps as needed.

### Product Page (Trading Card View)
- The product detail section should be structured like a minimalist trading card:
  - Product image contained within a clean bordered frame.
  - Product name and key details (price, sizes, collection) displayed in a structured, data-dense layout — reminiscent of stats on a trading card.
  - NVLCRK branding subtly integrated (e.g., logo running vertically along the card edge, similar to the Kappa card reference in the moodboard).
- The card container should feel like an object — defined borders, intentional proportions, a sense of being a collectible.
- Outside the card: standard e-commerce functionality (add to cart, size selector, description accordion).

### Buttons
- Primary: solid fill, neutral color (near-black), white text. Rectangular with minimal or no border-radius.
- Secondary: outlined, near-black border, transparent fill.
- Keep button styling sharp and minimal — no rounded pill shapes, no gradients.

### Footer
- Minimal. Logo, essential links, social icons, legal info.
- Same restrained typography and spacing as the rest of the site.

### Editorial Components (reusable magazine elements)
These are the building blocks for editorial pages. They should be componentized early so they can be reused across About, Archive, collection stories, and any long-form content.

- **Drop Cap** — first letter of an editorial opening rendered at ~`4em`, Source Serif Bold, floated left, tightly kerned into the following text.
- **Pull Quote** — oversized serif quote block (`28–40px`, Source Serif SemiBold), with thin top/bottom rules or a leading quote mark. Breaks up long body text.
- **Byline / Dateline** — small-caps Inter label (`12px / 0.05em`) for metadata like `ISSUE 01 · SS26 · SEOUL` or `WORDS BY NIVELCRACK`. Sits above headlines or under images.
- **Section Marker** — numbered editorial wayfinding (`01 / COLLECTION`) in Eurostile or Inter uppercase, paired with a thin horizontal rule.
- **Masthead Block** — the cover-style header used on Home and collection landing pages: issue number, date, cover line, large Eurostile headline.
- **Figure + Caption** — full-bleed or contained image with a small Inter caption below (`11–12px`, italic optional). Used for all editorial imagery.

---

## Pages

### Homepage (Magazine Cover)
- NVLCRK logo as masthead, centered at top.
- Full-bleed or near-full-bleed hero image — treated like a magazine cover photo.
- Minimal text overlay on hero — just enough to communicate the latest drop or editorial.
- Below the fold: featured collections, editorial content, new arrivals — paced like flipping through magazine pages with generous spacing between sections.

### Shop (Collection Rows)
- Unified shop page combining all products, organized as a vertical stack of horizontal collection rows (see "Collection Row" under Components).
- Each row is a collection — West Ham, Club America, Fresh Patterns Collective, Classic Football Shirts, etc. — presented as a magazine-style spread with the collection title on the left, a text list of its items in the middle, and an image grid on the right.
- Filter option in top right area for cross-collection filtering (by size, availability, price).
- Rows stack vertically with hairline dividers between them.

### Product Page (Trading Card)
- Hero section is the trading card component (described above).
- Supporting content below: full description, related products, collection context.
- Clean and focused — the product is the star.

### About
- Editorial layout. Large photography, generous whitespace, story-driven.
- Tells the NivelCrack story with a magazine-interior feel.

### Cafe NivelCrack
- Similar editorial structure to About.
- Location info, photography of the space, menu or offerings if applicable.

### Archive
- Grid-based lookback at past collections and collaborations.
- Could use a timeline or season-based structure.
- More editorial/visual, less transactional than the Shop page.

### Cart
- Clean, minimal cart page. Product thumbnails, quantities, pricing.
- No clutter — straightforward path to checkout.

### Account / Login
- Simple forms. Minimal styling. Functional.

---

## Imagery & Photography Direction
- Product photography should be clean and consistent — flat lay or model shots on neutral backgrounds.
- Editorial/lifestyle photography can be grittier and more atmospheric — this is where the soccer culture and vintage spirit comes through.
- The contrast between clean product shots and textured editorial imagery creates visual interest without cluttering the UI.

---

## Summary of Principles
1. **Magazine-inspired, not magazine-cosplay.** The concept informs structure and tone, not literal UI patterns.
2. **Neutral by default, colorful by collection.** The system is a blank canvas that each drop or collab can color.
3. **Products are collectibles.** The trading card and sticker book metaphors elevate products from items to objects worth having.
4. **Less is more.** Every element earns its place. No decorative clutter, no unnecessary animation.
5. **The brand voice is confident and quiet.** Bold typography for headlines, restrained everything else. Let the products and imagery speak.
