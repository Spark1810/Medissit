import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            speak_text("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            speak_text("Network error.")
            return None

# Main function for appointment booking
def book_appointment():
    speak_text("Welcome to the appointment booking assistant. What is your name?")
    name = recognize_speech()
    if not name:
        return

    speak_text(f"Hello {name}, which doctor would you like to book an appointment with?")
    doctor_name = recognize_speech()
    if not doctor_name:
        return

    speak_text("On which date would you like to book the appointment?")
    date = recognize_speech()
    if not date:
        return

    speak_text("At what time would you like the appointment?")
    time = recognize_speech()
    if not time:
        return

    # Confirm the appointment details
    speak_text(f"To confirm, you have an appointment with Dr. {doctor_name} on {date} at {time}. Is that correct?")
    confirmation = recognize_speech()

    if confirmation and "yes" in confirmation:
        speak_text("Your appointment has been successfully booked.")
        # Here, you would save the appointment details to a file or database.
        print(f"Appointment Details:\nName: {name}\nDoctor: Dr. {doctor_name}\nDate: {date}\nTime: {time}")
    else:
        speak_text("Okay, let's try again.")
        book_appointment()

# Run the appointment booking assistant
book_appointment()
