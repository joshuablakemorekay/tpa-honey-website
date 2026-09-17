# Social post copy — Longan Honey (Facebook, Thai/English)

> **Category:** content
> **Model used:** Claude Opus 5 drafted the prompt from the site's content; Meta AI ran it
> **Project area:** T.P.A. Honey Farm — social media marketing
> **Status:** production
> **Last updated:** 2026-09-17

## What this prompt does

Fills in a nine-part social-media-post template so Meta AI writes a bilingual (Thai first, English under) Facebook post promoting T.P.A. Honey Farm's Longan Honey — using only facts that are already on the live site.

## The prompt

```
Please draft a social media post based on the following information.

1. Purpose of the Post: Promote T.P.A. Honey Farm's signature Longan Honey and remind followers that every jar is 100% pure, raw honey straight from our own hives.

2. Target Audience: Health-conscious adults aged 25–55 in Thailand (and Thai-speaking expats), mostly women, who buy natural food and wellness products for their family, prefer buying direct from small local producers, and are active on Facebook and LINE.

3. Key Message: "Real honey from a real farm. T.P.A. Honey Farm in Lopburi has kept bees for generations — our Longan Honey is 100% pure, never blended, never heated, straight from hive to jar."

4. Tone and Style: Warm, honest and down-to-earth, like a family farmer talking to a neighbour. Simple words, no hype. Bilingual: write the post in Thai first, then a short English version underneath. Use the Thai brand name ฟาร์มผึ้งเทพภักดี alongside "T.P.A. Honey Farm".

5. Call to Action (CTA): "Message us on Facebook or call 086-315-1355 to order — we deliver nationwide."

6. Hashtags and Tags: #TPAHoneyFarm #ฟาร์มผึ้งเทพภักดี #น้ำผึ้งแท้100 #LonganHoney #น้ำผึ้งลำไย #ลพบุรี #RawHoney

7. Platform: Facebook

8. Length: 400–500 characters in total (Thai and English combined), plus hashtags.

9. Additional Notes: Mention that we also make bee pollen, royal jelly and propolis so people know it's a full bee farm, not just a honey seller. Include one or two bee/honey emojis but keep it tasteful. Don't make medical claims — "natural" and "pure" are fine, "cures" is not.
```

## Inputs

None at run time — the prompt is self-contained. The facts inside it (brand name, farm location, product, phone number, hashtags) were pulled from the live site's templates so nothing is invented. To reuse it for another product, change sections 1, 3 and 6.

## Expected output

One Facebook post: a Thai paragraph, then a shorter English paragraph, then the seven hashtags. Roughly 400–500 characters before the hashtags. Names the farm in both scripts, gives the phone number, mentions pollen / royal jelly / propolis in passing, and makes no health claims.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
