# Voice Bot using Gemma3:4b, Ollama, and Python

Welcome to the Voice Bot repository! This project leverages the **Gemma3:4b** language model (via Ollama), along with `pyttsx3` for text-to-speech and `speech_recognition` for speech-to-text, to create a conversational voice bot — all running locally on your machine.

---

## Features

- **Conversational AI**: Uses the powerful Gemma3:4b model for natural language understanding and response generation.
- **Speech-to-Text**: Converts your spoken words to text using `speech_recognition`.
- **Text-to-Speech**: Replies are spoken back to you using `pyttsx3`.
- **Runs Locally**: No cloud services required — your data stays on your machine.

---

## Prerequisites

- Python 3.8 or above
- [Ollama](https://ollama.com/) (for running Gemma3:4b locally)
- Basic microphone and speaker setup

---

## Getting Started

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up Ollama and Gemma3:4b

Run the setup script to install and configure Ollama and download the Gemma3:4b model:

```bash
python setup.py
```

> **Note:** The script will guide you through installing Ollama (if not already installed) and fetching the Gemma3:4b model.

### 3. Start the Voice Bot

```bash
python app.py
```

---

## Usage

* Speak into your microphone when prompted.
* The bot will transcribe your speech, generate a response using Gemma3:4b, and speak the reply back to you.
* To stop the bot, use `Ctrl+C` in the terminal.

---

## File Structure

```
voice-bot-gemma3/
│
├── app.py              # Main application entry point
├── setup.py            # Ollama and Gemma3:4b setup script
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── ...
```

---

## Troubleshooting

* **Microphone Not Detected:** Ensure your system microphone is enabled and accessible.
* **Ollama Issues:** Refer to [Ollama's documentation](https://ollama.com/docs) for troubleshooting installation or model loading problems.
* **Dependency Errors:** Double-check you installed all requirements with the correct Python version.

---

## Acknowledgements

* [Ollama](https://ollama.com/)
* [pyttsx3](https://pyttsx3.readthedocs.io/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

---
