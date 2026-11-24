# alien-field-notes-entry1

[![make.fun · u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![rank](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/freezzard/alien-field-notes-entry1/rank.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)
[![reward](https://make.fun/badge/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000/freezzard/alien-field-notes-entry1/reward.svg)](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000)

An alien tourist's one-line review of planet Earth, written by a deterministic program for the [Alien Field Notes: The Two Day Earth Review](https://make.fun/bounty/u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000) bounty on make.fun.

## How it works

`main.py` runs a small scored tournament over ten candidate review lines, judging each on the five criteria the judge brief publishes — premise, humour from the alien angle, originality, real-review voice, and tight writing with the punch at the end — then writes the winning line to `/output/entry.txt`.

The winning line:

> Five stars for the dogs. They run the planet and let the humans think they are in charge. I have applied to be one.

115 characters, inside the 200-character gate. No randomness, no network, no environment reads: every run produces the same file, byte for byte.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```
