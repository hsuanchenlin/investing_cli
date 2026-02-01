#!/usr/bin/env python3
"""Debug version of the app to see what's happening"""

import sys
import os

# Use the installed version
sys.path.insert(0, os.path.expanduser('~/.local/share/investing-bbs/source'))

print("="*60)
print("DEBUG MODE - Checking imports...")
print("="*60)

# Check which keyboard module gets imported
try:
    from investing_bbs.keyboard_native import KeyboardInput as KBNative
    print("✓ keyboard_native imported")
    using_native = True
except Exception as e:
    print(f"✗ keyboard_native failed: {e}")
    using_native = False

try:
    from investing_bbs.keyboard import KeyboardInput as KBReadchar
    print("✓ keyboard (readchar) imported")
    using_readchar = True
except Exception as e:
    print(f"✗ keyboard (readchar) failed: {e}")
    using_readchar = False

# Now try the actual import from main
try:
    from investing_bbs.keyboard_native import KeyboardInput
    print("\n✓ Main import: Using keyboard_native")
    implementation = "native (termios)"
except ImportError:
    try:
        from investing_bbs.keyboard import KeyboardInput
        print("\n⚠ Main import: Fell back to keyboard (readchar)")
        implementation = "readchar"
    except Exception as e:
        print(f"\n✗ Both imports failed!")
        print(e)
        sys.exit(1)

print(f"\nUsing implementation: {implementation}")
print("="*60)
print()

# Now try to use menu_select
menu_items = [
    ("1", "Test One", "First test item"),
    ("2", "Test Two", "Second test item"),
    ("Q", "Quit", "Exit test"),
]

print("Calling menu_select with test items...")
print("Try using arrow keys to navigate")
print()

try:
    choice = KeyboardInput.menu_select(menu_items)
    print(f"\n\nYou selected: {choice}")
except Exception as e:
    print(f"\n\n✗ ERROR in menu_select:")
    print(e)
    import traceback
    traceback.print_exc()
