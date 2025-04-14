# --------------------------------------------------
# Prerequisites - What you MUST do BEFORE running:
# --------------------------------------------------
# 1. Install Python: Make sure you have Python installed on your system.
#    You can download it from python.org if you don't.
# 2. Install pyttsx3: Open your terminal or command prompt (or PowerShell) and run:
#    pip install pyttsx3
# 3. Ensure a Text-to-Speech engine is installed on your system:
#    - Windows: SAPI5 is usually pre-installed.
#    - macOS: NSSpeech is built-in.
#    - Linux: Install Espeak (e.g., 'sudo apt-get install espeak' on Debian/Ubuntu).
# --------------------------------------------------

import pyttsx3
import os
import sys
import time  # For potential delays

def speak(text, rate=150, volume=1.0):
    """Speaks the given text using the pyttsx3 engine.

    Args:
        text (str): The text to be spoken.
        rate (int, optional): The speaking rate (words per minute). Defaults to 150.
        volume (float, optional): The volume (0.0 to 1.0). Defaults to 1.0.
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        return True
    except Exception as e:
        print(f"An error occurred during speech: {e}")
        return False

def save_to_file(text, filename="mufakosi_welcome.wav", rate=150, volume=1.0):
    """Saves the spoken text to an audio file using pyttsx3.

    Args:
        text (str): The text to be spoken and saved.
        filename (str, optional): The name of the output audio file. Defaults to "mufakosi_welcome.wav".
        rate (int, optional): The speaking rate (words per minute). Defaults to 150.
        volume (float, optional): The volume (0.0 to 1.0). Defaults to 1.0.
    """
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', rate)
        engine.setProperty('volume', volume)
        engine.save_to_file(text, filename)
        engine.runAndWait()
        engine.stop()
        print(f"Audio successfully saved as '{filename}'")
        return filename
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")
        return None

def play_audio(filepath):
    """Plays the audio file using the system's default player.

    Args:
        filepath (str): The path to the audio file.
    """
    if filepath and os.path.exists(filepath):
        print(f"Attempting to play '{filepath}'...")
        if sys.platform == "win32":
            os.system(f'start "" "{filepath}"')
        elif sys.platform == "darwin":
            os.system(f'open "{filepath}"')
        elif sys.platform.startswith("linux"):
            os.system(f'xdg-open "{filepath}"')
        else:
            print("Unsupported operating system for playback.")
    else:
        print(f"Error: Audio file '{filepath}' not found.")

if __name__ == "__main__":
    text_to_speak = "Welcome to Mufakosi Uncommon Hub"
    speech_rate = 150  # Adjust speaking speed
    speech_volume = 1.0 # Adjust volume (0.0 to 1.0)
    output_file = "mufakosi_welcome.wav"

    print("Starting Text-to-Speech conversion using pyttsx3...")

    # Speak the text aloud
    if speak(text_to_speak, rate=speech_rate, volume=speech_volume):
        print("Text spoken successfully.")
        time.sleep(1) # Give a short pause before saving

    # Save the text to an audio file
    saved_file = save_to_file(text_to_speak, filename=output_file, rate=speech_rate, volume=speech_volume)
    if saved_file:
        time.sleep(1) # Give a short pause before playing

        # Play the saved audio file
        play_audio(saved_file)

    print("Script finished. Welcome to Mufakosi Uncommon Hub!")
    