from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv()

# Load environment variables from .env file
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Replace with your Flow SID
FLOW_SID = "FWXXXXXXXXXXXXXXXXX"

studio_url = f"https://studio.twilio.com/v2/Flows/{FLOW_SID}/Executions"

# Kontaktdaten Laden
def load_contacts(file_path='contacts.txt'):
    with open(file_path, 'r') as f:
        numbers = [line.strip() for line in f if line.strip()]
    return numbers

# Kontaktdaten Test Laden
def load_contacts_test(file_path='contacts_test.txt'):
    with open(file_path, 'r') as f:
        numbers = [line.strip() for line in f if line.strip()]
    return numbers

# POST zum SERVER (TEST)
@app.route("/test_call", methods=['POST'])
def test_call():

    numbers_to_alert = load_contacts_test()

    for number in numbers_to_alert:
        response = requests.post(  # Corrected from request.post to requests.post
            studio_url,
            auth=(ACCOUNT_SID, AUTH_TOKEN),
            data={
                'To': number,
                'From': TWILIO_NUMBER,  # Replace with your Twilio phone number
                'Parameters': '{"campaign":"muttertag2025"}'  # Optional: Parameter für Studio
            }
        )
        if response.status_code == 201:
            print(f'✅ Anruf gestartet: {number}')
        else:
            print(f'❌ Fehler bei {number}: {response.status_code} - {response.text}')

    return "Anrufe wurden gestartet." 

# POST zum SERVER
@app.route("/incoming_call", methods=['POST'])
def incoming_call():

    numbers_to_alert = load_contacts()

    for number in numbers_to_alert:
        response = requests.post(  # Corrected from request.post to requests.post
            studio_url,
            auth=(ACCOUNT_SID, AUTH_TOKEN),
            data={
                'To': number,
                'From': TWILIO_NUMBER,  # Replace with your Twilio phone number
                'Parameters': '{"campaign":"muttertag2025"}'  # Optional: Parameter für Studio
            }
        )
        if response.status_code == 201:
            print(f'✅ Anruf gestartet: {number}')
        else:
            print(f'❌ Fehler bei {number}: {response.status_code} - {response.text}')

    return "Anrufe wurden gestartet."


if __name__ == "__main__":
    app.run(port=8830, debug=True)