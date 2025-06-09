import gradio as gr
import pyttsx3
import ollama
import speech_recognition as sr

# Text-to-Speech (TTS) Function
def speak_text(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"TTS error: {e}")
    return text

# Speech Recognition using Google (Free)
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError as e:
        return f"Speech Recognition error: {e}"

# Main Function: Listen → Translate → Speak
def translate_speech(target_language):
    english_text = recognize_speech()

    if "Sorry" in english_text or "error" in english_text.lower():
        return english_text

    prompt = f"Translate this English sentence into {target_language}:\n\n'{english_text}'"
    try:
        response = ollama.chat(
            model="llama3.2:latest",
            messages=[{"role": "user", "content": prompt}]
        )
        translated_text = response['message']['content'].strip()

        speak_text(translated_text)

        return f"Original (English): {english_text}\n\nTranslated ({target_language}): {translated_text}"
    except Exception as e:
        return f"Translation error: {e}"

# Gradio UI
interface = gr.Interface(
    fn=translate_speech,
    inputs=gr.Dropdown(["Spanish", "French", "German", "Hindi", "Chinese"], label="Translate To"),
    outputs="text",
    title="Speech Translation Assistant",
    description="Speak in English. This application translates your speech to a selected language and speaks the result using local text-to-speech."
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
