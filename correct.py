#!/usr/bin/python3

import sys
import os

if len(sys.argv) < 3:
  print("Parameters missing!")
  print("Example:  -->  python correct.py prefix file_1.ext file_2.ext")
  print("If you use \\ as prefix, please write \\\\ instead")
  sys.exit(0)

PREFIX = sys.argv[1]

replacements = {
    "c": "ç",
    "C": "Ç",
    "s": "ş",
    "S": "Ş",
    "g": "ğ",
    "G": "Ğ",
    "i": "ı"
}

for i in range(2, len(sys.argv)):
  filename, ext = os.path.splitext(sys.argv[i])

  try:
    with open(f"{filename}{ext}", "r+") as f:
      data = f.read()

      for r in replacements:
        data = data.replace(f"{PREFIX}{r}", replacements[r])

      with open(f"{filename}_corrected{ext}", "w+") as c:
        c.write(data)

  except FileNotFoundError:
    print(f"Skipping {filename}, since it not exists")
  except UnicodeDecodeError:
    print("This file format is not supported")
    sys.exit(1)
