"""
Fallback animations when Ollama is unavailable
"""

from typing import List
import random

FALLBACK_ANIMATIONS = {
    "spinner": [
        "    |    ",
        "    /    ",
        "    -    ",
        "    \\    "
    ],
    "dots": [
        "●○○○",
        "○●○○", 
        "○○●○",
        "○○○●"
    ],
    "wave": [
        "~~~~~",
        "~~~~~",
        "~~~~~",
        "~~~~~"
    ],
    "bounce": [
        "    ●    \n        \n        ",
        "         \n    ●    \n        ",
        "         \n         \n    ●    ",
        "         \n    ●    \n        "
    ]
}

THEMED_ANIMATIONS = {
    "car": [
        "  ____\n []--[]",
        "  ____\n /]--[\\",
        "  ____\n |]--[|",
        "  ____\n \\]--[/"
    ],
    "banana": [
        "   /\n  (\n   \\",
        "  __\n /  )\n(   \\",
        " (  )\n(   )\n \\__/",
        "  __\n(   \\\n \\   )"
    ],
    "cube": [
        "┌─┐\n│ │\n└─┘",
        "╭─╮\n│ │\n╰─╯",
        "┌─┐\n│ │\n└─┘",
        "╭─╮\n│ │\n╰─╯"
    ]
}

def get_fallback_animation(prompt: str, frames: int) -> List[str]:
    """Get fallback animation based on prompt"""
    prompt_lower = prompt.lower()
    
    # Check for themed animations
    for theme, animation in THEMED_ANIMATIONS.items():
        if theme in prompt_lower:
            return animation[:frames] if len(animation) >= frames else animation * 2
    
    # Check for generic patterns
    if any(word in prompt_lower for word in ["spin", "rotate", "turn"]):
        return FALLBACK_ANIMATIONS["spinner"][:frames]
    elif any(word in prompt_lower for word in ["bounce", "jump", "hop"]):
        return FALLBACK_ANIMATIONS["bounce"][:frames]
    elif any(word in prompt_lower for word in ["wave", "flow", "ripple"]):
        return FALLBACK_ANIMATIONS["wave"][:frames]
    else:
        return FALLBACK_ANIMATIONS["dots"][:frames]