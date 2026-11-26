"""The Printer Finally Answers.

Writes the office printer's one-line comeback to /output/entry.txt.

The line is a fixed, deterministic string: no input, no randomness,
no network. The printer speaks in its own flat machine voice, with
the exact sheet it choked on, the exact thump count, and the exact
error code, all logged.
"""

import os

LINE = (
    "Error 0xE3: sheet 41,208 is lodged in my throat, "
    "and thump 14 just joined it in the log."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
