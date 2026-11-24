"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell.

Fully deterministic: fixed string, no time, no randomness, no network,
no file traversal. Python 3.13 standard library only.
"""

import os

SENTENCE = (
    "We bottle the silence of an anechoic chamber and sell it by the minute "
    "to open-plan offices, because the only thing burned-out workers will "
    "expense without asking is ten minutes of nothing."
)


def main() -> None:
    # The gate refuses any entry outside 1..200 characters; fail loudly
    # here instead of shipping an invalid sentence.
    assert 1 <= len(SENTENCE) <= 200, f"sentence is {len(SENTENCE)} chars"
    assert SENTENCE.strip() == SENTENCE
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
