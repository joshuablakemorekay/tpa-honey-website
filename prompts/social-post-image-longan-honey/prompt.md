# Social post image — Longan Honey (Facebook, 1200×628)

> **Category:** content
> **Model used:** Claude Opus 5 drafted the prompt from the site's content; Meta AI generated the image
> **Project area:** T.P.A. Honey Farm — social media marketing
> **Status:** production
> **Last updated:** 2026-09-17

## What this prompt does

Fills in a ten-part image template so Meta AI generates the picture for the Longan Honey Facebook post — a realistic product shot in the site's own colours, with a short Thai caption kept small enough to survive image-model text rendering.

## The prompt

```
Please generate images for a social media post based on the following information.

1. Purpose of the Image: Promote T.P.A. Honey Farm's Longan Honey and show that it comes straight from a real family bee farm in Lopburi, Thailand.

2. Target Audience: Health-conscious Thai adults aged 25–55 who buy natural food for their family and like buying direct from small local farms.

3. Key Message or Theme: "100% pure honey, straight from hive to jar."

4. Visual Style and Tone: Warm, natural and honest — like a sunlit photograph, not a slick advert. Golden-hour light, soft focus background, real-farm feel.

5. Elements to Include: A glass jar of golden longan honey in the foreground with a wooden honey dipper drizzling honey; a few longan blossoms or a longan branch beside it; blurred beehives and a Thai orchard in the background; one or two honeybees in flight. Leave a clean area at the top for the logo.

6. Color Scheme: Honey golds (#FFD700, #F4A518, #FFBF00) as the main colours, with the brand's deep pink (#C71585) used as a small accent for the text or a ribbon on the jar, and soft cream (#FFF8E7) for the background highlights.

7. Text and Typography: Include the text "น้ำผึ้งแท้ 100%" in a clean, rounded Thai font, with "T.P.A. Honey Farm" underneath in a simple sans-serif. Keep the text small and in the top third of the image.

8. Image Format and Size: Wide 1200x628 for a Facebook feed post.

9. Platform: Facebook

10. Additional Notes: The honey should look thick and glossy. Keep it realistic — no cartoon bees, no oversaturated colours. The overall feeling should be "trustworthy family farm", not "luxury brand".
```

## Inputs

None at run time. The hex codes are the site's own CSS colours (`#C71585` is the site's main pink; the golds appear in its gradients), so the image matches the website it links to.

## Expected output

A 1200×628 photographic-style image: honey jar and dipper in front, longan blossom beside it, soft orchard and hives behind, gold-led palette with a small pink accent, and short Thai text in the top third.

Because an image can't be checked by a script, the rubric for this prompt scores a **reviewer's checklist** — a small JSON object you fill in after looking at the image — rather than the image itself. See `rubric.yaml` for the keys.

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
