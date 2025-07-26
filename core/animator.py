"""
Core animation logic
"""

import time
import sys
from typing import List
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.align import Align
from rich import box

from .ollama_client import OllamaClient
from .frame_parser import FrameParser
from ..ui.console import get_console
from ..ui.themes import get_theme_colors
from ..utils.fallback import get_fallback_animation

class ASCIIAnimator:
    """Main ASCII Animation class"""
    
    def __init__(self, config):
        self.config = config
        self.console = get_console()
        self.ollama_client = OllamaClient(config)
        self.frame_parser = FrameParser()
        
        # Speed mappings
        self.speed_delays = {
            "slow": 0.8,
            "normal": 0.4,
            "fast": 0.2,
            "turbo": 0.1
        }
    
    def animate(self, prompt: str):
        """Main animation function"""
        self.console.print(f"[cyan]🎬 Creating animation: [bold]{prompt}[/bold][/cyan]")
        self.console.print()
        
        # Get frames from Ollama or fallback
        frames = self._get_frames(prompt)
        
        if not frames:
            self.console.print("[red]❌ Failed to generate animation frames[/red]")
            return
        
        # Start animation
        self._play_animation(frames, prompt)
    
    def _get_frames(self, prompt: str) -> List[str]:
        """Get animation frames from Ollama or fallback"""
        try:
            self.console.print("[yellow]🤖 Generating frames with AI...[/yellow]")
            
            # Try Ollama first
            response = self.ollama_client.generate_frames(prompt)
            frames = self.frame_parser.parse_frames(response)
            
            if frames and len(frames) >= 2:
                self.console.print(f"[green]✅ Generated {len(frames)} frames![/green]")
                return frames
            else:
                raise Exception("Insufficient frames generated")
                
        except Exception as e:
            if self.config.debug:
                self.console.print(f"[yellow]⚠️  Ollama error: {e}[/yellow]")
            
            self.console.print("[yellow]🎲 Using fallback animation...[/yellow]")
            return get_fallback_animation(prompt, self.config.frames)
    
    def _play_animation(self, frames: List[str], title: str):
        """Play the animation with Rich Live"""
        theme_colors = get_theme_colors(self.config.theme)
        delay = self.speed_delays[self.config.speed]
        
        self.console.print(f"[green]🎭 Playing animation... (Press Ctrl+C to stop)[/green]")
        self.console.print()
        
        try:
            with Live(console=self.console, refresh_per_second=10) as live:
                frame_idx = 0
                while True:
                    current_frame = frames[frame_idx % len(frames)]
                    
                    # Apply theme coloring
                    colored_frame = self._colorize_frame(current_frame, theme_colors, frame_idx)
                    
                    # Create panel
                    panel = Panel(
                        Align.center(colored_frame),
                        title=f"[bold]{title}[/bold]",
                        subtitle=f"Frame {frame_idx % len(frames) + 1}/{len(frames)}",
                        box=box.ROUNDED,
                        style=theme_colors[0]
                    )
                    
                    live.update(panel)
                    time.sleep(delay)
                    frame_idx += 1
                    
        except KeyboardInterrupt:
            pass
    
    def _colorize_frame(self, frame: str, theme_colors: List[str], frame_idx: int) -> str:
        """Apply theme colors to frame"""
        if self.config.no_color:
            return frame
        
        # Cycle through theme colors
        color = theme_colors[frame_idx % len(theme_colors)]
        return f"[{color}]{frame}[/{color}]"