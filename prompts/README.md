# Prompt Library

[![Prompt Eval](https://github.com/joshuablakemorekay/tpa-honey-website/actions/workflows/prompt-eval.yml/badge.svg)](https://github.com/joshuablakemorekay/tpa-honey-website/actions/workflows/prompt-eval.yml)

This folder documents the GenAI prompts used for T.P.A. Honey Farm's marketing. It exists as portfolio evidence of prompt design, evaluation and honest record-keeping — not as runtime configuration for the website.

Each prompt directory contains the final prompt, the reasoning behind it, **a record of what I changed about the output before using it**, and an executable evaluation rubric. Every rubric runs on every push via GitHub Actions.

## Index

| Prompt | Category | What it does | Iterated? | Engineered on output |
|---|---|---|---|---|
| [`social-post-text-longan-honey`](./social-post-text-longan-honey/) | content | Bilingual Thai/English Facebook post for Longan Honey, built from facts on the live site | No | changed, not tracked |
| [`social-post-image-longan-honey`](./social-post-image-longan-honey/) | content | Matching 1200×628 product image in the site's own colours | No | changed, not tracked |

## Engineering on the outputs

Both prompts went into Meta AI exactly as drafted and both came back usable first time. I then changed the results "how I wanted it" — but I didn't log what I changed, so both rows say *not tracked* rather than pretending to a number. The next run should record the delta; that's noted in each `REASONING.md` under "What I'd change next".

## Where the facts came from

Nothing in either prompt is invented. The Thai brand name, the farm's location (Chai Badan, Lopburi), the product list, the phone number and the hex colours were all read from this repo's templates and CSS before the prompts were written. That's the main thing these two prompts demonstrate: **ground the prompt in the real source, then constrain the model** (no medical claims, Thai first, gold-led not pink-led).

## A note on evaluating an image prompt

A script can't look at a picture, so the image rubric scores a reviewer's checklist — eight true/false answers filled in after looking at the image — instead of the image itself. The fixture in `.fixtures/` shows the shape. It's an honest limit, not a workaround: the checklist is what a human would check anyway, and writing it down makes the review repeatable.

## Skills demonstrated

- [x] **Prompt design** — every prompt has a documented goal and structure
- [ ] **Iteration** — neither prompt needed a second version yet; `versions/` will appear when one does
- [x] **Evaluation** — every prompt has a rubric with executable pass conditions
- [x] **Automated testing** — rubrics run on every push via [`prompt-eval.yml`](../.github/workflows/prompt-eval.yml)
- [x] **Regression prevention** — `--fail-under 0.8` blocks merges that drop score below threshold
- [x] **Documentation** — every prompt has a REASONING.md explaining the *why*
- [x] **Honesty** — "not tracked" is written where it's true, rather than a made-up percentage
- [x] **Consistency** — all prompts follow the same file structure and metadata

## How to read this folder

- **90 seconds:** read this index, then `social-post-text-longan-honey/REASONING.md`.
- **5 minutes:** both REASONING files, then the two rubrics.
- **Longer:** the [CHANGELOG](./CHANGELOG.md), then run the eval runner.

## Running the evaluations locally

```bash
pip install pyyaml
python scripts/eval_runner.py --provider mock
```

This validates every prompt against its rubric using deterministic fixtures (no API costs). See [`results-summary.md`](./results-summary.md) for the latest run.

On Windows, prefix with `PYTHONIOENCODING=utf-8` (or `$env:PYTHONIOENCODING="utf-8"` in PowerShell) so the Thai in the fixtures prints without errors.

## Changelog

See [`CHANGELOG.md`](./CHANGELOG.md).
