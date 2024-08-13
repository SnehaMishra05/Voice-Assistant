# Voice-Assistant

## Overview

This is a simple voice assistant built using Python. It can perform various tasks such as providing information about the user, telling jokes, opening specific websites, and playing songs. The assistant is activated by a specific voice command and can handle a range of commands to assist the user.

## Features

- **Voice Activation:** Responds to a specific activation phrase.
- **Voice Commands:**
  - **Name Inquiry:** Provides the assistant's name.
  - **Age Inquiry:** Tells the age of the assistant.
  - **Time Inquiry:** Provides the current time.
  - **Website Navigation:** Opens specified websites (YouTube, LinkedIn).
  - **Joke Telling:** Tells a random joke.
  - **Song Playback:** Plays a song from a specified directory.
- **Exit Command:** Terminates the assistant session.

## Technologies Used

- **Python:** Programming language used for the voice assistant.
- **Libraries:**
  - `pyttsx3` - Text-to-speech conversion.
  - `speech_recognition` - Speech-to-text conversion.
  - `webbrowser` - Open websites in the default browser.
  - `datetime` - Get the current time.
  - `pyjokes` - Fetch random jokes.
