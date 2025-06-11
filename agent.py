import os
import asyncio
import websockets
import json
from dotenv import load_dotenv
from deepgram import Deepgram
import requests

# Load environment variables
load_dotenv()

LIVEKIT_URL = os.getenv("LIVEKIT_URL")
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
CARTESIA_API_KEY = os.getenv("CARTESIA_API_KEY")
CARTESIA_VOICE_ID = os.getenv("CARTESIA_VOICE_ID")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

dg = Deepgram(DEEPGRAM_API_KEY)

async def transcribe_audio(audio_data: bytes) -> str:
    try:
        response = await dg.transcription.prerecorded(
            {"buffer": audio_data, "mimetype": "audio/wav"},
            {"punctuate": True, "language": "en"},
        )
        return response["results"]["channels"][0]["alternatives"][0]["transcript"]
    except Exception as e:
        print("STT Error:", e)
        return ""

def generate_response(prompt: str) -> str:
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        res = requests.post(url, headers=headers, json=data)
        return res.json()['choices'][0]['message']['content']
    except Exception as e:
        print("LLM Error:", e)
        return "Sorry, I couldn't process that."

def text_to_speech(text: str) -> bytes:
    if ELEVENLABS_API_KEY:
        url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"
        headers = {
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
        }
        response = requests.post(url, headers=headers, json=data)
        return response.content
    elif CARTESIA_API_KEY:
        url = f"https://api.cartesia.ai/v1/speak"
        headers = {
            "Authorization": f"Bearer {CARTESIA_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "voice_id": CARTESIA_VOICE_ID
        }
        response = requests.post(url, headers=headers, json=data)
        return response.content
    else:
        raise Exception("No TTS provider configured.")

async def handle_audio_session():
    print("Starting voice session...")
    # Dummy flow for audio chunk processing
    while True:
        # Simulate: replace this with actual WebRTC or LiveKit audio stream capture
        user_audio = b''  # Replace with actual audio bytes
        transcript = await transcribe_audio(user_audio)
        print("User said:", transcript)

        response = generate_response(transcript)
        print("LLM:", response)

        speech_audio = text_to_speech(response)
        # Send `speech_audio` back to LiveKit track (to implement)
        # For now just simulating
        print("TTS generated", len(speech_audio), "bytes.")

        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(handle_audio_session())
