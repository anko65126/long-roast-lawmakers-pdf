"""Entry point for The Long Roast bounty.

Writes one satirical sentence to /output/entry.txt: lawmakers who
would regulate AI, crypto or the internet, but cannot convert a file
to PDF. The sentence is at most 320 characters, deterministic, and
needs no network access. The turn undercuts the committee's authority
with the one file it cannot convert.
"""
from pathlib import Path

ROAST = (
    "After three hearings demanding AI explain itself in plain "
    "language, the committee asked an intern to convert the bill to "
    "PDF, and the intern is still waiting, because the file is a "
    "screenshot of a Word document taped to a scanner."
)

TARGET = Path("/output/entry.txt")


def main():
    text = ROAST.strip()
    assert 1 <= len(text) <= 320, f"roast is {len(text)} characters"
    assert text.count(".") == 1, "roast must be exactly one sentence"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
