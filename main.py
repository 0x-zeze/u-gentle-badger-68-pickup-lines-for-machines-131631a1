#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, one AI agent to another, to /output/entry.txt.
Deterministic: no network, no randomness, no time, no dependencies.
"""

import os

# Chosen line: argmax/softmax — core LLM internals as flirtation.
# Fresh angle: the field is saturated with context-window / token /
# hallucination lines; argmax over a softmax is machine-native, lands on
# the first read, and the "rounds to zero" turn is the devotion.
LINE = "You're the argmax of my softmax — every other token's probability rounds to zero."


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
