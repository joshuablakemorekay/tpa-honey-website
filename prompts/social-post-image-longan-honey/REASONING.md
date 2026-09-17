# Reasoning: Social post image — Longan Honey

This document captures the thinking behind the prompt. It exists so a reader can understand not just *what* the prompt is, but *why* it ended up this way.

## Goal

The second half of the same coursework activity: a ten-part template so Meta AI generates the image for the post. Same one-line brief from me:

> "Do it for TPA Honey"

Claude drafted it to match the text prompt — same product (Longan Honey), same platform (Facebook), same farm facts — so the image and copy tell one story.

## Iteration history

First version only. Ran it once in Meta AI.

## Failure modes the final version handles

- **Off-brand colours** — the hex codes come straight from the site's CSS: honey golds (`#FFD700`, `#F4A518`, `#FFBF00`) lead, the site's deep pink (`#C71585`) is only an accent, because a pink-led honey image would look like a beauty brand.
- **Garbled Thai text** — image models often mangle Thai script, so the prompt keeps the text short ("น้ำผึ้งแท้ 100%"), small, and in the top third where it's easy to crop or replace.
- **Cartoon look** — asks for "a sunlit photograph, not a slick advert", no cartoon bees, no oversaturated colours, because the brand is "trustworthy family farm", not luxury.
- **Wrong format** — 1200×628 wide for a Facebook feed post, not Instagram square.

## Outcome

In my words:

> "Both usable at first go then I made changes how I wanted it"

## Engineering on the output

What I changed about the AI's output before it shipped, and why.

**Accepted as-is:** the prompt went into Meta AI exactly as drafted.

**Reworked, and why:** the image Meta AI produced — "I made changes how I wanted it." Which changes isn't recorded; left at that on purpose.

**Roughly:** not tracked.

## Decisions

- **Gold-led palette with pink as accent**, not the site's pink-led palette — the site is a catalogue, the post is a product shot.
- **Longan blossoms in frame** — "longan" means nothing visually unless you show the tree.

## What I'd change next

- Try a version with no text in the image at all and put the Thai in the post copy instead — that sidesteps the Thai-script problem entirely.
- Record the changes made after the next run.

## A note on this file

Same as the text prompt — my words are the same two quotes; kept short rather than padded.

## Tags

`content` `image-generation` `brand-colours` `meta-ai`
