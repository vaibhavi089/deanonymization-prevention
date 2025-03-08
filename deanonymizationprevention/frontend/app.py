import gradio as gr
import requests

# Backend API URL
BACKEND_URL = "https://your-backend-url.onrender.com/predict"

def analyze_message(message):
    response = requests.post(BACKEND_URL, json={"message": message})
    if response.status_code == 200:
        result = response.json()
        return f"Risk Level: {result['risk_level']}\nSuggestions: {result['suggestions']}"
    return "Error analyzing message"

# Gradio Interface
interface = gr.Interface(
    fn=analyze_message,
    inputs="text",
    outputs="text",
    title="AI-Based De-Anonymization Prevention",
    description="Enter your anonymous message and see if it contains identifiable information."
)

interface.launch()
