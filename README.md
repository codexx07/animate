```markdown
# 🎬 ASCII Animator

Create stunning ASCII animations with AI! Transform any text prompt into beautiful animated ASCII art using Ollama.

## ✨ Features

- 🤖 **AI-Powered**: Uses Ollama to generate creative ASCII animations
- 🎨 **Beautiful Themes**: 10+ color themes (rainbow, neon, fire, ocean, etc.)
- ⚡ **Variable Speed**: From slow to turbo speed
- 🎭 **Multiple Styles**: Blocky, minimal, detailed, figlet styles
- 🛡️ **Fallback System**: Works even when Ollama is offline
- 🎪 **Rich UI**: Beautiful terminal interface with Rich

## 🚀 Quick Start

### Installation

```bash
pip install ascii-animator
```

### Usage

```bash
# Basic usage
animate "a spinning wheel"

# With options
animate "a dancing banana" --theme neon --speed fast
animate "a rotating cube" --frames 6 --style figlet
```

## 🎮 Examples

```bash
animate "a car rotating"
animate "a bouncing ball" --theme fire --speed turbo
animate "a waving flag" --frames 8 --theme ocean
animate "a spinning top" --style minimal --theme matrix
```

## 🎨 Themes

- `rainbow` - Colorful rainbow cycle
- `neon` - Bright neon colors  
- `fire` - Red/yellow fire colors
- `ocean` - Blue/cyan ocean colors
- `forest` - Green nature colors
- `sunset` - Warm sunset colors
- `mono` - Monochrome white
- `retro` - 80s retro colors
- `matrix` - Green matrix style

## ⚙️ Setup Ollama

1. Install Ollama: https://ollama.ai
2. Pull a model: `ollama pull llama3`
3. Start Ollama: `ollama serve`

## 🔧 Development

```bash
git clone https://github.com/yourusername/ascii-animator
cd ascii-animator
pip install -e .
```