"""
Sound Reflex Training Game
FINAL UX + Adaptive Difficulty + LLM Feedback Disabilitas + FULLSCREEN + Scrollable Feedback
"""

import pygame
import time
import threading
import pyttsx3
from agent import AdaptiveAgent
from file_manager import save_session_data, save_session_txt
from llm_agent import get_feedback

pygame.init()

# ================= FULLSCREEN =================
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Sound Reflex Training")
font = pygame.font.Font(None, 60)

# ================= TTS =================
def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    threading.Thread(target=run, daemon=True).start()

def speak_blocking(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ================= UI =================
def draw_text(lines):
    screen.fill((0, 0, 0))
    height = screen.get_height()
    width = screen.get_width()
    y = height // 4
    for line in lines:
        if len(line) > 60:
            chunks = [line[i:i+60] for i in range(0, len(line), 60)]
            for chunk in chunks:
                label = font.render(chunk, True, (255, 255, 255))
                rect = label.get_rect(center=(width//2, y))
                screen.blit(label, rect)
                y += 80
        else:
            label = font.render(line, True, (255, 255, 255))
            rect = label.get_rect(center=(width//2, y))
            screen.blit(label, rect)
            y += 80
    pygame.display.update()

# ================= SCROLLABLE FEEDBACK =================
def show_feedback(feedback_text):
    lines = []
    for paragraph in feedback_text.split("\n"):
        chunks = [paragraph[i:i+60] for i in range(0, len(paragraph), 60)]
        lines.extend(chunks)

    height = screen.get_height()
    lines_per_screen = max((height // 80) - 1, 1)
    scroll_index = 0

    speak(" ".join(lines))

    scrolling = True
    while scrolling:
        screen.fill((0, 0, 0))
        visible_lines = lines[scroll_index:scroll_index + lines_per_screen]
        y = height // 8
        for line in visible_lines:
            label = font.render(line, True, (255, 255, 255))
            rect = label.get_rect(center=(screen.get_width()//2, y))
            screen.blit(label, rect)
            y += 80
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    scrolling = False
                if event.key == pygame.K_DOWN:
                    if scroll_index + lines_per_screen < len(lines):
                        scroll_index += 1
                if event.key == pygame.K_UP:
                    if scroll_index > 0:
                        scroll_index -= 1
        pygame.time.wait(50)

# ================= START MENU =================
def start_menu():
    draw_text([
        "Sound Reflex Training",
        "",
        "Press ENTER to Start",
        "Press Q to Quit"
    ])
    speak("Welcome to Sound Reflex Training.")
    time.sleep(1)
    speak("Press Enter to start. Press Q to quit.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                if event.key == pygame.K_q:
                    return False

# ================= INSTRUCTION SELECTION =================
def instruction_selection():
    draw_text([
        "Press I to hear instructions.",
        "Press SPACE to skip instructions and start the game."
    ])
    speak("Press I to hear instructions, or press SPACE to skip and start the game.")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    return "instructions"
                if event.key == pygame.K_SPACE:
                    return "skip"
                if event.key == pygame.K_ESCAPE:
                    return "menu"

# ================= INSTRUCTION SECTION =================
def instructions_section():
    tts_lines = [
        "You will hear a direction: left or right.",
        "Press the left or right arrow key as fast as possible.",
        "Your reaction time will be measured.",
        "Performance data will be saved after ten rounds."
    ]
    draw_text([
        "Instructions:",
        "- You will hear left or right directions.",
        "- Press corresponding arrow key quickly.",
        "- Reaction time will be recorded.",
        "- Data saved after ten rounds.",
        "Press SPACE to continue to countdown."
    ])
    time.sleep(0.5)
    for line in tts_lines:
        speak_blocking(line)
        time.sleep(0.3)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    return "menu"

# ================= COUNTDOWN =================
def countdown():
    for word in ["3", "2", "1", "Go"]:
        draw_text([word])
        speak(word)
        pygame.time.wait(900)

# ================= GAME LOOP =================
def run_game():
    agent = AdaptiveAgent()
    reaction_times = []
    rounds = 0
    MAX_ROUNDS = 10

    countdown()

    while True:
        draw_text([
            f"Round {rounds + 1} of {MAX_ROUNDS}",
            "Press SPACE for next round"
        ])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                if event.key == pygame.K_SPACE:
                    instruction = agent.choose_instruction()
                    speak(instruction)

                    display_time = max(1000 / agent.speed_multiplier, 300)

                    draw_text([
                        f"Round {rounds + 1} of {MAX_ROUNDS}",
                        "React now!"
                    ])
                    start_time = time.time()
                    reacting = True

                    while reacting:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                return "quit"
                            if e.type == pygame.KEYDOWN:
                                if e.key == pygame.K_ESCAPE:
                                    return "menu"

                                reaction_time = time.time() - start_time
                                correct = (
                                    (e.key == pygame.K_LEFT and instruction == "left") or
                                    (e.key == pygame.K_RIGHT and instruction == "right")
                                )

                                agent.update_performance(instruction, reaction_time, correct)
                                reaction_times.append(reaction_time)

                                if correct:
                                    draw_text([f"Correct! {reaction_time:.2f} seconds"])
                                else:
                                    draw_text(["Wrong response"])

                                pygame.time.wait(int(display_time))
                                rounds += 1
                                reacting = False

        if rounds >= MAX_ROUNDS:
            avg = sum(reaction_times) / len(reaction_times)

            save_session_data(
                avg_reaction=avg,
                errors=agent.error_count,
                difficulty=agent.speed_multiplier
            )

            performance = {
                "average_reaction_time": avg,
                "errors": agent.error_count,
                "difficulty_level": agent.speed_multiplier
            }

            draw_text([
                "Session complete",
                "Performance data saved",
                "",
                "LLM Feedback: Processing..."
            ])
            pygame.display.update()

            feedback = {
                "analysis": "No feedback available.",
                "recommendation": "No feedback available.",
                "motivation": "No feedback available."
            }

            def get_llm():
                nonlocal feedback
                feedback = get_feedback(performance)

            llm_thread = threading.Thread(target=get_llm)
            llm_thread.start()

            while llm_thread.is_alive():
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            exit()
                pygame.time.wait(100)

            agent.adjust_difficulty(feedback)

            # === SIMPAN TXT (INI SATU-SATUNYA TAMBAHAN) ===
            save_session_txt(
                performance=performance,
                feedback=feedback
            )

            feedback_text = (
                f"Analysis: {feedback.get('analysis','')}\n"
                f"Recommendation: {feedback.get('recommendation','')}\n"
                f"Motivation: {feedback.get('motivation','')}"
            )

            show_feedback(feedback_text)
            return "menu"

# ================= APP LOOP =================
app_running = True
while app_running:
    if not start_menu():
        break

    selection = instruction_selection()
    if selection == "quit":
        break
    if selection == "menu":
        continue
    if selection == "instructions":
        result = instructions_section()
        if result == "menu":
            continue

    result = run_game()
    if result == "quit":
        break

pygame.quit()
