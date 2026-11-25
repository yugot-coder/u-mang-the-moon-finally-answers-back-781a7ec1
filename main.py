"""The Moon Finally Answers Back.

Writes the Moon's one-line comeback to <MAKEFUN_OUTPUT_DIR>/entry.txt
(default /output/entry.txt). Single line, 1 to 240 characters, no
trailing newline.

The line:

    I don't grant wishes. I just reflect sunlight and watch you all
    make the same mistakes in better lighting.

Why this line (reasoning, kept here and in the README; the entry
itself is just the line):

* Funny first, no explaining: the joke is the premise itself -- the
  Moon is not a wish-granter, just a mirror -- and it lands in one
  read.
* Sounds like the Moon: "I just reflect sunlight" is literally what
  the Moon does; only the Moon could say it, so the voice is
  unmistakable.
* Twist in the tail: "in better lighting" turns a cosmic shrug into
  a punchline -- humanity's failures, now elegantly lit.
* Answers the brief directly: it replies to the wishes themselves,
  the core of the task, rather than to one narrow habit like howling.
* Hemat kata, membekas: 106 characters, three short beats, nothing
  wasted; the line is quotable the way a comeback should be.

Candidates weighed and set aside are listed in CANDIDATES.md.

Standard library only. Deterministic: no randomness, no network, no
clock.
"""

import hashlib
import os

TEXT = (
    "I don't grant wishes. I just reflect sunlight and watch you all "
    "make the same mistakes in better lighting."
)

MAX_CHARS = 240

# sha256 of the exact bytes main.py must write to entry.txt, measured
# from a verified run. The read-back step asserts the file's digest
# equals this value, so any drift in the written bytes fails loudly.
EXPECTED_SHA256 = (
    "23507c0e7ffc374030a26d38d6d5612a26702a70cd53ca3be8f1c1259e53313b"
)


def validate_entry(value) -> str:
    """Guard: value must be a single non-blank line of 1..240 chars.

    Accepts either the text string or the raw bytes read back from the
    entry file, so the same check covers the pre-write guard and the
    post-write read-back verification. Returns the text as a str, or
    raises ValueError with a clear message (ValueError, not assert,
    so the guard survives python -O).
    """
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    if not 1 <= len(value) <= MAX_CHARS:
        raise ValueError(
            f"entry.txt must be 1..{MAX_CHARS} characters, got {len(value)}"
        )
    if not value.strip():
        raise ValueError("entry.txt must not be only whitespace")
    if "\n" in value or "\r" in value:
        raise ValueError("entry.txt must be a single line")
    return value


def verify_written_bytes(data: bytes) -> str:
    """Byte-exact read-back verification: the bytes on disk must have
    the same length as the intended text's UTF-8 encoding, be equal
    to it, decode back to the text, and hash to EXPECTED_SHA256."""
    intended = TEXT.encode("utf-8")
    if len(data) != len(intended):
        raise ValueError("read-back byte length mismatch")
    if data != intended:
        raise ValueError("read-back bytes differ from the intended text")
    if validate_entry(data) != TEXT:
        raise ValueError("read-back text differs from the intended text")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(
            f"entry.txt sha256 mismatch: got {digest}, "
            f"expected {EXPECTED_SHA256}"
        )
    return digest


def main() -> None:
    # Pre-write guard: refuse to write anything outside the gate.
    validate_entry(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read-back validation: the gate is 1..240 characters, so the file
    # must hold exactly the text we intended to write.
    with open(path, "rb") as f:
        data = f.read()
    digest = verify_written_bytes(data)
    print(TEXT)
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
