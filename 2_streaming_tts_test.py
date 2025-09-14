# 2_streaming_tts_test.py
# This script reads text from a file, sends it to OpenAI's TTS API using AsyncOpenAI, and streams the audio to your laptop's speaker.

import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Read text from a file
text = ""
with open("Audio.txt", "r") as f:
    text = f.read().strip()
    print(f"Text to be converted to speech: {text}")

client = AsyncOpenAI(api_key=api_key)

async def main():
    
    # Streaming TTS request
    print(text)
    response = await client.audio.speech.create(
        model="gpt-4o-mini-tts",
        input=text,
        voice="nova",
        response_format="pcm"
    )
    await LocalAudioPlayer().play(response)

if __name__ == "__main__":
    asyncio.run(main())
