# Sound Reflex Training Game

> An accessible, audio-based reflex training application with LLM-powered feedback — built in Python for users with visual impairments or motor response challenges.

Developed as an individual MSc project at Warwick Business School, 2026.

---

## Overview

Many training applications rely on visual cues and static difficulty settings, limiting accessibility for users with disabilities. Sound Reflex addresses this by providing a lightweight, audio-first training tool that adapts to user performance and delivers personalised AI-generated feedback after each session.

Intended for use in educational institutions, rehabilitation programs, and inclusive training environments.

---

## Features

- **Audio-only interaction** — directions delivered via text-to-speech, no visual dependency
- **Adaptive difficulty** — internal agent adjusts session pace based on user performance, without visible level indicators
- **LLM-powered feedback** — Google Gemini 2.5 generates personalised performance analysis, recommendations, and motivational messages after each session
- **Session logging** — performance data saved as JSON (structured) and TXT (human-readable) for institutional tracking
- **Simple keyboard controls** — only left/right arrow keys required, reducing input barriers
- **Fullscreen UI** — minimises distractions for users with focus or attention challenges
- **Scrollable feedback display** — ensures AI feedback is fully readable on any screen size

---

## Architecture

The application is structured as separate Python modules, each with a distinct responsibility:

| Module | Responsibility |
|---|---|
| `main.py` | Core game loop, TTS, reaction time measurement, UI rendering |
| `agent.py` | Adaptive difficulty via `AdaptiveAgent` class |
| `llm_agent.py` | Google Gemini integration for post-session feedback generation |
| `file_manager.py` | Session logging and data persistence |

---

## Sample Output

**Session log (JSON):**
```json
{
    "timestamp": "2026-01-24_20-35-24",
    "average_reaction_time": 1.095,
    "errors": 1,
    "difficulty_level": 1.0
}
```

**LLM Feedback (TXT):**
```
Analysis: You demonstrated excellent accuracy with only one error, indicating strong focus and understanding during the session.
Recommendation: Ensure your setup is optimally comfortable for sustained engagement.
Motivation: You are doing wonderfully — celebrate this great progress and consistency in your training!
```

---

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set up Google Gemini API key

In `llm_agent.py`, replace the placeholder with your key:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

### 3. Run the application

```bash
python main.py
```

---

## Controls

| Key | Action |
|---|---|
| `ENTER` | Start game |
| `I` | Listen to instructions |
| `SPACE` | Proceed / Skip / Continue |
| `LEFT / RIGHT` | Respond to audio cues |
| `ESC` | Exit application |

---

## Tech Stack

- Python 3.9+
- Pygame
- pyttsx3 (text-to-speech)
- Google Gemini 2.5 Flash API

---

## Development Approach

Built iteratively using an agile-style workflow — core gameplay first, then accessibility features, then adaptive difficulty and LLM integration. AI-assisted development tools were used throughout as a collaborative layer alongside manual reasoning, debugging, and testing.
