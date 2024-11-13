import requests

response = requests.post("http://0.0.0.0:8003/process_text",
                         json = {
  "text": "OpenAI is launching new AI models in 2024."
}
).json()
