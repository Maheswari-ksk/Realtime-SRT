' ===================================================================================
'                                 Real-Time Speech-to-Text Transcription
' ===================================================================================
'
' # Overview
' This project enables real-time transcription of speech into text using the 
' SpeechRecognition library. It listens to your microphone, converts your speech 
' into text, and saves the transcriptions into a text file. The program continues 
' transcribing until the word "stop" is spoken, after which it ends the session. 
' This can be useful for transcription services, accessibility tools, or real-time 
' captioning.
'
' # Technologies Used
' - **Python 3.x** (Tested with Python 3.7+)
' - **SpeechRecognition**: For recognizing speech and converting it to text.
' - **PyAudio**: To access the microphone and capture audio input.
' - **Google Web Speech API**: For processing the speech data and converting it into text.
'
' # Setup Instructions
'
' ## 1. Install Dependencies
' Ensure Python is installed on your machine. Then, install the required libraries 
' using the following command:
' 
' ```bash
' pip install SpeechRecognition pyaudio
' ```
'
' ## 2. Download the Script
' Download or copy the Python script `realtime_transcription.py` into your working 
' directory. You can get the script by clicking the link below:
' 
' [Download realtime_transcription.py](#)  ' Replace with actual link if hosted online
'
' ## 3. Run the Script
' To start the transcription process, navigate to the directory where the script 
' is saved and execute the following command:
' 
' ```bash
' python realtime_transcription.py
' ```
'
' The script will begin recording and transcribing your speech in real-time. 
' The transcriptions will be saved to a file named `project2_transcripts.txt`.
'
' ## 4. Stopping the Transcription
' You can stop the transcription session by saying **"stop"**. The script will detect 
' the keyword and automatically stop recording. You can also stop the script manually 
' at any time by pressing **Ctrl + C** in the terminal.
'
' # How It Works
' 1. **Listening to Microphone**: 
'    The script uses the **SpeechRecognition** library to capture audio from the 
'    microphone. It listens continuously and recognizes speech as you talk.
'
' 2. **Speech-to-Text**: 
'    The audio is processed using the **Google Web Speech API**, which converts the 
'    speech into text. The text is then displayed in the terminal.
'
' 3. **Saving Transcriptions**: 
'    Each recognized speech is printed to the terminal and saved into the 
'    `project2_transcripts.txt` file, allowing you to keep a record of the transcription.
'
' 4. **Stop Command**: 
'    If the script detects the word **"stop"** in your speech, it will automatically 
'    stop the transcription session and exit the loop.
'
' ===================================================================================
