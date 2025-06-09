#  LLaMA 3.2 + TTS Interface (Gradio + pyttsx3 + Ollama)

This project provides a simple interactive **text-to-speech chatbot** interface using:

-  [LLaMA 3.2](https://ollama.com/library/llama3) via [Ollama](https://ollama.com/)
-  Local speech synthesis with `pyttsx3`
-  User-friendly web UI powered by [Gradio](https://www.gradio.app/)

---

##  Features

-  Send user input to **LLaMA 3.2**
-  Get a locally generated AI response (no cloud)
-  Speak the response aloud using `pyttsx3`
-  Web UI using Gradio (runs locally in your browser)

---

##  Requirements

Ensure you have the following installed:

### Python Packages

Install the required libraries:

```bash
pip install gradio pyttsx3
```
Usage
Run the script:

```bash
python app.py
```
Then open your browser to the Gradio interface (usually at `http://127.0.0.1:7860`).

Voice Settings
The script uses the "Zira" voice by default. You can change it in the code:

```python

if "Zira" in voice.name:  # Change to "David", "Mark", etc.
```

## Notes
- This tool works offline (after model download).

- Ideal for local voice assistants, accessibility tools, or educational projects.

- Ensure your system TTS voices are properly installed (especially on Linux or macOS).


