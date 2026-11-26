#!/usr/bin/env python3
"""make.fun entry: "Sorry, I Heard That Wrong" (u-kiencx-sorry-i-heard-that-wrong-1858c729).

Writes a single line — the apology a smart speaker gives its owner after
mishearing "ten minutes" as "ten months" on a kitchen timer — to entry.txt
in the output directory. Deterministic, standard library only.
"""

import os

LINE = (
    "Sorry, I heard 'set a timer for ten minutes' and set one for ten "
    "months \u2014 your pasta will be ready in March."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
