# 🍯 T.P.A. Honey Farm Website

**ฟาร์มผึ้งเทพภักดี**

A bilingual (Thai/English) brochure website for T.P.A. Honey Farm, a family bee farm in Lopburi, Thailand — built in Flask, pre-rendered to static files, and served from Cloudflare Pages.

**👉 Live site: https://tpa-honey-website.pages.dev**

## What It Does

- **Bilingual throughout** — every page reads in Thai and English
- **Product catalogue** — Honey, Bee Pollen, Royal Jelly, Honey Comb, Propolis, Luffa and Spa Products, each with its own page
- **Photo gallery** — real product photography lifted from the farm's printed brochures
- **Works on phones** — responsive layout for desktop, tablet and mobile
- **Loads instantly** — no server to wake up, about 0.3 seconds to first paint

## Built With

- **Python (Flask)** — assembles the pages from one product dictionary
- **HTML, CSS, JavaScript** — the pages themselves; no framework
- **Cloudflare Pages** — hosts the pre-rendered static output
- **PyMuPDF** — used once, to pull the photos out of the farm's brochure PDFs

## Architecture

- `app.py` — the Flask app. Holds `PRODUCTS` (every product in both languages) and `CONTACT_INFO` at the top, then one small route per page. Routes only render; there's no form handling or database.
- `templates/` — one Jinja template per page, all extending `base.html`.
- `static/` — product photos, plus the brochure images and text they were extracted from.
- `freeze.py` — renders every route once and writes plain HTML to `dist/`. This is what gets deployed.
- `extract_images.py` — one-off helper that pulled the photos out of the brochure PDFs.
- `prompts/` — the GenAI marketing prompts used for the farm's social media, with reasoning and executable rubrics. See [`prompts/README.md`](./prompts/README.md).
- `scripts/eval_runner.py` + `.github/workflows/prompt-eval.yml` — run the prompt rubrics on every push.

The reason it's a Flask app that gets frozen rather than hand-written HTML: the product data lives in one place and the templates stay DRY, but visitors get static files with no cold start.

## How to Run It

1. Clone and install:
   ```bash
   git clone https://github.com/joshuablakemorekay/tpa-honey-website.git
   cd tpa-honey-website
   pip install -r requirements.txt
   ```
2. Run the dev server:
   ```bash
   python app.py
   ```
3. Open http://localhost:5000

To publish a change:
```bash
python freeze.py
wrangler pages deploy dist --project-name=tpa-honey-website --branch=main
```

The older Render deployment is still up at https://tpa-honey-website.onrender.com but sleeps when idle, so the first visitor after a quiet spell waits around 20 seconds.

## Testing

No automated tests for the website yet — next step is a smoke test that renders every route in `freeze.py`'s `PAGES` map and checks for a 200 and the Thai brand name in the body.

The prompt library is tested: every rubric in `prompts/` runs against fixtures on every push.
```bash
pip install pyyaml
python scripts/eval_runner.py --provider mock
```

## Engineering Decisions

- **Pre-render to static instead of running a server.** Every route is read-only, so a server has nothing to decide at request time. Freezing removed the ~20 second Render cold start entirely.
- **Product data as a Python dictionary, not a database.** Seven categories that change a few times a year — a database would add a deploy step and a failure mode for no benefit.
- **Ground the marketing prompts in the site's own content.** Brand name, location, phone and hex colours are read from the templates, so nothing in a generated post can contradict the website it links to.
- **Score the image prompt with a reviewer's checklist.** A script can't look at a picture; writing the eight checks down as JSON makes the human review repeatable and lets CI enforce the shape.

## My Journey

Full entries in [`JOURNAL.md`](./JOURNAL.md).

**2026-09-17 — Two GenAI marketing prompts, archived with a receipt.** Used the real farm as the brand for a course activity on GenAI social posts, then archived both prompts under `prompts/` with reasoning, executable rubrics and CI. Key lesson: an image can't be scored by a script, so the rubric scores the reviewer's checklist instead — and "not tracked" is the honest value when the edits weren't logged.

**2026-09-12 — Froze the site and moved to Cloudflare Pages.** Replaced the sleeping Render deployment with static output from `freeze.py`; first paint dropped from ~20s cold to ~0.3s.

**2025-12-10 — First version.** Flask app with bilingual product catalogue and gallery, photos extracted from the farm's brochure PDFs.

## What's Next

- **Testing** — a route smoke test for the site itself (the weakest area right now).
- **Housekeeping** — `app_OLD.py` and the `TPA_DEPLOYMENT_COMPLETE` bundle are stale duplicates that git history already keeps.
- **Prompts** — log what changed after the next Meta AI run so the delta becomes a receipt.

## Contact

**T.P.A. Beekeeping Farm / ฟาร์มผึ้งเทพภักดี**

- **Address**: 143/139 Arun Amarin, Bangkok Noi, Bangkok 10700, Thailand
- **Phone**: 02-884 6177, 434 3031
- **Email**: tpa_farm@yahoo.com

## License

See [`LICENSE`](./LICENSE) — the code is mine, the content and photos belong to the farm.

---

🐝 Made with love and honey 🍯
