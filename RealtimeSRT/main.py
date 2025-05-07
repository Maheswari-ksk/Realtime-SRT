import openai
import speech_recognition as sr

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Start the real-time interaction loop
while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Transcribe the audio using Whisper
        transcription = openai.Audio.transcribe(
            model="whisper-1",
            file=audio
        )

        user_input = transcription['text']
        print(f"User: {user_input}")

        # Generate a response using GPT-4o
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_input}]
        )

        assistant_reply = response['choices'][0]['message']['content']
        print(f"Assistant: {assistant_reply}")

    except Exception as e:
        print(f"Error: {e}")