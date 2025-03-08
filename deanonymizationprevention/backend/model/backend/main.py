from fastapi import FastAPI
import pickle
import uvicorn
from pydantic import BaseModel

# Load the trained AI model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the FastAPI app
app = FastAPI()

# Request schema
class TextData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI-Based De-Anonymization Prevention System"}

@app.post("/predict/")
def predict(data: TextData):
    """
    Predict whether the given text contains de-anonymization risk.
    """
    prediction = model.predict([data.text])
    return {"prediction": "Anonymized" if prediction[0] == 1 else "Not Anonymized"}

# Run the API locally (not needed for Render)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
