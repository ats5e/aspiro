# Aspiro brand language

Design reference for Aspiro Management Consultants. Use this to apply the Aspiro identity to any long-form document: whitepapers, points of view, proposals, reports. It mirrors the system used on aspiro.me.

Aspiro is an independent, partner-owned management consultancy for GCC financial institutions, founded in Dubai in 2015, with offices in Dubai, Riyadh and London. The brand should feel like a senior banker's counsel: calm, precise, confident, never loud.

Strapline: **Leading with clarity. Delivering the difference.** (always on two lines when set as display text)

---

## 1. Colour

Deep purple carries authority. Teal is the single accent and is used sparingly. Everything else is paper, ink and grey.

| Token | Hex | Role |
|---|---|---|
| Purple (primary) | `#2B0E48` | Headings, primary buttons, dark section backgrounds, cover |
| Purple 2 | `#3D1A63` | Hover states, gradient partner to primary |
| Purple deep | `#1A0830` | Deepest background in gradients |
| Ink | `#120B1C` | Near-black backgrounds (footers, dark sections) |
| Teal (accent) | `#40B8A2` | Rules, markers, the italic accent word on dark, buttons on purple |
| Teal 2 | `#2A8F7C` | Accent text on white (AA contrast), labels, the italic accent word on light |
| Teal bright | `#6FD6C0` | Accent text and labels on purple or ink |
| Paper | `#FFFFFF` | Page background |
| Paper 2 | `#F6F4F9` | Tinted background for alternating sections and sidebars |
| Text | `#1A1425` | Body copy |
| Muted | `#5D566A` | Secondary body copy, captions, metadata |
| Line | `rgba(43,14,72,0.12)` | Hairlines on light |
| Line strong | `rgba(43,14,72,0.22)` | Card borders, table rules on light |
| Line on dark | `rgba(255,255,255,0.14)` | Hairlines on purple or ink |

Rules

- Headings are **always purple** on light backgrounds and **white** on dark. Never black, never grey.
- Teal is an accent, not a fill. Use it for rules, small labels, numbers, the accent word and one button per dark panel. Never as a background for text-heavy areas.
- Dark panels use purple (`#2B0E48`) for warmth or ink (`#120B1C`) for depth. A subtle diagonal gradient from purple deep to purple is acceptable for covers.
- On purple, a teal button uses purple text (not white) for contrast.
- No gradients on text. No drop shadows on type. No neon, glows or glowing lines.

---

## 2. Typography

Two families, one job each.

**DM Sans** (Google Fonts) for everything: headings, body, labels, numbers. Weights 300, 400, 500, 600, 700. Headings in 600 with tight tracking.

**Instrument Serif Italic** (Google Fonts) for one accent word inside a heading and for pull quotes only. Never for body copy, never in labels.

For print or PowerPoint where DM Sans is unavailable, Aspiro's deck standard is **Avenir**: Avenir Heavy for headings and labels, Avenir Book for body. Keep the same proportions below.

### Scale (web reference, scale to page size)

| Style | Size | Weight | Line height | Tracking | Colour |
|---|---|---|---|---|---|
| Display (cover, page title) | 76 px | 600 | 1.02 | -0.035em | Purple |
| Title (section) | 62 px max, 34 min | 600 | 1.04 | -0.03em | Purple |
| Heading 2 | 30 px | 600 | 1.2 | -0.025em | Purple |
| Heading 3 / card title | 22 to 24 px | 600 | 1.1 | -0.025em | Purple |
| Lead | 20 to 22 px | 400 | 1.5 | -0.01em | Muted |
| Body | 17 to 18 px | 400 | 1.75 to 1.8 | 0 | Text |
| Secondary body | 15 px | 400 | 1.65 | 0 | Muted |
| Label / eyebrow | 12 px | 700 | 1 | +0.14em, uppercase | Teal 2 (Teal bright on dark) |
| Stat number | 44 to 60 px | 600 | 1 | -0.045em | Purple (Teal bright on dark) |
| Pull quote | 24 to 30 px | Instrument Serif Italic 400 | 1.3 | -0.01em | Purple |

