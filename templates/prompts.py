"""
Prompt templates for different animation styles
"""

def get_prompt_template(subject: str, frames: int, style: str) -> str:
    """Generate prompt based on subject and style"""
    
    style_instructions = {
        "blocky": "Make it bold and blocky using characters like █, ▓, ▒, ░, |, #, =, +",
        "minimal": "Use simple characters like |, /, \\, -, _, and spaces for clean lines",
        "detailed": "Use a variety of ASCII characters for detailed representation",
        "figlet": "Style it like FIGlet fonts with bold, geometric shapes"
    }
    
    base_prompt = f"""You are an expert ASCII artist. Create {frames} animation frames showing {subject}.

Style: {style_instructions.get(style, style_instructions['blocky'])}

Requirements:
- Each frame should be clearly labeled as "Frame 1:", "Frame 2:", etc.
- Use only ASCII characters
- Make each frame 8-15 lines tall and 20-40 characters wide
- Show smooth progression between frames
- Keep the same general size across all frames
- Make it visually appealing and recognizable

Create {frames} distinct frames that when played in sequence will show {subject}.

Example format:
Frame 1:
    ___
   |   |
   |___|

Frame 2:
    ___
   /   /
  /___ /

Generate the frames now:"""

    return base_prompt