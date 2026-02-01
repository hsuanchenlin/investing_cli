#!/usr/bin/env python3
"""Simplest possible test"""

print("Step 1: Testing sys.stdin.isatty()")
import sys
print(f"  Result: {sys.stdin.isatty()}")
print()

print("Step 2: Testing termios import")
try:
    import termios
    import tty
    print("  ✓ termios and tty imported")
except Exception as e:
    print(f"  ✗ Failed: {e}")
    sys.exit(1)
print()

print("Step 3: Testing terminal control")
try:
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    print(f"  ✓ Got terminal settings: fd={fd}")
    termios.tcsetattr(fd, termios.TCSADRAIN, old)
    print("  ✓ Can set terminal settings")
except Exception as e:
    print(f"  ✗ Failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
print()

print("Step 4: Testing raw mode read")
print("  Press UP arrow key:")

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

try:
    tty.setraw(fd)
    import select

    # Read with timeout
    if select.select([sys.stdin], [], [], 5)[0]:
        ch1 = sys.stdin.read(1)
        print(f"    Got char 1: {repr(ch1)}")

        if ch1 == '\x1b':
            if select.select([sys.stdin], [], [], 0.1)[0]:
                ch2 = sys.stdin.read(1)
                print(f"    Got char 2: {repr(ch2)}")

                if select.select([sys.stdin], [], [], 0.1)[0]:
                    ch3 = sys.stdin.read(1)
                    print(f"    Got char 3: {repr(ch3)}")

                    if ch3 == 'A':
                        print("\n  ✓✓✓ UP ARROW DETECTED! ✓✓✓")
                    elif ch3 == 'B':
                        print("\n  ✓✓✓ DOWN ARROW DETECTED! ✓✓✓")
    else:
        print("    (timeout - no input)")

finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    print()
    print("Done!")
