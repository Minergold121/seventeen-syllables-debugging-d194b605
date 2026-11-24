import os

ENTRY = "git blame points at me\nthe commit is mine, from June\npast me wrote this bug\n"
OUTPUT_PATH = "/output/entry.txt"

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as entry_file:
    entry_file.write(ENTRY)
