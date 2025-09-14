from dotenv import load_dotenv
import os
import requests

load_dotenv()  # reads .env and sets environment variables
api_key = os.environ.get("OPENAI_API_KEY")
# Use api_key in your code, but do not print it
if api_key:
    print("API key loaded successfully!")
else:
    print("API key not found.")

url = "https://api.openai.com/v1/audio/speech"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-4o-mini-tts",
    "input": "Hello world, This is AI class!",
    "voice": "nova",
    "response_format": "mp3"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    with open("hello1.mp3", "wb") as f:
        f.write(response.content)
    print("Audio saved as hello1.mp3")
else:
    print(f"Error: {response.status_code}")
    print(response.text)