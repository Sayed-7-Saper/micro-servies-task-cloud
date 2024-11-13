from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Define a Pydantic model for the request body
class TextRequest(BaseModel):
    text: str

# Load the sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

@app.post("/analyze_sentiment")
def analyze_sentiment(request: TextRequest):
    text = request.text
    result = sentiment_analyzer(text)
    return {"sentiment": result}
