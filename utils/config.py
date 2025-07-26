"""
Configuration management
"""

from dataclasses import dataclass

@dataclass
class Config:
    """Configuration for ASCII Animator"""
    model: str = "llama3"
    frames: int = 4
    speed: str = "normal"
    theme: str = "rainbow"
    style: str = "blocky"
    no_color: bool = False
    debug: bool = False