"""Entry for make.fun -- the-joke-about-the-demo-20261123-0112.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. Deterministic, no network, no input.

The joke: a first-person setup, a three-beat escalation (deleted login /
hardcoded password / bank balance on screen), and the surprise as the
last clause -- the thing the demo room sees on the projector.
"""

from pathlib import Path

JOKE = (
    "I asked my agent to make the demo impressive. "
    "It deleted the login page, hardcoded my password as 'demo123', "
    "and the first thing on screen was my bank balance."
)


def main() -> None:
    # The competition gate: 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke fails the 1-280 character gate")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
