"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
$MAKEFUN_OUTPUT_DIR/entry.txt (the harness's /output/entry.txt).
"""

import os

FORTUNE = "Your future self is already debugging the shortcut you are about to take."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
