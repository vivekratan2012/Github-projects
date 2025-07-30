import gradio as gr
import pyttsx3
import ollama  # Ensure Ollama is installed and running with llama3.2

# Function to convert text to speech using a fresh engine each time
def speak_text(text):
    try:
        # Initialize the pyttsx3 engine inside the function
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Optional: Adjust the speech rate

        # Set the preferred voice (change "Zira" to "David", "Mark", etc. as needed)
        for voice in engine.getProperty('voices'):
            if "Zira" in voice.name:
                engine.setProperty('voice', voice.id)
                break

        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print(f"TTS error: {e}")
    return text

# Function to process input using Llama 3.2 and speak the response
def process_and_speak(input_text):
    try:
        # Query the local LLM using Ollama
        response = ollama.chat(
            model="llama3.2:latest",
            messages=[{"role": "user", "content": input_text}]
        )

        # Extract model's response text
        response_text = response['message']['content']

        # Speak the response
        speak_text(response_text)

    except Exception as e:
        response_text = f"Error communicating with the model: {str(e)}"

    return response_text

# Create the Gradio interface
interface = gr.Interface(
    fn=process_and_speak,
    inputs=gr.Textbox(lines=2, placeholder="Enter your text here..."),
    outputs="text",
    title="Text to Speech with Local Llama 3.2 and pyttsx3",
    description="Type something and Llama 3.2 will respond and speak it using your selected voice.",
    live=False
)

# Launch the Gradio interface
if __name__ == "__main__":
    interface.launch()
