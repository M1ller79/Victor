<div align="center">

# 🗣️ Voice Assistant "Victor" (v2.1)

**A Python voice assistant: offline speech recognition, voice responses, and command execution.**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Victor-181717?style=for-the-badge&logo=github)](https://github.com/M1ller79/Victor)

</div>

---

## ✨ About the Project

**"Victor"** is a voice assistant written in Python. It recognizes speech from a microphone, executes voice commands, and responds with synthesized speech.

The project demonstrates skills in **audio processing**, **speech recognition and synthesis**, **fuzzy string matching**, and **integration with external services** (weather, music, browser).

> "Victor" is not just a script — it's a full-fledged assistant that can listen, understand, and act.

---

## 🚀 Features

- **🎙️ Speech Recognition (STT)** — powered by **Vosk** (offline, no internet required).
- **🔊 Speech Synthesis (TTS)** — powered by **Silero** (natural voice, model `v3_1_ru`).
- **🧠 Fuzzy Command Matching** — `fuzzywuzzy` (`fuzz.ratio`) identifies commands even with recognition errors.
- **🔢 Number-to-Text Conversion** — `num2t4ru` is used to announce the time.
- **🌐 Commands:**
  - `music` — opens Yandex.Music in Chrome.
  - `weather` — opens Yandex.Weather.
  - `browser` — opens Yandex in Chrome.
  - `time` — announces the current time (with number-to-text conversion).
  - `joke` — tells a random joke from a list.
  - `list of commands` — lists what the assistant can do.
  - `author` — names the creator.
  - `thank you` — responds with gratitude.
- **💾 Portability** — can run from a USB flash drive (models are loaded locally).

---

## 🛠️ Technologies

| Technology | Purpose |
|------------|---------|
| **Python** | Main programming language |
| **Vosk** | Speech recognition (STT, offline) |
| **Silero** | Speech synthesis (TTS) |
| **fuzzywuzzy** | Fuzzy command matching |
| **sounddevice** | Audio recording and playback |
| **num2t4ru** | Number-to-text conversion |
| **torch** | Loading and running the Silero model |

---

## ⚡ Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/M1ller79/Victor.git
cd Victor/Voice_Assistant_Victor_v2.1
```

### 2. Create and activate a virtual environment
```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Download models
Vosk (STT): vosk-model-small-ru-0.22 — unzip into models/small_voice_model/

Silero (TTS): https://github.com/snakers4/silero-models downloaded automatically on first run via torch.hub (or download model.pt manually and place it in the project root).

### 5. Run the assistant
```
python src/main.py
```

After launch, "Victor" will greet you and start listening. Say "Victor" or "Hello" to activate a command.

Author: Alexander Babenko