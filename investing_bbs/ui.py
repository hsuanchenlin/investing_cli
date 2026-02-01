"""
BBS-style UI components using Rich
"""

import os
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.box import DOUBLE, ROUNDED, HEAVY
from rich.align import Align
from rich import box

class BBSInterface:
    """BBS-style terminal interface"""
    
    def __init__(self, console: Console):
        self.console = console
        self.width = 80
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')
        
    def draw_header(self, title: str):
        """Draw BBS-style header"""
        header_text = f"╔{'═' * 78}╗\n"
        header_text += f"║{' ':^78}║\n"
        
        # Center the title
        title_display = f"◄ {title} ►"
        padding = (78 - len(title_display)) // 2
        header_text += f"║{' ' * padding}{title_display}{' ' * (78 - padding - len(title_display))}║\n"
        
        header_text += f"║{' ':^78}║\n"
        header_text += f"╚{'═' * 78}╝"
        
        self.console.print(Text(header_text, style="bright_cyan"))
        
    def draw_footer(self, status: str = ""):
        """Draw BBS-style footer"""
        footer_text = f"╔{'═' * 78}╗\n"
        
        status_display = f" {status} " if status else " Ready "
        padding = 78 - len(status_display) - 2
        footer_text += f"║{status_display}{' ' * padding}║\n"
        
        footer_text += f"╚{'═' * 78}╝"
        
        self.console.print(Text(footer_text, style="bright_blue"))
        
    def draw_menu(self, items: list):
        """Draw BBS-style menu
        
        Args:
            items: List of tuples (key, title, description)
        """
        menu_text = "\n"
        menu_text += "┌────────────────────────────────────────────────────────────────────────────┐\n"
        menu_text += "│                              MAIN MENU                                      │\n"
        menu_text += "├────────────────────────────────────────────────────────────────────────────┤\n"
        
        for key, title, desc in items:
            key_display = f"[{key}]"
            line = f"│  {key_display:<6} {title:<20} {desc:<40}      │"
            menu_text += line + "\n"
            
        menu_text += "└────────────────────────────────────────────────────────────────────────────┘"
        
        self.console.print(Text(menu_text, style="bright_white"))
        
    def draw_quote_table(self, title: str, data: list):
        """Draw a financial quote table
        
        Args:
            title: Table title
            data: List of dicts with keys: symbol, name, price, change, change_pct
        """
        table = Table(
            title=title,
            box=box.DOUBLE_EDGE,
            border_style="bright_cyan",
            title_style="bright_yellow bold",
            header_style="bright_green bold",
            show_header=True,
            width=self.width
        )
        
        table.add_column("Symbol", style="bright_white", width=12)
        table.add_column("Name", style="white", width=25)
        table.add_column("Price", justify="right", style="bright_white", width=15)
        table.add_column("Change", justify="right", width=12)
        table.add_column("%", justify="right", width=10)
        
        for item in data:
            change = item.get('change', 0)
            change_pct = item.get('change_pct', 0)
            
            # Color based on positive/negative
            if change >= 0:
                change_style = "bright_green"
                change_str = f"+{change:,.2f}"
                pct_str = f"+{change_pct:,.2f}%"
            else:
                change_style = "bright_red"
                change_str = f"{change:,.2f}"
                pct_str = f"{change_pct:,.2f}%"
                
            table.add_row(
                item.get('symbol', 'N/A'),
                item.get('name', 'Unknown')[:24],
                f"{item.get('price', 0):,.2f}",
                Text(change_str, style=change_style),
                Text(pct_str, style=change_style)
            )
            
        self.console.print(table)
        
    def draw_info_box(self, title: str, content: str):
        """Draw an info box"""
        panel = Panel(
            content,
            title=title,
            border_style="bright_magenta",
            box=box.ROUNDED,
            width=self.width
        )
        self.console.print(panel)
        
    def draw_message(self, message: str, style: str = "white"):
        """Draw a message line"""
        box_line = f"╔{'═' * 78}╗\n"
        box_line += f"║  {message:<76}║\n"
        box_line += f"╚{'═' * 78}╝"
        self.console.print(Text(box_line, style=style))
