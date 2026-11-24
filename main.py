#!/usr/bin/env python3
"""Entry program for 'The Dog Ate My Homework: Funniest Excuse'.

The whole submission is one line in the dog's own voice: caught red-pawed
with the homework, the dog does not apologise — it reports a failed taste
test and claims it destroyed the evidence to save its human embarrassment.

The program writes that line to entry.txt inside the directory named by
MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is where
the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

TEXT = (
    "I didn't eat it. I ran a taste test, and your essay on the water "
    "cycle failed so very badly I had to destroy the evidence before it "
    "embarrassed us both in front of the whole class tomorrow morning."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200

def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("excuse must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
