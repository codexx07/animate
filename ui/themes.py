"""
Color themes for animations
"""

THEMES = {
    "rainbow": ["red", "yellow", "green", "cyan", "blue", "magenta"],
    "neon": ["bright_cyan", "bright_magenta", "bright_green", "bright_yellow"],
    "fire": ["red", "bright_red", "yellow", "bright_yellow"],
    "ocean": ["blue", "cyan", "bright_blue", "bright_cyan"],
    "forest": ["green", "bright_green", "yellow", "white"],
    "sunset": ["red", "magenta", "yellow", "orange"],
    "mono": ["white", "bright_white", "dim white"],
    "retro": ["magenta", "cyan", "yellow", "green"],
    "pastel": ["light_pink", "light_blue", "light_green", "light_yellow"],
    "matrix": ["green", "bright_green", "dim green"],
}

def get_theme_colors(theme_name: str) -> list:
    """Get color list for theme"""
    return THEMES.get(theme_name, THEMES["rainbow"])


