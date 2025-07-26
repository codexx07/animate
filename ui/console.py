"""
Rich console configuration
"""

from rich.console import Console
from rich.theme import Theme

# Custom theme for better aesthetics
CUSTOM_THEME = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "highlight": "bold yellow",
    "accent": "bold blue",
})

_console = None

def get_console() -> Console:
    """Get configured console instance"""
    global _console
    if _console is None:
        _console = Console(
            theme=CUSTOM_THEME,
            force_terminal=True,
            width=120,
            legacy_windows=False
        )
    return _console