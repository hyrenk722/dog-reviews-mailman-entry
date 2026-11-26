"""Entry for make.fun — The Dog Reviews the Mailman.

Slug: u-motasimfuad-the-dog-reviews-the-mailman-87608f85

The program writes one funny one-line review, as told by the dog, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The text must be
UTF-8, 1-200 characters, and not only whitespace.
"""

import os
import sys

ENTRY = (
    "He comes every day at the same time, rings once, and runs \u2014 "
    "I have trained him perfectly and he still thinks it is his job."
)


def check_gate(text):
    """Return True when the text passes the competition gate."""
    if not isinstance(text, str):
        return False
    if text.strip() == "":
        return False
    if not 1 <= len(text) <= 200:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not check_gate(ENTRY):
        print("gate failed", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    with open(path, "rb") as fh:
        written = fh.read()
    if written != ENTRY.encode("utf-8"):
        print("verify failed: bytes on disk differ", file=sys.stderr)
        return 1
    print("wrote", path, len(ENTRY), "chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
