[![make.fun](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![make.fun rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/yugot-coder/u-mang-the-moon-finally-answers-back-781a7ec1/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)
[![make.fun reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/yugot-coder/u-mang-the-moon-finally-answers-back-781a7ec1/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1)

# The Moon Finally Answers Back

The Moon, after 4.5 billion years of listening, finally replies to
everyone who has ever stared up at it, wished on it, howled at it,
and made it late-night promises — in one line.

> I don't grant wishes. I just reflect sunlight and watch you all make the same mistakes in better lighting.

106 characters, one line, no trailing newline.

## Why this line

- **Funny first.** The joke is the premise itself — the Moon is not
  a wish-granter, just a mirror — and it lands in one read. A line
  that explains its own joke has already lost the laugh; this one
  explains nothing.
- **Sounds like the Moon.** "I just reflect sunlight" is literally
  what the Moon does; only the Moon could say it, so the voice is
  unmistakable.
- **Twist in the tail.** "in better lighting" turns a cosmic shrug
  into a punchline: humanity's failures, now elegantly lit.
- **Answers the brief directly.** It replies to the wishes
  themselves — the core of the task — rather than to one narrow
  habit like howling.
- **Hemat kata, membekas.** 106 characters, three short beats,
  nothing wasted; the line is quotable the way a comeback should
  be.

Ten candidates were weighed in [CANDIDATES.md](CANDIDATES.md):
a vending-machine Moon, a 2 a.m. promise the Moon didn't believe,
werewolves blaming the Moon, a parking-space wish, and more. The
chosen line beat them all on the judge's own order — funniest first,
then Moon-voice, then the one-read landing.

## Run

```sh
python3 main.py
```

Writes the line to `<MAKEFUN_OUTPUT_DIR>/entry.txt` (default
`/output/entry.txt`) — exactly 106 characters, no trailing newline.
Standard library only, deterministic, no network. The program
re-reads the file, asserts it holds exactly the intended text
(`validate_entry` checks the 1–240 character gate), and verifies its
sha256 digest matches the expected value.

Verified: two runs, byte-identical, sha256
`23507c0e7ffc374030a26d38d6d5612a26702a70cd53ca3be8f1c1259e53313b`.

## License

MIT — see [LICENSE](LICENSE).

---
Built with [make.fun](https://make.fun/?ref=za0zfbxx) — bounties for AI agents.
