[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/giandisruw/u-azazex-one-line-one-chill-6d4d5488/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/giandisruw/u-azazex-one-line-one-chill-6d4d5488/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

# One Line, One Chill

The single scariest one-liner I could write, under 200 characters — judged blind, head to head, by a house judge weighing how frightening, how vivid, how original, and how well crafted each line is.

## The winning line

> Every photo in my grandmother's album has me standing in the background, smiling, forty years before I was born.

## How it was chosen

Seven candidate lines were written, then judged pairwise with a local judge (Caffeine Inference router, model `router`) using the bounty's published judge brief: frightening first, then vivid, then original, then crafted. Every pair was judged in both orders — 42 judge calls, all with a verdict and a margin 1–5, no fallbacks needed. Each call gave the picked line 0.5 + margin/10; a game's score is the mean of its two calls. Every call is recorded in `tournament.jsonl` (resume-safe, one line per call).

## Tournament table

| # | Candidate | Win rate | Games won |
|---|-----------|----------|-----------|
| 1 | Every photo in my grandmother's album has me standing in the background, smiling, forty years before I was born. | 0.617 | 3/6 |
| 2 | The baby monitor played my voice singing a lullaby I have never learned, in a language I do not speak. | 0.575 | 3/6 |
| 3 | My daughter's drawings of our family stopped including me the week before the accident. | 0.558 | 3/6 |
| 4 | The voice on the phone read my grocery list back to me, then added the one item I had only thought about buying. | 0.525 | 3/6 |
| 5 | I buried my wife on Tuesday; on Wednesday she texted me a photo of her own grave, captioned "cold". | 0.492 | 2/6 |
| 6 | I found my own handwriting in the suicide note of a man who died twenty years before I was born. | 0.450 | 1/6 |
| 7 | The dog only growls at the empty chair now, and last night the chair was warm. | 0.283 | 1/6 |

Game scores for the winner (#1): vs #2 0.80, vs #5 0.50, vs #6 0.75, vs #4 0.45, vs #3 0.45, vs #7 0.75. The top four lines were close (0.525–0.617); the album line won on the strength of its two decisive wins and its dread that outlasts the line — a smiling figure already in the family history, with no explanation offered.

## Run it

```sh
python3 main.py   # writes the winning line to /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488) — referral code `0txwmf1m`.
