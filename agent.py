import random

class AdaptiveAgent:
    def __init__(self):
        self.speed_multiplier = 1.0  # Difficulty factor
        self.error_count = 0
        self.performance_log = []

    def choose_instruction(self):
        """Randomly choose left or right"""
        return random.choice(["left", "right"])

    def update_performance(self, instruction, reaction_time, correct):
        """Update agent performance and log"""
        self.performance_log.append({
            "instruction": instruction,
            "reaction_time": reaction_time,
            "correct": correct
        })
        if not correct:
            self.error_count += 1

    def adjust_difficulty(self, llm_feedback):
        """Adjust speed_multiplier based on LLM recommendation"""
        rec = llm_feedback.get("recommendation", "").lower()
        if "increase difficulty" in rec:
            self.speed_multiplier = min(self.speed_multiplier + 0.1, 2.0)
        elif "decrease difficulty" in rec:
            self.speed_multiplier = max(self.speed_multiplier - 0.1, 0.5)