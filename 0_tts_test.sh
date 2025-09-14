#!/bin/bash
source .env
curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini-tts",
    "input": "Hello world!",
    "voice": "nova",
    "response_format": "mp3"
  }' --output hello1.mp3