# AI_Voice_Agent

# 🧠 Real-Time Voice AI Agent using LiveKit

This project implements a real-time voice-based AI agent using:
- **LiveKit** for audio streaming (WebRTC)
- **Deepgram** for Speech-to-Text (STT)
- **LLM (Groq/OpenAI)** for generating text responses
- **ElevenLabs or Cartesia** for Text-to-Speech (TTS)

---

## 🚀 Features

- Real-time streaming using **LiveKit**
- Transcribe user voice with **Deepgram**
- Generate responses via **Groq LLM** or OpenAI
- Respond with natural-sounding speech using **ElevenLabs** or **Cartesia**
- Supports interruption handling and latency tracking

---

## 📦 Requirements

- Python 3.9+
- Valid API keys for:
  - LiveKit
  - Deepgram
  - ElevenLabs **OR** Cartesia
  - Groq **OR** OpenAI

---

## 🛠 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/livekit-voice-agent.git
cd livekit-voice-agent


2.Set up a virtual environment

--bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies

--bash
pip install -r requirements.txt

▶️ Running the Voice Agent
--bash
python agent.py

🧪 Testing Locally
You can test the STT + TTS + LLM pipeline independently by uploading a .wav file or using LiveKit's test session.

🧾 License
MIT License. Feel free to use and modify for your own purposes.
