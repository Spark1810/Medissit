import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

# Function to listen to the user
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Network error.")
            return None

# Function to detect language
def detect_language(text):
    detected = translator.detect(text)
    language_code = detected.lang
    language_name = LANGUAGES.get(language_code, "unknown")
    print(f"Detected language: {language_name}")
    return language_code

# Function to translate and respond in the user's language
def respond_in_user_language(response_text, language_code):
    translated_text = translator.translate(response_text, dest=language_code).text
    print(f"Translated response: {translated_text}")
    
    # Convert text to speech in user's language
    tts = gTTS(text=translated_text, lang=language_code)
    tts.save("response.mp3")
    os.system("start response.mp3" if os.name == "nt" else "mpg123 response.mp3")

# Main function
def language_aware_assistant():
    print("Say something to the assistant.")
    user_input = recognize_speech()
    
    if user_input:
        user_language = detect_language(user_input)
        response_text = "Hello! How can I help you today?"
        
        # Respond in the user's detected language
        respond_in_user_language(response_text, user_language)

# Run the assistant
language_aware_assistant()
