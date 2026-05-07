# Sound Reflex Training Game

An accessible, audio-based reflex training application built in Python, designed for users with visual impairments or motor response challenges. Integrates Google Gemini 2.5 to generate personalised performance feedback after each session.

## Overview

Many training applications are overly heavy and complex, limiting accessibility for their intended users. Sound Reflex addresses this by providing a lightweight, inclusive training tool that relies on audio-based interaction and adaptive pacing — removing the dependency on visual cues and reducing barriers for users with disabilities.

The application is intended for use in educational institutions, rehabilitation programs, and similar settings to support measurable improvement in auditory processing, motor response coordination, and sustained attention.

## Features

- **Audio-only interaction** with text-to-speech output for full accessibility
- **Adaptive difficulty** that adjusts session pace based on user performance, without visible level indicators to reduce pressure
- **LLM-powered feedback** using Google Gemini 2.5 — generates personalised performance analysis, improvement recommendations, and motivational messages after each session
- **Session logging** in JSON format for institutional use, progress tracking, and potential analytics integration
- **Simple controls** requiring only a standard keyboard, reducing input barriers for users with motor challenges
- **Modular architecture** across separate components for gameplay, adaptive logic, LLM feedback, and file management

## Tech Stack

- Python
- Pygame
- Google Gemini 2.5 API
- JSON for session logging and data persistence

## Architecture

The application is structured as separate Python modules, each with a distinct responsibility:

| Module | Responsibility |
|---|---|
| `main.py` | Core game loop, audio directions, reaction time measurement, UI |
| `agent.py` | Adaptive difficulty logic via `AdaptiveAgent` class |
| `llm_agent.py` | LLM integration with Google Gemini for feedback generation |
| `file_manager.py` | Session logging and data persistence |

## Project Context

Developed as an individual MSc project at Warwick Business School (2026) as part of the MSc in Management of Information Systems & Digital Innovation.

Built using an iterative, agile-style workflow — features were developed incrementally with AI-assisted development tools used as a collaborative layer alongside manual reasoning, debugging, and testing.

## References

- UNESCO (2020). *Global education monitoring report: Inclusion and education.* Paris: UNESCO.
- Yuan, B., Folmer, E. and Harris, F.C. (2011). 'Game accessibility: A survey', *Universal Access in the Information Society*, 10(1), pp. 81–100.
