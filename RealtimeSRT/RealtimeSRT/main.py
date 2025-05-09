import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎤 Real-time transcription started. Say 'stop' to exit.")

    while True:
        with mic as source:
            print("🦻 Listening for your speech...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(f"📄 You said: {text}")

            if "stop" in text.lower():
                print("🔴 'Stop' keyword detected. Ending session. Goodbye! 👋")
                break

        except sr.UnknownValueError:
            print("🤷 Could not understand audio.")
        except sr.RequestError as e:
            print(f"⚠ Could not request results; {e}")

if __name__ == "__main__":
    main()
