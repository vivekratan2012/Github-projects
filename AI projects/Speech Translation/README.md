# Speech Translation Assistant

This project is a local **speech-to-speech translator** powered by:

-  [LLaMA 3.2](https://ollama.com/library/llama3) via [Ollama](https://ollama.com/)
-  Offline **text-to-speech** using `pyttsx3`
-  **Speech recognition** using Google API (free tier)
-  A web UI via [Gradio](https://gradio.app)

---

##  Features

-  Speak in **English**
-  Get translations in **Spanish**, **French**, **German**, **Hindi**, or **Chinese**
-  Hear the translation spoken aloud
-  Runs **100% locally** (except for Google Speech API)

---

##  Requirements

###  Python Packages

Install dependencies:

```bash
pip install gradio pyttsx3 SpeechRecognition pyaudio
```
## Ollama + LLaMA 3.2
Install and run Ollama locally:

```bash
ollama pull llama3.2
```
Make sure Ollama is running in the background:

```bash
ollama run llama3.2
```
## Usage
Start the app:

```bash
python app.py
```

Then speak when prompted! The interface will:

- Recognize your speech (English)

- Translate it to the selected language

Speak the translated sentence back to you

## Languages Supported
Currently supports translation from English to:

- Spanish 🇪🇸

- French 🇫🇷

- German 🇩🇪

- Hindi 🇮🇳

- Chinese 🇨🇳

You can add more by editing the gr.Dropdown() options.

## Voice Output Notes
- pyttsx3 uses your system's TTS engine.

- On Windows, it uses SAPI5 (e.g., voices like David, Zira).

- On macOS, it uses NSSpeechSynthesizer (e.g., Samantha, Alex).

- On Linux, it typically uses eSpeak (can be customized).

## Privacy & Connectivity
- Your voice is processed locally, except for Google’s free speech recognition.

- For 100% offline, consider replacing Google API with vosk, whisper, or similar.