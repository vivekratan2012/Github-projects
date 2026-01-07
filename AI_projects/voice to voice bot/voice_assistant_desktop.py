import pyttsx3
import ollama
import speech_recognition as sr
import sys
import tkinter as tk
from tkinter import scrolledtext
import threading
import platform

# =========================
# Language Hints for TTS
# =========================

LANGUAGES = {
    "English": "english",
    "German": "german",
    "French": "french",
    "Polish": "polish",
    "Hindi": "hindi"
}

# =========================
# Text-to-Speech
# =========================

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def set_voice(language_hint):
    for voice in engine.getProperty("voices"):
        if language_hint in voice.name.lower() or language_hint in voice.id.lower():
            engine.setProperty("voice", voice.id)
            return

def speak(text, language_hint):
    set_voice(language_hint)
    engine.say(text)
    engine.runAndWait()

# =========================
# Speech Recognition (Push-to-Talk)
# =========================

def beep():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 200)
    else:
        print("\a")  # macOS / Linux

def listen(recognizer, microphone, gui):
    speak("Press the button to speak.", "english")
    gui.update_text("Assistant: Press the button to speak.")
    gui.update_button_text("Listening...")

    beep()
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        audio = recognizer.listen(source)

    try:
        user_text = recognizer.recognize_google(audio)
        gui.update_text(f"You: {user_text}")
        process_input(user_text, gui)
    except:
        gui.update_text("Assistant: Sorry, I did not catch that.")
        gui.update_button_text("Press to Speak")

def process_input(user_text, gui):
    if not user_text:
        gui.update_text("Assistant: I did not understand.")
        return

    # Stop assistant command
    if user_text.lower() in ["stop assistant", "exit", "quit"]:
        speak("Goodbye.", "english")
        gui.update_text("Assistant: Goodbye!")
        sys.exit()

    detected_language = detect_language(user_text)
    if detected_language not in LANGUAGES:
        detected_language = "English"

    language_hint = LANGUAGES[detected_language]

    # Include short memory
    prompt = (
        "You are a helpful assistant.\n"
        f"Previous question: {gui.last_question}\n"
        f"Reply ONLY in {detected_language}.\n\n"
        f"User: {user_text}"
    )

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response["message"]["content"].strip()
    speak(reply, language_hint)
    gui.update_text(f"Assistant: {reply}")
    gui.last_question = user_text

# =========================
# Language Detection
# =========================

def detect_language(text):
    prompt = (
        "Detect the language of the following text. "
        "Reply with ONLY one word: English, German, French, Polish, or Hindi.\n\n"
        f"Text: {text}"
    )
    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"].strip()

# =========================
# GUI Class (Tkinter)
# =========================

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry("500x400")
        self.last_question = ""
        
        # Text Box for displaying conversation
        self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=15)
        self.text_box.grid(row=0, column=0, padx=10, pady=10)
        
        # Button for starting voice recognition
        self.listen_button = tk.Button(self.root, text="Press to Speak", width=20, height=2, command=self.start_listening)
        self.listen_button.grid(row=1, column=0, pady=20)
        
    def update_text(self, text):
        self.text_box.insert(tk.END, f"{text}\n")
        self.text_box.yview(tk.END)
    
    def update_button_text(self, text):
        self.listen_button.config(text=text)
    
    def start_listening(self):
        # Start the listening process in a new thread to avoid freezing the UI
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()
        threading.Thread(target=listen, args=(recognizer, microphone, self)).start()

# =========================
# Main Function
# =========================

def main():
    root = tk.Tk()
    gui = VoiceAssistantGUI(root)
    root.mainloop()

# =========================
# Entry Point
# =========================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
