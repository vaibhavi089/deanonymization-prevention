import gradio as gr
import requests
import os

# Backend API URL (Set directly to your Render backend URL)
BACKEND_URL = "https://deanonymization-prevention-4.onrender.com/predict"

def analyze_message(message):
    try:
        response = requests.post(BACKEND_URL, json={"message": message})
        if response.status_code == 200:
            result = response.json()
            return f"Risk Level: {result.get('risk_level', 'Unknown')}\nSuggestions: {result.get('suggestions', 'None')}"
        return "Error analyzing message: Invalid response"
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Gradio Interface
interface = gr.Interface(
    fn=analyze_message,
    inputs=gr.Textbox(label="Enter Message"),
    outputs=gr.Textbox(label="Analysis Result"),
    title="AI-Based De-Anonymization Prevention",
    description="Enter an anonymous message to check if it contains identifiable information."
)

if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 7860)))
