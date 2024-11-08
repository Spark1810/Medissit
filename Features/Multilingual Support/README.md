# Language-Aware Assistant

## Overview
The **Language-Aware Assistant** is a voice-activated translation tool that detects the spoken language of the user, translates responses into the same language, and plays the response in audio format. This tool is designed to create an interactive and multilingual experience for users.

## Features
1. **Speech Recognition**: Captures and recognizes user input via microphone.
2. **Language Detection**: Automatically identifies the language of the user's spoken input.
3. **Translation and Response**: Translates responses into the detected language and provides audio playback of the translated text.
4. **Text-to-Speech**: Converts translated text into spoken language and plays it back to the user.

## Technologies Used
- **SpeechRecognition**: For capturing and processing spoken input.
- **googletrans**: For language detection and translation.
- **gTTS (Google Text-to-Speech)**: For generating spoken audio from text.
- **os**: For managing audio file playback.

## File Structure

- **translation.py**: The main script to run the language-aware assistant, listen for user input, detect language, translate responses, and output audio feedback.

## How It Works
### Listening for Input
1. The assistant waits for the user to speak, capturing the audio via a microphone.
2. The captured audio is then processed to convert speech to text.

### Language Detection
1. Once text is generated, the assistant detects the language using `googletrans`.
2. The language code is mapped to the corresponding language name.

### Response Translation
1. The assistant prepares a default response and translates it into the user’s detected language.
2. Using **gTTS**, the translated text is converted to speech and saved as an audio file.

### Playback
1. The saved audio file is played, responding in the user’s own language.

## Usage
1. **Run the Application**:
    ```bash
    python translation.py
    ```
2. **Interaction**:
    - Speak a phrase or ask a question when prompted.
    - The assistant will detect your language, translate its response, and reply in the same language.
    
## Requirements
- **Python Packages**:
    - `SpeechRecognition`
    - `googletrans`
    - `gTTS`
    - `os`
- **Microphone**: Required for capturing user input.

## License
This project is licensed under the MIT License.
