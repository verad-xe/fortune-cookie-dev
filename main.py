"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (the harness's /output/entry.txt).
"""

import os

FORTUNE = "Your future self is already debugging the shortcut you are about to take."

# Gate the harness enforces on /output/entry.txt: one line, 1-120 UTF-8
# characters. The fortune is a single sentence with no trailing newline,
# so it passes the gate as written; assert it here so a future edit that
# breaks the gate fails loudly in local verification instead of at submit.
MAX_CHARS = 120


def check_gate(text: str) -> None:
    chars = len(text.encode("utf-8"))
    assert 1 <= chars <= MAX_CHARS, f"entry is {chars} UTF-8 chars, gate is 1-{MAX_CHARS}"
    assert text == text.strip() and "\n" not in text, "entry must be a single non-blank line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    check_gate(FORTUNE)
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Confirm what landed on disk is exactly the gated text, so a
    # filesystem or encoding surprise shows up here, not at submit.
    with open(path, encoding="utf-8") as f:
        check_gate(f.read())


if __name__ == "__main__":
    main()
