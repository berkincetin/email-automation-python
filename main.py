import os
from dotenv import load_dotenv
from email_sender import (
    EmailSender,
)  # Import the EmailSender class from email_sender.py

# Load environment variables
load_dotenv()

# Email configuration
sender_email = os.getenv("SENDER_MAIL")
app_password = os.getenv("APP_PASSWORD")
recipient_email = os.getenv("RECIPIENT_MAIL")

# Create an EmailSender instance
email_sender = EmailSender(sender_email, app_password)

# Send 5 emails with a custom subject and body
email_sender.send_emails(recipient_email, "Custom Subject", "Custom body text", 5)
