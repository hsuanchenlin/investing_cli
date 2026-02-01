"""
Native keyboard input handling using termios (more reliable than readchar)
"""

import sys
import tty
import termios
from typing import Optional, List, Tuple


class KeyboardInput:
    """Handle keyboard input with special key support using native termios"""

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
        import select

        # Check if stdin is a TTY
        if not sys.stdin.isatty():
            # Fallback to regular input if not a TTY
            return input()

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)

            # Read first character
            ch = sys.stdin.read(1)

            # Handle escape sequences (arrow keys, function keys, etc.)
            if ch == '\x1b':  # ESC
                # Use select to check if more data is available (with small timeout)
                # This distinguishes between ESC key and arrow keys
                if select.select([sys.stdin], [], [], 0.1)[0]:
                    ch2 = sys.stdin.read(1)
                    if ch2 == '[':
                        # Read the direction character
                        if select.select([sys.stdin], [], [], 0.1)[0]:
                            ch3 = sys.stdin.read(1)
                            # Arrow keys
                            if ch3 == 'A':
                                return KeyboardInput.UP
                            elif ch3 == 'B':
                                return KeyboardInput.DOWN
                            elif ch3 == 'C':
                                return KeyboardInput.RIGHT
                            elif ch3 == 'D':
                                return KeyboardInput.LEFT
                            # Handle other sequences if needed
                            return '\x1b[' + ch3
                        else:
                            return '\x1b['
                    else:
                        # ESC followed by something else
                        return KeyboardInput.ESC
                else:
                    # Just ESC key by itself
                    return KeyboardInput.ESC

            # Handle special characters
            if ch == '\r' or ch == '\n':
                return KeyboardInput.ENTER
            elif ch == '\x03':  # Ctrl+C
                raise KeyboardInterrupt
            elif ch == '\x04':  # Ctrl+D
                return KeyboardInput.ESC

            return ch

        except Exception as e:
            # On any error, restore terminal and re-raise
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            raise
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

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
