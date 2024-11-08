import streamlit as st
from datetime import datetime, timedelta
from plyer import notification
import threading
import time

# Function to send system notification
def send_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Patient Helper App',
        timeout=10  # Notification duration in seconds
    )

# Background reminder function for on-screen pop-up
def set_reminder(reminder_time, title, message, interval=30):
    def reminder():
        while True:
            current_time = datetime.now().time()
            if current_time.hour == reminder_time.hour and current_time.minute == reminder_time.minute:
                send_notification(title, message)
                
                # JavaScript alert for on-screen pop-up
                st.write(
                    f"""
                    <script>
                    alert("{title}: {message}");
                    </script>
                    """,
                    unsafe_allow_html=True
                )
                break
            time.sleep(interval)  # Check every `interval` seconds

    threading.Thread(target=reminder).start()

# Streamlit UI
st.title("Patient Reminder")

# Tabs for different reminder types
tab1, tab2, tab3 = st.tabs(["Medications", "Appointments", "Custom Reminders"])

# Medication Reminders
with tab1:
    st.header("Medication Reminders")
    med_name = st.text_input("Medication Name")
    med_dose = st.text_input("Dosage (e.g., 1 tablet, 2ml)")
    med_time = st.time_input("Reminder Time for Medication")
    add_med = st.button("Set Medication Reminder")

    if add_med:
        st.success(f"Medication reminder for {med_name} set at {med_time}!")
        set_reminder(med_time, f"Time for {med_name}", f"Take {med_dose}")

# Appointment Reminders
with tab2:
    st.header("Appointment Reminders")
    doc_name = st.text_input("Doctor's Name")
    app_date = st.date_input("Appointment Date")
    app_time = st.time_input("Appointment Time")
    add_app = st.button("Set Appointment Reminder")

    if add_app:
        st.success(f"Appointment with {doc_name} set for {app_date} at {app_time}!")
        
        # Custom appointment reminder check to include date and time
        def appointment_reminder():
            while True:
                now = datetime.now()
                if now.date() == app_date and now.time().hour == app_time.hour and now.time().minute == app_time.minute:
                    send_notification("Appointment Reminder", f"Visit {doc_name} today at {app_time}")
                    st.write(
                        f"""
                        <script>
                        alert("Appointment Reminder: Visit {doc_name} today at {app_time}");
                        </script>
                        """,
                        unsafe_allow_html=True
                    )
                    break
                time.sleep(60)  # Check every 60 seconds

        threading.Thread(target=appointment_reminder).start()

# Custom Reminders
with tab3:
    st.header("Custom Reminders")
    custom_message = st.text_input("Reminder Message")
    custom_time = st.time_input("Custom Reminder Time")
    add_custom = st.button("Set Custom Reminder")

    if add_custom:
        st.success(f"Custom reminder set for {custom_time} with message: {custom_message}")
        set_reminder(custom_time, "Custom Reminder", custom_message)
