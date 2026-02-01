#!/usr/bin/env python3
"""Test with different timeout"""

import sys
import termios
import tty
import select

print("Testing with longer timeout...")
print("Press UP arrow key:")
print()

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setraw(fd)

    # Read first character
    if select.select([sys.stdin], [], [], 5)[0]:
        ch1 = sys.stdin.read(1)
        print(f"Char 1: {repr(ch1)} - ", end='', flush=True)

        if ch1 == '\x1b':
            print("(ESC detected, waiting for more...)")

            # Try longer timeout
            for timeout in [0.01, 0.05, 0.1, 0.5, 1.0]:
                print(f"  Trying {timeout}s timeout...", end='', flush=True)
                if select.select([sys.stdin], [], [], timeout)[0]:
                    ch2 = sys.stdin.read(1)
                    print(f" got {repr(ch2)}")

                    if ch2 == '[':
                        print(f"  Bracket detected, reading next...")
                        if select.select([sys.stdin], [], [], timeout)[0]:
                            ch3 = sys.stdin.read(1)
                            print(f"  Char 3: {repr(ch3)}")

                            if ch3 == 'A':
                                print("\n✓✓✓ UP ARROW! ✓✓✓")
                            elif ch3 == 'B':
                                print("\n✓✓✓ DOWN ARROW! ✓✓✓")
                        else:
                            print(f"  No char 3 after {timeout}s")
                    break
                else:
                    print(" (no data)")
            else:
                print("\n  ✗ No more characters received")

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print("\nDone!")
