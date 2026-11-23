#!/usr/bin/env python3
"""One-star review of something essential: sleep.

Writes a single-line deadpan one-star review (160 characters or fewer)
to /output/entry.txt, as the competition harness expects.
"""

import os

REVIEW = (
    "Sleep: one star. Never shows up when I am in bed waiting for it, "
    "arrives uninvited in meetings, and charges me eight hours a night "
    "for the privilege."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
