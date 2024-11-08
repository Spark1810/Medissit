# Patient Helper App - Reminders

## Overview
The **Patient Helper App** provides a streamlined way for patients to set reminders for medications, appointments, and custom notifications. This app uses system notifications and JavaScript alerts to remind users, ensuring that important tasks aren’t forgotten.

## Features
1. **Medication Reminders**: Sets reminders for taking medications at specified times, with dosage details.
2. **Appointment Reminders**: Sets reminders for doctor appointments on a specific date and time.
3. **Custom Reminders**: Allows users to create any type of reminder with a custom message.

## Technologies Used
- **Streamlit**: For creating an easy-to-use, interactive interface.
- **plyer**: For sending system notifications.
- **JavaScript Alerts**: For on-screen pop-up notifications.
- **Threading**: To handle background tasks for reminders without interrupting the Streamlit interface.

## File Structure

- **remainders.py**: Main application file to set up reminders and notifications.
  
## How It Works
### Medication Reminder
1. Enter the medication name, dosage, and reminder time.
2. The app will notify the user at the specified time via system notification and on-screen pop-up.
  
### Appointment Reminder
1. Input the doctor's name, appointment date, and time.
2. The app checks for the date and time match and sends a notification for the appointment along with a JavaScript alert.

### Custom Reminder
1. Enter any reminder message and set a specific time.
2. The app will notify the user at the given time with a personalized message.

## Usage
1. **Run the Application**:
    ```bash
    streamlit run remainders.py
    ```

2. **Setting Reminders**:
    - Go to the **Medication** tab for medication reminders.
    - Use the **Appointments** tab to set doctor appointment reminders.
    - Access the **Custom Reminders** tab for other personalized notifications.

3. The app will send a system notification and pop-up reminder when the time arrives for each set reminder.

## License
This project is licensed under the MIT License.
