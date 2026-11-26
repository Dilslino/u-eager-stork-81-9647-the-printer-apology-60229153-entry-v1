"""Write one one-line apology from a printer to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. No network. Deterministic: the same bytes every run.

The line: the printer apologises for jamming, then turns the blame around
on the cheap paper it is fed. Deadpan, specific, one sentence, no padding.
The joke lands on the reversal: the machine is sorry, but the human bought
the paper, so the apology is really an accusation wearing a sorry hat.
"""

import os
import sys

LINE = (
    "Sorry I jammed again \u2014 you buy the cheapest paper in town, "
    "then blame me for choking on it."
)

MAX_CHARS = 120


def checked_line_bytes() -> bytes:
    """Encode the line and enforce the competition gate before writing.

    The entry must be valid UTF-8, hold 1 to 120 Unicode code points,
    contain at least one non-whitespace character, and be a single line.
    Anything outside the gate is a hard failure, never a silent bad file.
    """
    if not any(char for char in LINE if not char.isspace()):
        print("error: line is only whitespace", file=sys.stderr)
        sys.exit(1)
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(LINE) > MAX_CHARS:
        print(
            f"error: entry is {len(LINE)} chars, over the {MAX_CHARS} cap",
            file=sys.stderr,
        )
        sys.exit(1)
    try:
        return LINE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: entry is not valid UTF-8: {exc}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    data = checked_line_bytes()
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(data)
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
