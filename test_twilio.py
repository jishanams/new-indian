import os
from twilio.rest import Client

from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')
TARGET_WHATSAPP_NUMBER = os.getenv('TARGET_WHATSAPP_NUMBER')

try:
    print("Initializing Twilio client...")
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    print("Sending message...")
    message = client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        body="Test message from Django backend!",
        to=TARGET_WHATSAPP_NUMBER
    )
    print(f"Success! Message SID: {message.sid}")
except Exception as e:
    print(f"Twilio Error: {e}")
