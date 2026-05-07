import google.generativeai as genai

API_KEY = "YOUR_GEMINI_API_KEY"  # ganti dengan API key Gemini kamu
genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"

def get_feedback(performance: dict) -> dict:
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"""
You are an adaptive training coach for users with disabilities.
Analyze the following session performance:

Average reaction time: {performance.get('average_reaction_time')}
Errors: {performance.get('errors')}

Provide tips or motivation suitable for someone with accessibility needs.

Respond exactly in this format:

ANALYSIS:
<one or two sentences>

RECOMMENDATION:
<one practical suggestion>

MOTIVATION:
<one encouraging sentence>
"""
        response = model.generate_content(prompt)
        text = (response.text or "").strip()

        feedback = {"analysis":"", "recommendation":"", "motivation":""}
        section = None
        for line in text.splitlines():
            line = line.strip()
            if line.startswith("ANALYSIS"):
                section = "analysis"; continue
            if line.startswith("RECOMMENDATION"):
                section = "recommendation"; continue
            if line.startswith("MOTIVATION"):
                section = "motivation"; continue
            if section and line:
                feedback[section] += line + " "
        for key in feedback:
            if not feedback[key].strip():
                feedback[key] = "No feedback available."
        return feedback
    except Exception as e:
        print("LLM request failed:", e)
        return {
            "analysis":"No feedback available.",
            "recommendation":"No feedback available.",
            "motivation":"No feedback available."
        }
