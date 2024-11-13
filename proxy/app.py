from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Define a Pydantic model for the request body
class TextRequest(BaseModel):
    text: str

# Define the URLs of the other services
SENTIMENT_SERVICE_URL = "http://sentiment_service:8001/analyze_sentiment"
NER_SERVICE_URL = "http://ner_service:8002/extract_entities"

@app.post("/process_text")
def process_text(request: TextRequest):
    text = request.text

    # Step 1: Sentiment Analysis
    sentiment_response = requests.post(SENTIMENT_SERVICE_URL, json={"text": text})
    sentiment_result = sentiment_response.json()
    text = f"{text}, Sentiment: {sentiment_result.get('sentiment')[0].get('label')}"
    print(text, flush = True)
    # Step 2: NER Analysis
    ner_response = requests.post(NER_SERVICE_URL, json={"text": text})
    ner_result = ner_response.json()

    return {
        "sentiment": sentiment_result,
        "entities": ner_result
    }
