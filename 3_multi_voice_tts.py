# 3_multi_voice_tts.py
"""
This script cycles through multiple OpenAI voices and effects, generating TTS for each combination.
- Reads lines from 'Audio.txt' (one narration per line)
- For each line, generates audio with different voices and effects
- Saves each result as an mp3 file with a descriptive filename
- Optionally, can stream audio directly to speakers (set STREAM_AUDIO=True)

Requirements:
- openai>=1.0.0
- python-dotenv
- requests
- sounddevice (if streaming)

Edit the VOICES and EFFECTS lists to try more options.
"""

import os
from dotenv import load_dotenv
import asyncio
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer


# Config
VOICES = ["nova", "shimmer", "echo"]  # Add more voices as desired
INSTRUCTIONS = [
    None,
    "Speak in a dramatic tone.",
    "Read as if telling a bedtime story.",
    "Use a cheerful and energetic style.",
    "Speak slowly and clearly."
]  # Add more instructions as desired
STREAM_AUDIO = False  # Set to True to stream audio instead of saving

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Read lines from text file
with open("Audio.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip()]

client = AsyncOpenAI(api_key=api_key)

async def synthesize_and_play(text, voice, instruction=None):
    params = {
        "model": "gpt-4o-mini-tts",
        "input": text,
        "voice": voice,
        "response_format": "mp3"
    }
    if instruction:
        params["instructions"] = instruction
    response = await client.audio.speech.create(**params)
    filename = f"output_{voice}"
    if instruction:
        safe_instruction = instruction.replace(" ", "_").replace(".", "").replace(",", "").replace("-", "_")[:30]
        filename += f"_{safe_instruction}"
    filename += ".mp3"
    with open(filename, "wb") as f:
        f.write(await response.aread())
    print(f"Saved: {filename}")
    if STREAM_AUDIO:
        await LocalAudioPlayer().play(response)

async def main():
    for text in lines:
        for voice in VOICES:
            for instruction in INSTRUCTIONS:
                await synthesize_and_play(text, voice, instruction)

if __name__ == "__main__":
    asyncio.run(main())
