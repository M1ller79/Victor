<div align="center">

# 🗣️ Голосовой ассистент «Виктор» (v2.1)

**Ваш голосовой помощник, который работает с сервисами Яндекса и умеет запускать приложения на Windows офлайн.**

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Victor-181717?style=for-the-badge&logo=github)](https://github.com/M1ller79/Victor)

[🇷🇺 Русская версия](README.md) | [🇬🇧 English version](README-en.md)

</div>

---

## ✨ О проекте

**«Виктор»** - это голосовой ассистент, написанный на Python. Он способен распознавать речь, выполнять голосовые команды и отвечать голосом.

Проект создан для демонстрации навыков работы с **API**, **асинхронным программированием**, **обработкой звука** и **интеграцией с внешними сервисами**.

> «Виктор» - это не просто скрипт, а полноценный ассистент, который умеет слушать, понимать и действовать.

---

## 🚀 Возможности

- **🎙️ Распознавание речи (STT)** - на базе Vosk (офлайн-распознавание).
- **🔊 Синтез речи (TTS)** - на базе Silero (естественный голос).
- **🌐 Интеграция с API Яндекса** - погода, музыка, браузер.
- **🖥️ Офлайн-команды** - запуск приложений Windows по голосовой команде.
- **🧠 Нечёткое сравнение команд** - понимает команды даже с ошибками распознавания.
- **💾 Портативность** - может работать с USB-флешки без установки.

---

## 🛠️ Технологии

| Технология     |         Назначение        |
|----------------|---------------------------|
| **Python**     | Основной язык разработки  |
| **Vosk**       | Распознавание речи (STT)  |
| **Silero**     | Синтез речи (TTS)         |
| **fuzzywuzzy** | Нечёткое сравнение команд |
| **sounddevice**| Воспроизведение звука     |
| **requests**   | Работа с API Яндекса      |

---

## ⚡ Быстрый старт

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/M1ller79/Victor.git
cd Victor/Voice_Assistant_Victor_v2.1
```

### 2. Создайте виртуальное окружение и активируйте его
```
python -m venv .venv
```

# Windows:
```
.venv\Scripts\activate
```
# macOS/Linux:
```
source .venv/bin/activate
```

### 3. Установите зависимости
```
pip install -r requirements.txt
```

### 4. Скачайте модели

Vosk (STT): vosk-model-small-ru-0.22 https://alphacephei.com/vosk/models - распакуйте в models/small_voice_model/

Silero (TTS): скачайте model.pt из репозитория Silero https://github.com/snakers4/silero-models и положите в models/

### 5. Запустите ассистента
```
python src/main.py
```

### 6. Структура проекта

Voice_Assistant_Victor_v2.1/
├── src/
│   ├── config.py      # Конфигурация
│   ├── main.py        # Точка входа
│   ├── stt.py         # Распознавание речи
│   └── tts.py         # Синтез речи
├── models/            # Модели (не в репозитории)
├── requirements.txt   # Зависимости
└── README.md          # Этот файл

Автор: Александр Бабенко