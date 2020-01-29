#!/usr/bin/env python3

import sys
from pathlib import Path

import pyperclip

# print(sys.argv)

pathfile = Path(sys.argv[-1])

if not pathfile.exists():
    print(f"No such file {pathfile}")
    sys.exit(1)

with open(pathfile, "r") as file:
    file.readline()
    text = file.read().strip()

text = text.replace("\n\n", "[end paragraph]")
text = text.replace("\n", " ")
text = text.replace("[end paragraph]", "\n\n").strip()
number_of_words = len(text.split())

pyperclip.copy(text)
print(f"text copied to the clipboard (approximately {number_of_words} words)")