For an A4 whitepaper at print scale: display 40 to 48 pt, section title 28 to 32 pt, H2 18 to 20 pt, body 10.5 to 11 pt on 15 to 16 pt leading, labels 8 pt tracked.

### The accent word

Every major heading may carry **one** word set in Instrument Serif Italic, slightly larger (1.08em) and in teal 2 (teal bright on dark). It should be the word that carries the meaning:

- We engineer *clarity* for the most ambitious financial institutions.
- We don't just advise. We *engineer* outcomes.
- Outcomes delivered. Results that *speak*.
- Senior practitioners. Real *accountability*.

One accent word per heading. Never two. Never in body text.

### Labels

Section eyebrows and metadata are 12 px, bold, uppercase, tracked 0.14em, in teal 2. Plain text only: **no dot, bullet, icon or line before the label.** Examples: `OUR APPROACH`, `CASE STUDY`, `SMART OPS / MCUBED`.

---

## 3. Layout and spacing

- Content measure for long-form text: 66 to 72 characters (about 720 px on web, 110 to 120 mm on A4).
- Generous section spacing: 80 to 140 px between sections on web; 18 to 24 mm on print.
- Grid: 12 columns, 24 px gutters. Two-column text layouts pair a purple heading on the left with lead copy on the right.
- Corners: 20 to 24 px radius on cards and images on web; 4 to 6 mm on print. Buttons are pills.
- Hairline rules (1 px, line colour) separate list rows and table rows. A 2 to 3 px teal rule is the hover or emphasis state.
- Alternate white and paper 2 sections. Use one purple or ink section per document as a moment of weight (a key framework, the method, or the close).

---

## 4. Components

**Section head.** Label, then title (with optional accent word), then a short note on the right at 16 px muted, max 380 px wide.

**Stat band.** Three or four large numbers on a purple background, teal bright numerals, 15 px muted-white labels, each stat with a thin left rule. Numbers stay short (`$25M`, `70%`, `Top 5`, `Zero`).

**Numbered principles.** Cards with `01` `02` `03` in tracked teal 2, a 22 px purple heading and 15.5 px muted body. Three across. Hairline border, 20 px radius, white on paper 2 or paper 2 on white.

**Timeline / engagement model.** Four phases on a single hairline: numbered purple circles, phase name in purple, period in tracked teal 2 (`WEEKS 1–2`), four short bullets separated by hairlines.

**Case study block.** Category label, large metric in purple, uppercase sub-line in muted, title, client descriptor, then three columns: **The challenge / What we did / The outcome** with tracked teal 2 headings.

**Pull quote.** Instrument Serif Italic, 24 to 30 px, purple, with a 3 px teal rule on the left. One per two pages at most.

**Sidebar / capabilities box.** White card, hairline border, tracked label heading, list rows separated by hairlines with a short teal dash before each item.

**C-suite table.** Rows of role (28 px purple) with subtitle, then two columns: *Your challenge* (17 px purple, medium) and *How we help* (15.5 px muted with a bold purple lead sentence).

**Call to action.** Purple panel: label in teal bright, white title with accent word, lead in muted white, teal pill button with purple text, email address underlined below.

**Buttons.** Pill shape. Primary: purple fill, white text. Ghost: transparent, line-strong border, purple text. On dark: teal fill, purple text, or white fill, purple text.

---

## 5. Imagery

Photographic, not illustrative. Editorial architectural photography graded into the palette.

- **Subject:** modern Gulf architecture, glass towers, atria, bridges, skylines across water, precision objects (machined glass, watch movements), infrastructure (ports, solar, turbines) when the topic warrants.
- **Light:** dusk or blue hour. Deep aubergine skies, teal reflections in glass and water, warm window light.
- **Grade:** shadows toward `#2B0E48`, highlights toward `#40B8A2`. Muted, cinematic, restrained.
- **Composition:** generous negative space, strong geometry, medium-format feel.
- **Never:** people as subjects, text or logos in the image, neon tubes, glowing lines, lens flare, 3D renders, stock-photo handshakes, silhouettes walking toward light, circuit boards.
- **Never reuse** the same image twice in one document. Each section that needs an image gets its own.
- Images sit in rounded frames on light pages, or bleed as a darkened background (image at 50 percent opacity under an ink-to-transparent gradient) behind white text on dark sections.

