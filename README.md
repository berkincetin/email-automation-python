# Email Sender Python Script

This Python script allows you to send multiple emails using an SMTP server. It uses a context manager to handle the SMTP connection and timing, and provides a class-based approach for sending emails.

## Requirements

- Python 3.x
- `python-dotenv` library
- `smtplib` (standard library)
- `email` (standard library)

## Setup

### 1. Create a Google App Password

To use Gmail's SMTP server, you need to create an App Password:

1. **Enable 2-Step Verification**:
   - Go to your [Google Account Security page](https://myaccount.google.com/security).
   - Under "Signing in to Google," select "2-Step Verification" and follow the instructions to enable it.

2. **Generate an App Password**:
   - After enabling 2-Step Verification, return to the [Google App Passwords page](https://myaccount.google.com/apppasswords).
   - Choose "Mail" as the app and "Other" as the device, then generate a new password.
   - Copy this password; you'll use it as your SMTP password.

### 2. Create a `.env` File

Create a file named `.env` in the root directory of your project and add the following lines:

```env
SENDER_MAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECIPIENT_MAIL=recipient_email@example.com
```

Replace `your_email@gmail.com`, `your_app_password`, and `recipient_email@example.com` with your actual email addresses and the generated app password.

### 3. Install Dependencies

Ensure you have the `python-dotenv` library installed. You can install it using pip:

```
pip install python-dotenv
```
## Usage

### 1. `email_sender.py`

This file contains the `EmailSender` class, which handles the SMTP connection and email sending. It provides methods to manage the connection and send emails.

### 2. `main.py`

This file uses the `EmailSender` class to send emails. You can customize the subject, body, and number of emails to be sent.

Create a Python script (e.g., `main.py`) with the following content:

```python
import os
from dotenv import load_dotenv
from email_sender import EmailSender  # Import the EmailSender class from email_sender.py

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
```

Replace `your_script_name` with the name of your Python script file that contains the `EmailSender` class.

## Notes
- Make sure your .env file is included in your .gitignore to prevent exposing sensitive information.
- This script is configured for use with Gmail. For other email services, you may need to adjust the SMTP settings.#email-automation-python
