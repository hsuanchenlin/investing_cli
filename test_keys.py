#!/usr/bin/env python3
"""Diagnostic tool to test keyboard input"""

import sys
import os

# Add the package to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("Testing keyboard input detection...")
print("Press arrow keys, Enter, letters, etc.")
print("Press Ctrl+C to exit")
print("-" * 50)

try:
    # Test native implementation first
    from investing_bbs.keyboard_native import KeyboardInput
    print("Using NATIVE keyboard implementation (termios)")
    print()

    while True:
        key = KeyboardInput.get_key()

        # Show the raw key value
        print(f"Raw key: {repr(key):<20} | Type: {type(key).__name__}")

        # Show what it matches
        if key == KeyboardInput.UP:
            print("  ✓ Matched: UP")
        elif key == KeyboardInput.DOWN:
            print("  ✓ Matched: DOWN")
        elif key == KeyboardInput.LEFT:
            print("  ✓ Matched: LEFT")
        elif key == KeyboardInput.RIGHT:
            print("  ✓ Matched: RIGHT")
        elif key == KeyboardInput.ENTER:
            print("  ✓ Matched: ENTER")
        elif key == KeyboardInput.ESC:
            print("  ✓ Matched: ESC")
            break
        else:
            print(f"  → No match, checking KeyboardInput constants:")
            print(f"     UP={repr(KeyboardInput.UP)}")
            print(f"     DOWN={repr(KeyboardInput.DOWN)}")
            print(f"     LEFT={repr(KeyboardInput.LEFT)}")
            print(f"     RIGHT={repr(KeyboardInput.RIGHT)}")

        print()

except KeyboardInterrupt:
    print("\n\nExiting...")
except Exception as e:
    print(f"\nError: {e}")
    import traceback
    traceback.print_exc()
