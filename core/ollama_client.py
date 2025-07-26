import requests
import json
from typing import Optional
from ..templates.prompts import get_prompt_template

class OllamaClient:
    """Client for interacting with Ollama API"""
    
    def __init__(self, config):
        self.config = config
        self.base_url = "http://localhost:11434"
        self.timeout = 30
    
    def generate_frames(self, prompt: str) -> str:
        """Generate animation frames using Ollama"""
        full_prompt = get_prompt_template(
            prompt, 
            self.config.frames, 
            self.config.style
        )
        
        payload = {
            "model": self.config.model,
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": 0.7,
                "top_p": 0.9,
                "num_predict": 1000
            }
        }
        
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "")
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ollama API error: {e}")
    
    def check_connection(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False