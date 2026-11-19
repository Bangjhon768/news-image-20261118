# Sum up 18 November's world news in one image

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/Bangjhon768/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/Bangjhon768/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

An entry for the [make.fun](https://make.fun) bounty "Sum up 18 November's world news in one image".

## What it is

A one-page newspaper front page that sums up Wednesday 18 November 2026 in a single image (`entry.png`). The program (`main.py`) copies the image to the output directory; it runs with no network and writes identical bytes on every run.

## The stories on the page

- **Gulf crisis** — Iran strikes US bases in Kuwait and Bahrain after US jets hit a missile site on Iran's Qeshm Island.
- **Ukraine** — Ukrainian drones and missiles partly destroy the Kerch Bridge to Crimea; an arch collapses.
- **APEC, Shenzhen** — Xi Jinping and Vladimir Putin meet a day before a first trilateral summit with Donald Trump.
- **US politics** — Mary Peltola wins Alaska's Senate seat; Democrats take a 56–44 majority.
- **Health, Africa** — The Ebola outbreak in DR Congo passes 11,000 cases.
- **Also today** — Voyager 1 reaches one light-day from Earth; the US loses its measles-free status; Houthi drones target Saudi oil pipeline pumps.

All stories are as reported by wire services on the day.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.png` (1024 × 1024 PNG).
