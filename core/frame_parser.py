"""
Parse ASCII frames from AI response
"""

import re
from typing import List

class FrameParser:
    """Parse and clean ASCII animation frames"""
    
    def __init__(self):
        self.frame_patterns = [
            r"Frame\s*(\d+)[:\s]*\n(.*?)(?=Frame\s*\d+|$)",
            r"(\d+)[:\.\)]\s*\n(.*?)(?=\d+[:\.\)]|$)",
            r"```\n(.*?)\n```",
        ]
    
    def parse_frames(self, response: str) -> List[str]:
        """Extract frames from AI response"""
        frames = []
        
        # Try different parsing patterns
        for pattern in self.frame_patterns:
            matches = re.findall(pattern, response, re.DOTALL | re.IGNORECASE)
            if matches:
                if isinstance(matches[0], tuple):
                    frames = [match[1].strip() if len(match) > 1 else match[0].strip() 
                             for match in matches]
                else:
                    frames = [match.strip() for match in matches]
                break
        
        # If no patterns match, try splitting by common delimiters
        if not frames:
            frames = self._split_by_delimiters(response)
        
        # Clean and validate frames
        frames = [self._clean_frame(frame) for frame in frames if frame.strip()]
        frames = [frame for frame in frames if self._is_valid_frame(frame)]
        
        return frames[:10]  # Limit to reasonable number
    
    def _split_by_delimiters(self, text: str) -> List[str]:
        """Split text by common delimiters"""
        delimiters = ["\n\n\n", "---", "===", "***"]
        
        for delimiter in delimiters:
            parts = text.split(delimiter)
            if len(parts) > 1:
                return parts
        
        # Fallback: split by double newlines
        return text.split("\n\n")
    
    def _clean_frame(self, frame: str) -> str:
        """Clean up a single frame"""
        # Remove common prefixes
        prefixes = ["Frame", "frame", r"\d+[\:\.\)]", "```"]
        for prefix in prefixes:
            frame = re.sub(f"^{prefix}.*?\n", "", frame, flags=re.IGNORECASE)
        
        # Remove trailing/leading whitespace but preserve internal structure
        lines = frame.split('\n')
        lines = [line.rstrip() for line in lines]
        
        # Remove empty lines at start and end
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()
        
        return '\n'.join(lines)
    
    def _is_valid_frame(self, frame: str) -> bool:
        """Check if frame is valid ASCII art"""
        if not frame.strip():
            return False
        
        lines = frame.split('\n')
        
        # Must have at least 2 lines
        if len(lines) < 2:
            return False
        
        # Must contain some ASCII art characters
        ascii_chars = set('|/\\#*+=<>^v()[]{}~`\'"-_.,;:!?@$%&')
        if not any(any(c in ascii_chars for c in line) for line in lines):
            return False
        
        return True