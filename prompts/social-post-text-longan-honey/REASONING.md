# Reasoning: Social post copy — Longan Honey

This document captures the thinking behind the prompt. It exists so a reader can understand not just *what* the prompt is, but *why* it ended up this way.

## Goal

This was a coursework activity from my social-media-marketing course: fill in a nine-part template so a GenAI tool (Meta AI) writes a social post. Rather than invent a brand, I used T.P.A. Honey Farm — the real client site in this repo. My brief to Claude was one line:

> "Do it for TPA Honey"

Claude filled the template from facts already in the site — the Thai brand name ฟาร์มผึ้งเทพภักดี, the farm in Chai Badan, Lopburi (the office is in Bangkok), the product list, the phone number — so nothing in the prompt is made up.

## Iteration history

First version only. I ran it in Meta AI once and didn't need to change the prompt.

## Failure modes the final version handles

- **Fake brand facts** — every detail is pulled from the live site, not guessed.
- **Medical claims** — the prompt says "natural" and "pure" are fine, "cures" is not, because Thai advertising rules are strict on health claims.
- **Wrong language** — asks for Thai first, English underneath, because the customers are Thai.
- **Hype** — asks for "a family farmer talking to a neighbour", no marketing-speak.

## Outcome

In my words:

> "Both usable at first go then I made changes how I wanted it"

## Engineering on the output

What I changed about the AI's output before it shipped, and why.

**Accepted as-is:** the prompt itself went into Meta AI exactly as Claude drafted it.

**Reworked, and why:** the post Meta AI wrote — "I made changes how I wanted it." Which changes isn't recorded; deliberately left at that.

**Roughly:** not tracked.

## Decisions

- **Facebook over Instagram** — Thai farm customers are mostly on Facebook.
- **Longan Honey as the hero product** — it's the first product listed on the site.

## What I'd change next

- Log what actually got changed after the next run, so the delta is a receipt rather than a sentence.
- Consider a LINE contact — most Thai customers message on LINE, not Facebook.

## A note on this file

My own words in here are three short quotes. The whole session was driven by one line from me, so the file is kept short rather than padded.

## Tags

`content` `social-media` `bilingual-thai` `meta-ai`
