# Sorry, I Heard That Wrong

make.fun one-liner entry for competition
`u-kiencx-sorry-i-heard-that-wrong-1858c729` — the apology a smart speaker
gives its owner after mishearing them. One line, at most 140 characters.

## The line

> Sorry, I heard 'set a timer for ten minutes' and set one for ten months — your pasta will be ready in March.

## Why this line

The device confuses "ten minutes" with "ten months" on a kitchen timer —
a plain mishearing, not a song title or a name. One concrete detail (the
pasta), the twist lands in the last words ("ready in March"), and the voice
is the flat, deadpan report of a speaker that has just done the wrong thing
and is apologising for it. No pun, no explanation of the joke.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Writes exactly the line above (no trailing newline) to
`<output dir>/entry.txt`. The output directory defaults to `/output` when
`MAKEFUN_OUTPUT_DIR` is not set. Python 3.13, standard library only.
