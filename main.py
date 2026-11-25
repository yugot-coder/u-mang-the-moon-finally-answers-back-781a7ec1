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
    raises AssertionError with a clear message.
    """
    if isinstance(value, bytes):
        value = value.decode("utf-8")
    assert 1 <= len(value) <= MAX_CHARS, (
        f"entry.txt must be 1..{MAX_CHARS} characters, got {len(value)}"
    )
    assert value.strip(), "entry.txt must not be only whitespace"
    assert "\n" not in value and "\r" not in value, (
        "entry.txt must be a single line"
    )
    return value


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
    assert validate_entry(data) == TEXT
    # Digest verification: the written bytes must hash to the digest
    # measured from the verified run, proving no drift or stray bytes.
    digest = hashlib.sha256(data).hexdigest()
    assert digest == EXPECTED_SHA256, (
        f"entry.txt sha256 mismatch: got {digest}, "
        f"expected {EXPECTED_SHA256}"
    )
    print(TEXT)
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
