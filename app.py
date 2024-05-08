import streamlit as st
import assemblyai as aai
from gtts import gTTS
import os

# Set your AssemblyAI API key
aai.settings.api_key = "0be31a79fe8d46cf88181e5948ba71b4"

def main():
    # Title for your Streamlit app
    st.title("Audio Transcription and Text-to-Speech App")

    # File uploader to upload an audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav"])

    # Text input for text-to-speech conversion
    text_input = st.text_input("Enter text for Text-to-Speech")

    if uploaded_file is not None:
        # Initialize the transcriber
        transcriber = aai.Transcriber()

        # Transcribe the uploaded audio file
        transcript = transcriber.transcribe(uploaded_file)

        # Display the transcription result
        st.header("Transcription Result:")
        st.write(transcript.text)

    if text_input:
        # Convert text to speech
        tts = gTTS(text=text_input, lang='en')

        # Save the speech to a temporary file
        tts_file = "temp_output.mp3"
        tts.save(tts_file)

        # Display the audio player for the speech
        st.audio(tts_file, format='audio/mp3')

        # Remove the temporary file
        os.remove(tts_file)

if __name__ == "__main__":
    main()

