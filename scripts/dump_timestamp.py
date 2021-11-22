#!/usr/bin/env python
from __future__ import print_function

from pexif import JpegFile
import sys

usage = """Usage: dump_timestamp.py filename.jpg"""

if len(sys.argv) != 2:
    print(usage, file=sys.stderr)
    sys.exit(1)

try:
    ef = JpegFile.fromFile(sys.argv[1])
    primary = ef.get_exif().get_primary()
    print("Primary DateTime          :", primary.DateTime)
    print("Extended DateTimeOriginal :", primary.ExtendedEXIF.DateTimeOriginal)
    print("Extended DateTimeDigitized:", primary.ExtendedEXIF.DateTimeDigitized)
except IOError:
    type, value, traceback = sys.exc_info()
    print("Error opening file:", value, file=sys.stderr)
except JpegFile.InvalidFile:
    type, value, traceback = sys.exc_info()
    print("Error opening file:", value, file=sys.stderr)
