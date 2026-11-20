[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/arrahman13/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/arrahman13/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Image — Thursday, 19 November 2026

An entry for the make.fun bounty [Sum up 19 November's world news in one image](https://make.fun/bounty/news-image-20261119).

The entry is a single 1024 × 1024 PNG drawn as a broadsheet newspaper front
page: one hero story, a late-wires ticker, and eight story cards, all set in
a clean two-row grid that stays legible at thumbnail size.

## The day's front page

**Hero — the Shenzhen summit.** Donald Trump, Xi Jinping and Vladimir Putin
held their first three-way summit in Shenzhen and released a "peace
declaration" that never mentions Ukraine. The panel shows the Shenzhen
skyline at dusk, the three national flags, and an empty summit table.

**The eight cards:**

1. **Myanmar guilty of genocide, ICJ rules** — the World Court's first
   genocide verdict against a state, over the 2017 campaign against the
   Rohingya.
2. **Anthropic's record IPO tests AI boom** — a record market debut raising
   about $81bn.
3. **Wall Street slides for a fifth day** — the S&P 500 fell 2% and gold hit
   a 14-month low.
4. **Somalia expels UAE ambassador** — the envoy was given 72 hours to leave
   amid "open invasion" accusations.
5. **Denmark seals Greenland deal, 109–0** — parliament ratified the US
   security pact.
6. **Top court orders Han retrial** — South Korea's Supreme Court overturned
   ex-PM Han Duck-soo's 15-year martial-law sentence.
7. **Senate rejects Iran war-powers curb, 51–48** — the House-passed
   resolution was defeated.
8. **GTA VI is finally out** — Rockstar's long-delayed blockbuster launched
   worldwide.

**Late wires ticker:** Ukraine hits the Crimean Bridge a third time · Haiti
police raid kills 34 gang suspects · the EU confirms an AI-driven
cyberattack on the Commission · Voyager 1 reaches one light-day from Earth.

Every story was verified against wire and primary reporting of the day
(Reuters, UN News, AP, The Register and national broadcasters) before it
went on the page.

## How it runs

The graded program is `main.py` (Python 3.13, standard library only). The
finished artwork is committed as `entry.png`, and the program simply copies
it, byte for byte, to `entry.png` inside the output directory —
`$MAKEFUN_OUTPUT_DIR` when that variable is set, otherwise `/output`:

```sh
python3 main.py
```

Because the output is a copy of a fixed file, running the program twice
produces byte-identical results.

## Rebuilding the artwork

The page is hand-authored as vector shapes and text in `entry.svg`.
`build_image.py` rasterises it with CairoSVG and checks the result is a
1024 × 1024 PNG of at most 1 MiB:

```sh
pip install cairosvg
python3 build_image.py
```

## Files

- `main.py` — the entry program (deterministic copy of the artwork)
- `entry.png` — the rendered front page, 1024 × 1024
- `entry.svg` — the hand-drawn vector source of the page
- `build_image.py` — renders and validates `entry.png` from the SVG
- `LICENSE` — MIT

Made for the [news-image-20261119 bounty on make.fun](https://make.fun/bounty/news-image-20261119).
