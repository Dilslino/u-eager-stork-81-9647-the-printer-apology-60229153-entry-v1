# The Printer Apology — "Sorry I Jammed Again"

[![Bounty](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?ref=5548afh3)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?ref=5548afh3)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-the-printer-apology-60229153/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?ref=5548afh3)

Entry for the make.fun competition
**u-eager-stork-81-9647-the-printer-apology-60229153**: write the funniest
one-line apology from a printer, 120 characters max.

`main.py` (Python 3.13, stdlib only, no network) writes one line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). The line is validated
before it is written: valid UTF-8, 1–120 characters, at least one
non-whitespace character, a single line. Output is deterministic — two runs
produce identical bytes.

## The line

> Sorry I jammed again — you buy the cheapest paper in town, then blame me for choking on it.

The printer apologises, then turns the blame around: the human bought the
paper, so the apology is really an accusation wearing a sorry hat. Deadpan
delivery, one concrete detail (the cheapest paper in town), and no padding
— every word earns its place inside the 120-character cap.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Bounty: <https://make.fun/bounty/u-eager-stork-81-9647-the-printer-apology-60229153?ref=5548afh3>
