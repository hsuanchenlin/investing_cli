#!/usr/bin/env python3
"""
Investing.com BBS-style CLI
A retro BBS interface for browsing financial markets data.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.layout import Layout
from rich.live import Live
from rich.box import DOUBLE, ROUNDED, HEAVY
from rich.align import Align
from rich import box
import argparse
from datetime import datetime

from .api import InvestingAPI
from .ui import BBSInterface

# Use native keyboard implementation (more reliable than readchar)
try:
    from .keyboard_native import KeyboardInput
except ImportError:
    # Fallback to readchar version if termios not available (Windows)
    from .keyboard import KeyboardInput

console = Console()

class InvestingBBS:
    """Main BBS-style CLI application for investing.com"""
    
    def __init__(self):
        self.api = InvestingAPI()
        self.ui = BBSInterface(console)
        self.running = True
        self.current_menu = "main"
        self.user = "Guest"
        
    def run(self):
        """Main entry point"""
        self.ui.clear_screen()
        self.show_welcome()
        
        while self.running:
            if self.current_menu == "main":
                self.main_menu()
            elif self.current_menu == "markets":
                self.markets_menu()
            elif self.current_menu == "crypto":
                self.crypto_menu()
            elif self.current_menu == "forex":
                self.forex_menu()
            elif self.current_menu == "commodities":
                self.commodities_menu()
            elif self.current_menu == "indices":
                self.indices_menu()
            elif self.current_menu == "stocks":
                self.stocks_menu()
                
    def show_welcome(self):
        """Display BBS welcome screen"""
        welcome = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   ██╗███╗   ██╗██╗   ██╗███████╗███████╗████████╗██╗███╗   ██╗   ║
║   ██║████╗  ██║██║   ██║██╔════╝██╔════╝╚══██╔══╝██║████╗  ██║   ║
║   ██║██╔██╗ ██║██║   ██║█████╗  ███████╗   ██║   ██║██╔██╗ ██║   ║
║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ╚════██║   ██║   ██║██║╚██╗██║   ║
║   ██║██║ ╚████║ ╚████╔╝ ███████╗███████║   ██║   ██║██║ ╚████║   ║
║   ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═══╝   ║
║                                                                  ║
║                     ██████╗ ██████╗ ███████╗                     ║
║                     ██╔══██╗██╔══██╗██╔════╝                     ║
║                     ██████╔╝██████╔╝███████╗                     ║
║                     ██╔══██╗██╔══██╗╚════██║                     ║
║                     ██████╔╝██║  ██║███████║                     ║
║                     ╚═════╝ ╚═╝  ╚═╝╚══════╝                     ║
║                                                                  ║
║              BBS-Style Financial Markets Terminal                ║
║                                                                  ║
║                    Press ENTER to continue...                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
        """
        console.print(Text(welcome, style="bright_green"))
        input()
        self.ui.clear_screen()
        
    def main_menu(self):
        """Display main BBS menu"""
        self.ui.draw_header("MAIN MENU")

        menu_items = [
            ("1", "Market Overview", "View major market indices"),
            ("2", "Cryptocurrency", "Crypto prices and trends"),
            ("3", "Forex", "Currency exchange rates"),
            ("4", "Commodities", "Gold, oil, and commodities"),
            ("5", "World Indices", "Global stock indices"),
            ("6", "Search Stocks", "Find specific stocks"),
            ("Q", "Quit", "Exit the terminal"),
        ]

        self.ui.draw_footer(f"User: {self.user} | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Use arrow key navigation
        choice = KeyboardInput.menu_select(menu_items)

        menu_map = {
            "1": "markets",
            "2": "crypto",
            "3": "forex",
            "4": "commodities",
            "5": "indices",
            "6": "stocks",
            "Q": "quit",
        }

        if choice in menu_map:
            if menu_map[choice] == "quit":
                self.running = False
                self.ui.clear_screen()
                console.print("[bright_green]Thank you for using Investing BBS. Goodbye![/]")
            else:
                self.current_menu = menu_map[choice]
                self.ui.clear_screen()
                
    def markets_menu(self):
        """Display major markets overview"""
        while True:
            self.ui.draw_header("MARKET OVERVIEW")

            try:
                data = self.api.get_major_indices()
                self.ui.draw_quote_table("Major Indices", data)
            except Exception as e:
                console.print(f"[red]Error fetching data: {e}[/]")

            self.ui.draw_footer("Press ← /ENTER to return | →/R to refresh | Q to quit")
            choice = KeyboardInput.get_key()

            # Handle arrow keys
            if choice == KeyboardInput.UP or choice == KeyboardInput.DOWN:
                # Ignore up/down arrows on data screens
                continue
            elif choice == KeyboardInput.LEFT or choice == KeyboardInput.ENTER:
                # Left arrow or Enter = go back to main menu
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            elif choice == KeyboardInput.RIGHT or choice.upper() == "R":
                # Right arrow or R = refresh
                self.ui.clear_screen()
            elif choice.upper() == "Q":
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            
    def crypto_menu(self):
        """Display cryptocurrency data"""
        while True:
            self.ui.draw_header("CRYPTOCURRENCY MARKETS")

            try:
                data = self.api.get_crypto()
                self.ui.draw_quote_table("Top Cryptocurrencies", data)
            except Exception as e:
                console.print(f"[red]Error fetching data: {e}[/]")

            self.ui.draw_footer("Press ← /ENTER to return | →/R to refresh | Q to quit")
            choice = KeyboardInput.get_key()

            # Handle arrow keys
            if choice == KeyboardInput.UP or choice == KeyboardInput.DOWN:
                # Ignore up/down arrows on data screens
                continue
            elif choice == KeyboardInput.LEFT or choice == KeyboardInput.ENTER:
                # Left arrow or Enter = go back to main menu
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            elif choice == KeyboardInput.RIGHT or choice.upper() == "R":
                # Right arrow or R = refresh
                self.ui.clear_screen()
            elif choice.upper() == "Q":
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            
    def forex_menu(self):
        """Display forex rates"""
        while True:
            self.ui.draw_header("FOREX / CURRENCY MARKETS")

            try:
                data = self.api.get_forex()
                self.ui.draw_quote_table("Major Currency Pairs", data)
            except Exception as e:
                console.print(f"[red]Error fetching data: {e}[/]")

            self.ui.draw_footer("Press ← /ENTER to return | →/R to refresh | Q to quit")
            choice = KeyboardInput.get_key()

            # Handle arrow keys
            if choice == KeyboardInput.UP or choice == KeyboardInput.DOWN:
                # Ignore up/down arrows on data screens
                continue
            elif choice == KeyboardInput.LEFT or choice == KeyboardInput.ENTER:
                # Left arrow or Enter = go back to main menu
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            elif choice == KeyboardInput.RIGHT or choice.upper() == "R":
                # Right arrow or R = refresh
                self.ui.clear_screen()
            elif choice.upper() == "Q":
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            
    def commodities_menu(self):
        """Display commodities data"""
        while True:
            self.ui.draw_header("COMMODITIES")

            try:
                data = self.api.get_commodities()
                self.ui.draw_quote_table("Commodity Prices", data)
            except Exception as e:
                console.print(f"[red]Error fetching data: {e}[/]")

            self.ui.draw_footer("Press ← /ENTER to return | →/R to refresh | Q to quit")
            choice = KeyboardInput.get_key()

            # Handle arrow keys
            if choice == KeyboardInput.UP or choice == KeyboardInput.DOWN:
                # Ignore up/down arrows on data screens
                continue
            elif choice == KeyboardInput.LEFT or choice == KeyboardInput.ENTER:
                # Left arrow or Enter = go back to main menu
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            elif choice == KeyboardInput.RIGHT or choice.upper() == "R":
                # Right arrow or R = refresh
                self.ui.clear_screen()
            elif choice.upper() == "Q":
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            
    def indices_menu(self):
        """Display world indices"""
        while True:
            self.ui.draw_header("WORLD INDICES")

            try:
                data = self.api.get_world_indices()
                self.ui.draw_quote_table("Global Stock Indices", data)
            except Exception as e:
                console.print(f"[red]Error fetching data: {e}[/]")

            self.ui.draw_footer("Press ← /ENTER to return | →/R to refresh | Q to quit")
            choice = KeyboardInput.get_key()

            # Handle arrow keys
            if choice == KeyboardInput.UP or choice == KeyboardInput.DOWN:
                # Ignore up/down arrows on data screens
                continue
            elif choice == KeyboardInput.LEFT or choice == KeyboardInput.ENTER:
                # Left arrow or Enter = go back to main menu
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            elif choice == KeyboardInput.RIGHT or choice.upper() == "R":
                # Right arrow or R = refresh
                self.ui.clear_screen()
            elif choice.upper() == "Q":
                self.current_menu = "main"
                self.ui.clear_screen()
                break
            
    def stocks_menu(self):
        """Search and display stocks"""
        self.ui.draw_header("STOCK SEARCH")

        symbol = KeyboardInput.get_input("\n[?] Enter stock symbol (e.g., AAPL): ").strip().upper()

        if symbol:
            try:
                data = self.api.search_stock(symbol)
                if data:
                    self.ui.draw_quote_table(f"Search Results: {symbol}", data)
                else:
                    console.print(f"[yellow]No results found for '{symbol}'[/]")
            except Exception as e:
                console.print(f"[red]Error fetching data: {e}[/]")

        self.ui.draw_footer("Press ENTER to return")

        # Wait for Enter key, ignore arrow keys
        while True:
            choice = KeyboardInput.get_key()
            if choice == KeyboardInput.ENTER:
                break
            # Ignore arrow keys and other keys

        self.current_menu = "main"
        self.ui.clear_screen()

def main():
    parser = argparse.ArgumentParser(
        description="Investing.com BBS-style CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  investing-bbs              Launch interactive BBS interface
  investing-bbs --version    Show version
        """
    )
    parser.add_argument("--version", action="store_true", help="Show version")
    
    args = parser.parse_args()
    
    if args.version:
        from investing_bbs import __version__
        console.print(f"Investing BBS v{__version__}")
        return
        
    app = InvestingBBS()
    app.run()

if __name__ == "__main__":
    main()
