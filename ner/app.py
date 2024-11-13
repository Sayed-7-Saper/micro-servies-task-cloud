from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Define a Pydantic model for the request body
class TextRequest(BaseModel):
    text: str

# Load the NER model
ner = pipeline("ner", aggregation_strategy="simple")

@app.post("/extract_entities")
def extract_entities(request: TextRequest):
    text = request.text
    ner_results = ner(text)

    # Convert results to JSON serializable format
    processed_results = [
        {
            "entity": entity["entity_group"],
            "word": entity["word"],
            "score": float(entity["score"]),
            "start": entity["start"],
            "end": entity["end"]
        }
        for entity in ner_results
    ]

    return {"entities": processed_results}
