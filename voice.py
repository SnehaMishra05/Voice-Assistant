import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def listen_for_command():
    """Listen for a command from the user and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble connecting to the service.")
            return None

def speak(text):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('voice', engine.getProperty('voices')[0].id)  # Set voice
    engine.say(text)
    engine.runAndWait()

def handle_command(command):
    """Process the command and perform the corresponding action."""
    if "your name" in command:
        speak("My name is Sneha")
    elif "how old are you" in command:
        speak("I am 21 years old")
    elif 'what time is it' in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")
    elif 'youtube' in command:
        webbrowser.open("https://www.youtube.com/")
    elif 'linkedin' in command:
        webbrowser.open("https://www.linkedin.com/in/sneha-mishra-791352276/")
    elif "joke" in command:
        joke = pyjokes.get_joke(language="en", category="neutral")
        print(joke)
        speak(joke)
    elif 'play song' in command:
        play_song()
    elif "exit" in command:
        speak("Thank you. Goodbye!")
        return True
    return False

def play_song():
    """Play a song from a predefined directory."""
    song_directory = "C:\\Users\\KIIT\\Desktop\\Projects\\python"
    try:
        songs = os.listdir(song_directory)
        if songs:
            print(f"Playing: {songs[0]}")
            os.startfile(os.path.join(song_directory, songs[0]))
        else:
            speak("No songs found in the directory.")
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred while trying to play the song.")

def main():
    """Main function to run the voice assistant."""
    print("Say 'Hey Sneha' to activate the assistant.")
    while True:
        command = listen_for_command()
        if command and "hey sneha" in command:
            while True:
                command = listen_for_command()
                if command and handle_command(command):
                    break
                time.sleep(2)
        else:
            print("Waiting for activation command...")

if __name__ == '__main__':
    main()