"""
Keyboard input handling with arrow key support (readchar fallback)
NOTE: This is a fallback for systems where termios doesn't work.
The native implementation (keyboard_native.py) is preferred.
"""

import sys
from typing import Optional, List, Tuple

try:
    import readchar
    READCHAR_AVAILABLE = True
except ImportError:
    READCHAR_AVAILABLE = False
    # If readchar isn't available, this module will fail
    # The main.py should use keyboard_native instead


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
        try:
            key = readchar.readkey()
        except Exception as e:
            # Fallback to regular input on error
            return input()

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

        def clear_screen():
            """Clear the terminal screen"""
            os.system('clear' if os.name != 'nt' else 'cls')

        def draw_menu():
            """Draw the menu with current selection highlighted"""
            clear_screen()

            # Draw header (match the BBS style from main menu)
            print("╔" + "═" * 78 + "╗")
            print("║" + " " * 78 + "║")
            print("║" + " " * 30 + "◄ MAIN MENU ►" + " " * 35 + "║")
            print("║" + " " * 78 + "║")
            print("╚" + "═" * 78 + "╝")

            # Draw menu items
            print("\n┌────────────────────────────────────────────────────────────────────────────┐")

            for i, (key, title, desc) in enumerate(items):
                key_display = f"[{key}]"

                if i == current:
                    # Highlighted item with arrow
                    line = f"│ ▶ {key_display:<6} {title:<20} {desc:<39}    │"
                    print(f"\033[7m{line}\033[0m")  # Reverse video
                else:
                    line = f"│   {key_display:<6} {title:<20} {desc:<39}    │"
                    print(line)

            print("└────────────────────────────────────────────────────────────────────────────┘")
            print("\n[↑/↓] Navigate  [←] Back  [→/Enter/Number] Select  [Q] Quit")

        # Main loop
        while True:
            draw_menu()

            # Get key
            key = KeyboardInput.get_key()

            # Handle navigation
            if key == KeyboardInput.UP:
                current = (current - 1) % len(items)
            elif key == KeyboardInput.DOWN:
                current = (current + 1) % len(items)
            elif key == KeyboardInput.LEFT:
                # Left arrow = go back (return 'Q' to go to main menu)
                return 'Q'
            elif key == KeyboardInput.RIGHT or key == KeyboardInput.ENTER:
                # Right arrow or Enter = select current item
                return items[current][0]
            elif key.upper() == 'Q':
                return 'Q'
            elif len(key) == 1 and (key.isdigit() or key.isalpha()):
                # Check if key matches any menu item
                for item_key, _, _ in items:
                    if key.upper() == item_key.upper():
                        return item_key
            elif key == KeyboardInput.ESC:
                return None
