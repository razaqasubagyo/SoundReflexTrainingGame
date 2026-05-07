"""
file_manager.py
Module for saving session data for Sound Reflex Training Game
"""

import os
import json
from datetime import datetime

def save_session_data(avg_reaction, errors, difficulty, folder="sessions"):
    """
    Save basic session performance as JSON log
    """
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    data = {
        "timestamp": timestamp,
        "average_reaction_time": avg_reaction,
        "errors": errors,
        "difficulty_level": difficulty
    }
    filename = os.path.join(folder, f"log_{timestamp}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Performance log saved to {filename}")


def save_session_txt(performance, feedback, folder="sessions"):
    """
    Save session performance + LLM feedback as human-readable TXT
    """
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"session_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Timestamp: {timestamp}\n\n")
        f.write("=== Performance ===\n")
        f.write(f"Average Reaction Time: {performance['average_reaction_time']:.3f} seconds\n")
        f.write(f"Errors: {performance['errors']}\n")
        f.write(f"Difficulty Level: {performance['difficulty_level']}\n\n")
        f.write("=== LLM Feedback ===\n")
        f.write(f"Analysis: {feedback.get('analysis','')}\n")
        f.write(f"Recommendation: {feedback.get('recommendation','')}\n")
        f.write(f"Motivation: {feedback.get('motivation','')}\n")

    print(f"Session saved to {filename}")
