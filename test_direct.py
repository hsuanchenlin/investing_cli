#!/usr/bin/env python3
"""Direct test of keyboard input"""

import sys
import os

# Test the native implementation directly
sys.path.insert(0, os.path.expanduser('~/.local/share/investing-bbs/source'))

print("Testing native keyboard directly...")
print()

try:
    from investing_bbs.keyboard_native import KeyboardInput
    print("✓ Imported KeyboardInput from keyboard_native")
    print()
    print("Press an arrow key (will read one key):")

    key = KeyboardInput.get_key()

    print(f"\nReceived key: {repr(key)}")
    print(f"Type: {type(key)}")

    if key == KeyboardInput.UP:
        print("✓ Matched UP!")
    elif key == KeyboardInput.DOWN:
        print("✓ Matched DOWN!")
    elif key == KeyboardInput.LEFT:
        print("✓ Matched LEFT!")
    elif key == KeyboardInput.RIGHT:
        print("✓ Matched RIGHT!")
    else:
        print(f"✗ No match. Key constants:")
        print(f"  UP = {repr(KeyboardInput.UP)}")
        print(f"  DOWN = {repr(KeyboardInput.DOWN)}")
        print(f"  LEFT = {repr(KeyboardInput.LEFT)}")
        print(f"  RIGHT = {repr(KeyboardInput.RIGHT)}")

except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
