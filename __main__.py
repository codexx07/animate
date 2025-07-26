"""
ASCII Animator CLI Entry Point
"""

import sys
import argparse
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

from .core.animator import ASCIIAnimator
from .ui.console import get_console
from .ui.themes import THEMES
from .utils.config import Config

def create_banner():
    """Create a beautiful banner for the CLI"""
    console = get_console()
    
    banner_text = """
╔═══════════════════════════════════════╗
║           ASCII ANIMATOR              ║
║     ✨ AI-Powered ASCII Art Magic ✨    ║
╚═══════════════════════════════════════╝
    """
    
    return Panel(
        Text(banner_text, style="bold cyan"),
        box=box.DOUBLE,
        style="bright_blue",
        title="[bold magenta]Welcome[/bold magenta]",
        title_align="center"
    )

def main():
    """Main CLI function"""
    console = get_console()
    
    # Show banner
    console.print(create_banner())
    console.print()
    
    parser = argparse.ArgumentParser(
        description="🎬 Create stunning ASCII animations with AI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:  "a spinning wheel"  "a dancing banana" --theme neon --speed fast  "a rotating cube" --frames 6 --model llama3
        """
    )
    
    parser.add_argument(
        "prompt", 
        help="🎯 Description of the animation (e.g., 'a spinning car')"
    )
    
    parser.add_argument(
        "--model", 
        default="llama3",
        help="🤖 Ollama model to use (default: llama3)"
    )
    
    parser.add_argument(
        "--frames", 
        type=int, 
        default=4,
        help="🎞️ Number of animation frames (default: 4)"
    )
    
    parser.add_argument(
        "--speed", 
        choices=["slow", "normal", "fast", "turbo"],
        default="normal",
        help="⚡ Animation speed (default: normal)"
    )
    
    parser.add_argument(
        "--theme", 
        choices=list(THEMES.keys()),
        default="rainbow",
        help="🎨 Color theme (default: rainbow)"
    )
    
    parser.add_argument(
        "--style", 
        choices=["blocky", "minimal", "detailed", "figlet"],
        default="blocky",
        help="🎭 ASCII art style (default: blocky)"
    )
    
    parser.add_argument(
        "--no-color", 
        action="store_true",
        help="🚫 Disable colors"
    )
    
    parser.add_argument(
        "--debug", 
        action="store_true",
        help="🐛 Enable debug mode"
    )
    
    args = parser.parse_args()
    
    # Create config
    config = Config(
        model=args.model,
        frames=args.frames,
        speed=args.speed,
        theme=args.theme,
        style=args.style,
        no_color=args.no_color,
        debug=args.debug
    )
    
    try:
        # Create and run animator
        animator = ASCIIAnimator(config)
        animator.animate(args.prompt)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]⏹️  Animation stopped by user[/yellow]")
        sys.exit(0)
    except Exception as e:
        if args.debug:
            console.print_exception()
        else:
            console.print(f"[red]❌ Error: {e}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()