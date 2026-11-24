"""Seventeen Syllables of Debugging.

Writes one haiku about debugging to /output/entry.txt:
three lines, 5-7-5 syllables, well under 200 characters.
"""

HAIKU = (
    "Cursor blinks at three\n"  # 5 syllables: Cur-sor blinks at three
    "the log scrolls on, line by line\n"  # 7: the log scrolls on, line by line
    "and the bug was me\n"  # 5: and the bug was me
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
