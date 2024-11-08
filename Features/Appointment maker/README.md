# NIH RAG Chatbot & Voice-Activated Appointment Maker

## Overview
This project contains two primary components:
1. **NIH RAG Chatbot**: A chatbot using Streamlit, LangChain, and Chroma for answering questions based on NIH ODS Fact Sheets.
2. **Voice-Activated Appointment Maker**: A voice-interactive assistant that assists users in booking appointments using speech recognition and text-to-speech functionality.

## Features

### NIH RAG Chatbot
- **Interactive Chat Interface**: Provides a responsive chat UI where users can query the bot.
- **RAG Model**: Combines OpenAI’s GPT-3.5 with NIH ODS Fact Sheets to generate medically reliable responses.
- **Prompt-based Instruction**: Ensures answers are provided in a concise, friendly manner, suitable for healthcare contexts.
- **Reliable Data Source**: Uses up-to-date data from the NIH API for accurate information retrieval.

### Voice-Activated Appointment Maker
The voice-activated appointment maker uses `speech_recognition` and `pyttsx3` libraries to handle speech-to-text and text-to-speech interactions, making it user-friendly for those preferring hands-free interaction.

#### Key Features:
- **Speech Recognition**: Recognizes and processes voice inputs for a smooth user experience.
- **Text-to-Speech Output**: Provides verbal responses for each prompt, creating an interactive, hands-free booking process.
- **Personalized Assistance**:
  - **Name Collection**: Prompts users for their name to personalize the booking experience.
  - **Doctor Selection**: Asks users for the preferred doctor's name, allowing customization of appointment details.
  - **Date & Time**: Collects the desired date and time for the appointment to ensure accuracy.
  - **Confirmation**: Confirms appointment details before finalizing, allowing the user to make changes if needed.

#### Example Usage
When the assistant is run:
1. It welcomes the user and asks for their name.
2. It then inquires about the doctor, date, and time for the appointment.
3. Finally, it confirms the details and saves the information if the user agrees.

## Technologies Used
- **Streamlit**: For the chatbot interface.
- **LangChain & Chroma**: For document retrieval and vector-based querying in the NIH Chatbot.
- **OpenAI GPT-3.5**: Generates responses based on retrieved data.
- **SpeechRecognition**: Recognizes spoken language for the appointment maker.
- **pyttsx3**: Provides text-to-speech functionality to respond verbally.

## Setup Instructions

### Prerequisites
- Python 3.7 or higher
- Required packages (listed in `requirements.txt`)
- OpenAI API key for the chatbot

### Installation
1. Clone the repository to your local machine:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have an OpenAI API key for the NIH RAG Chatbot.

### Running Each Application

1. **Run the NIH RAG Chatbot**
   ```bash
   python chunking.py   # To process NIH data
   streamlit run app.py  # To launch the chatbot interface
   ```

2. **Run the Appointment Maker**
   ```bash
   python appointment_maker.py
   ```
   This script will launch the voice-activated assistant to guide users through booking an appointment.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
