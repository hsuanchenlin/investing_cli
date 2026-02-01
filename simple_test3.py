#!/usr/bin/env python3
"""Test reading multiple characters at once"""

import sys
import termios
import tty

print("Testing multi-character read...")
print("Press UP arrow key:")
print()

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setraw(fd)

    # Try reading 3 characters at once
    chars = sys.stdin.read(3)
    print(f"Read {len(chars)} characters: {repr(chars)}")

    for i, ch in enumerate(chars):
        print(f"  [{i}]: {repr(ch)} (hex: {ord(ch):02x})")

    if chars == '\x1b[A':
        print("\n✓✓✓ UP ARROW! ✓✓✓")
    elif chars == '\x1b[B':
        print("\n✓✓✓ DOWN ARROW! ✓✓✓")
    elif chars == '\x1b[C':
        print("\n✓✓✓ RIGHT ARROW! ✓✓✓")
    elif chars == '\x1b[D':
        print("\n✓✓✓ LEFT ARROW! ✓✓✓")
    else:
        print(f"\nGot: {repr(chars)}")

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print("\nDone!")