Generation prompt seed, if creating new imagery: *"Realistic editorial photograph, medium format, cinematic and restrained. Colour grade dominated by deep aubergine purple (#2b0e48) shadows and soft teal (#40b8a2) highlights, dusk light. No people, no text, no logos, no neon, no glowing lines, no lens flare."*

---

## 6. Voice

British English. Senior advisory register. Specific over generic.

- Say what is right, not what is welcome. Confident, never boastful.
- Lead with the point, then the evidence. Numbers where they exist: `$25M cost savings`, `70% reduction`, `1,200+ hours`.
- Short sentences. Plain verbs. One idea per sentence.
- Practitioner framing: *"people who have sat in your seat"*, *"we never leave the room"*, *"strategy survives contact with reality"*.
- Avoid consulting clichés: synergise, leverage, best-in-class, holistic, journey, ecosystem (unless literal), transformative.
- Avoid the AI tells: no em dashes, no rhetorical triplets for their own sake, no "in today's fast-paced world".
- Regional specificity earns trust: name the regulator (SAMA, CBUAE, QCB), the standard (IFRS S1/S2, Basel III, UAE Decree-Law No. 11), the programme (Vision 2030, Nitaqat).

Positioning pillars to draw on: **Independent** (investor-free, no alliances, no referral fees), **Practitioner-led** (20+ years, ran banks), **Outcome-based** (measured on the P&L, fees linked to results).

---

## 7. Whitepaper structure

1. **Cover.** Full purple (or purple-deep to purple gradient). White Aspiro logo top left. Label in teal bright (`POINT OF VIEW` or `WHITEPAPER · 2026`). Display title in white with one teal accent word. One-line subtitle in muted white. Optional darkened hero image bleed on the lower half.
2. **Executive summary.** Paper 2 panel. Three to five short paragraphs or a numbered list of the argument. A stat band if the numbers are strong.
3. **Body sections.** Label, section title with accent word, lead paragraph in muted, body in text colour. One image or one component (timeline, principles, table) per section. Pull quote every two to three pages.
4. **Case evidence.** One or two case study blocks (challenge / what we did / outcome). Client names withheld; numbers real.
5. **What to do on Monday.** A numbered principles card set: three to five concrete actions.
6. **About Aspiro.** Short: founded 2015, Dubai HQ, Riyadh and London, 100+ years leadership experience, 8,000+ specialist network, 24+ programmes, investor-free.
7. **Close.** Purple CTA panel. Strapline on two lines. Contact: info@aspiro.me · +971 5230 8566 · aspiro.me · Dubai · Riyadh · London.

Running furniture: small logo top left of each spread, page number bottom right, `Aspiro Management Consultants` bottom left in muted, 8 pt. Confidential documents add `Confidential` after the name.

---

## 8. Logo

Wordmark "aspiro" in purple with the teal stacked-chevron mark to the left. Use the white version on purple or ink. Minimum clear space equal to the height of the mark. Never recolour, outline, stretch or place on a busy image without a dark overlay.

Assets in the site repository: `public/LogoAspiro.png` (colour), `public/icon-512.png` (mark only). The deck skill bundles `aspiro_logo_white.png`.

---

## 9. Quick checklist

- Headings purple (white on dark), never black.
- One serif italic accent word per heading, teal.
- Labels: uppercase, tracked, teal, no dot or icon.
- Teal as accent only.
- One photograph per section, none reused, all in the dusk aubergine-teal grade, no people, no text, no neon.
- Pill buttons. Hairline rules. 20 to 24 px radii.
- British English, specific numbers, named regulators, no clichés.
- Strapline on two lines. Contact block on the close.
