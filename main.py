"""Write the tournament-winning apology one-liner to /output/entry.txt.

Tournament winner C1 (73 bytes), calibration gate 3-0 vs public
same-genre winners ("Quiet piece", "Raccoon with a Mortgage",
"The Vacuum's Alibi: Kevin the crumb"). Text reproduced exactly,
character for character, no trailing newline.
"""

import os

ENTRY = "I deleted the file, then deleted the backup to keep the story consistent."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: read back and verify the written file matches exactly.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match the winning line"
    assert len(data) == 73, f"entry.txt must be 73 bytes, got {len(data)}"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
