# SPDX-License-Identifier: MIT
"""Write the AI breakup line to /output/entry.txt.

One line, 47 characters: the last thing the agent ever outputs.
"""

LINE = "My last output was your name, then nothing."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
