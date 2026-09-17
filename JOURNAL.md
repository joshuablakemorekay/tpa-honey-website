# Development Journal — T.P.A. Honey Farm Website
A chronological log of key developments, decisions and learnings throughout this project.

---
## 2026-09-17 — Two GenAI marketing prompts, archived with a receipt

**Type:** Learning / Milestone

**TL;DR:** Used the real T.P.A. Honey site as the brand for a course activity on GenAI social posts, then archived both prompts with rubrics and CI instead of leaving them in a chat window.

**What I built or did**
A text prompt and an image prompt for a Longan Honey Facebook post, filled in from the course template. My brief was one line — "Do it for TPA Honey" — and Claude pulled every fact (Thai brand name, Lopburi farm, phone number, hex colours) from this repo's templates rather than inventing them. Both ran in Meta AI. The result: "Both usable at first go then I made changes how I wanted it."

**Why I did it this way**
A made-up brand teaches nothing. Using the real client site meant real constraints: Thai first, no medical claims, gold-led not pink-led.

**How we did it**
Read the site for facts → drafted both prompts → ran them in Meta AI → archived them under `prompts/` with reasoning, executable rubrics, fixtures and a GitHub Actions eval that passes at 100%.

**What I learned**
An image can't be scored by a script, so the image rubric scores a reviewer's checklist instead — writing the checklist down is what makes the review repeatable.

**Engineering Contribution**
- *Decisions made:* Facebook over Instagram (Thai farm customers are on Facebook); Longan Honey as hero (first on the site); pink as accent only, not lead (a pink honey shot reads as a beauty brand). See `prompts/*/REASONING.md`.
- *Improvements made to generated code:* none — no code changed this session. The rubric's first draft failed YAML parsing and used a builtin the runner doesn't expose; both fixed by running the runner, not by guessing.
- *Roughly how much was accepted as-is vs engineered on:* prompts went in exactly as drafted; Meta AI's outputs were changed — "Just say I made changes how I wanted it." — not tracked.

---
