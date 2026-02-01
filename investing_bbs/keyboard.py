"""
Keyboard input handling with arrow key support
"""

import sys
import readchar
from typing import Optional, List, Tuple


class KeyboardInput:
    """Handle keyboard input with special key support"""

    # Key constants
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    ENTER = 'enter'
    ESC = 'esc'

    @staticmethod
    def get_key() -> str:
        """Get a single keypress, handling special keys

        Returns:
            String representing the key pressed
        """
        key = readchar.readkey()

        # Map readchar keys to our constants
        key_map = {
            readchar.key.UP: KeyboardInput.UP,
            readchar.key.DOWN: KeyboardInput.DOWN,
            readchar.key.LEFT: KeyboardInput.LEFT,
            readchar.key.RIGHT: KeyboardInput.RIGHT,
            readchar.key.ENTER: KeyboardInput.ENTER,
            readchar.key.CR: KeyboardInput.ENTER,
            readchar.key.LF: KeyboardInput.ENTER,
            readchar.key.ESC: KeyboardInput.ESC,
        }

        return key_map.get(key, key)

    @staticmethod
    def get_input(prompt: str = "") -> str:
        """Get a line of input (fallback to regular input for text entry)

        Args:
            prompt: Prompt to display

        Returns:
            User input string
        """
        if prompt:
            print(prompt, end='', flush=True)
        return input()

    @staticmethod
    def menu_select(items: List[Tuple[str, str, str]],
                   current: int = 0) -> Optional[str]:
        """Interactive menu selection with arrow keys

        Args:
            items: List of (key, title, description) tuples
            current: Currently selected index

        Returns:
            The key of selected item, or None if cancelled
        """
        import os
        first_draw = True

        while True:
            # Clear screen and redraw (simpler and more reliable than cursor positioning)
            if not first_draw:
                # Move cursor up and clear
                lines_to_clear = len(items) + 4  # menu items + borders + help text
                print(f'\033[{lines_to_clear}A', end='')  # Move cursor up
                print('\033[J', end='')  # Clear from cursor to end of screen
            first_draw = False

            # Draw menu with highlight
            print("\n┌────────────────────────────────────────────────────────────────────────────┐")

            for i, (key, title, desc) in enumerate(items):
                key_display = f"[{key}]"

                if i == current:
                    # Highlighted item
                    line = f"│ ▶{key_display:<6} {title:<20} {desc:<40}     │"
                    print(f"\033[7m{line}\033[0m")  # Reverse video
                else:
                    line = f"│  {key_display:<6} {title:<20} {desc:<40}     │"
                    print(line)

            print("└────────────────────────────────────────────────────────────────────────────┘")
            print("\n[↑/↓] Navigate  [Enter/Number] Select  [Q] Quit", end='', flush=True)

            # Get key
            key = KeyboardInput.get_key()

            # Ignore left/right arrow keys
            if key == KeyboardInput.LEFT or key == KeyboardInput.RIGHT:
                continue
            elif key == KeyboardInput.UP:
                current = (current - 1) % len(items)
            elif key == KeyboardInput.DOWN:
                current = (current + 1) % len(items)
            elif key == KeyboardInput.ENTER:
                return items[current][0]
            elif key.upper() == 'Q':
                return 'Q'
            elif key.isdigit() or key.isalpha():
                # Check if key matches any menu item
                for item_key, _, _ in items:
                    if key.upper() == item_key.upper():
                        return item_key
            elif key == KeyboardInput.ESC:
                return None
