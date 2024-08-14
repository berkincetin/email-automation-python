<a name="readme-top"></a>

# Email Sending Application

This project allows you to send emails using either a Python script or a Streamlit web application. It utilizes an SMTP server to handle email delivery and provides options for sending emails through a command-line script or a user-friendly web interface.

## Requirements

- Python 3.x
- `python-dotenv` library
- `streamlit` library

## Setup

### 1. Create a Google App Password

To use Gmail's SMTP server, you need to create a Google App Password:

1. **Enable 2-Step Verification**:
   - Go to your [Google Account Security page](https://myaccount.google.com/security).
   - Under "Signing in to Google," select "2-Step Verification" and follow the instructions to enable it.

2. **Generate an App Password**:
   - After enabling 2-Step Verification, return to the [Google App Passwords page](https://myaccount.google.com/apppasswords).
   - Choose "Mail" as the app and "Other" as the device, then generate a new password.
   - Copy this password; you'll use it as your SMTP password.

### 2. Create a `.env` File

Create a file named `.env` in the root directory of your project and add the following lines:

```python
SENDER_MAIL=your_email@gmail.com
APP_PASSWORD=your_app_password
RECIPIENT_MAIL=recipient_email@example.com
```

Replace `your_email@gmail.com`, `your_app_password`, and `recipient_email@example.com` with your actual email addresses and the generated app password.

### 3. Install Dependencies

Ensure you have the `python-dotenv` library installed. You can install it using pip:

```python
pip install python-dotenv
```
## Usage

### Option 1: Using `main.py`

To send emails using the `main.py` script:

1. **Create a `.env` file**:
   - In the root directory of your project, create a file named `.env`.

2. **Edit `main.py`**:
   - Open `main.py` and update the `send_emails` method call with your desired subject, body text, and the number of emails to send. The default line:

     ```python
     email_sender.send_emails(recipient_email, "Custom Subject", "Custom body text", 5)
     ```

     can be modified. For example, to set a custom subject, body, and send 10 emails, update it to:

     ```python
     email_sender.send_emails(recipient_email, "Your Subject Here", "Your body text here", 10)
     ```

3. **Run the Script**:

     Execute `main.py` by running:

     ```python
     python main.py
     ```

     This will send the specified number of emails with the given subject and body text to the recipient.

### Option 2: Using `email_sender_streamlit.py`
This script provides a web interface for sending emails using Streamlit.

Run the Streamlit application with:

```python
streamlit run email_sender_streamlit.py
```

You will be prompted to enter your email and password in the sidebar. Follow the instructions to generate a Google App Password if needed. Then, you can compose and send emails through the web interface.

![streamlit_interface](https://github.com/user-attachments/assets/1eeeafac-1205-491f-a020-f67c0e9c2ac8)



## Notes
- Make sure your .env file is included in your .gitignore to prevent exposing sensitive information.
- This script is configured for use with Gmail. For other email services, you may need to adjust the SMTP settings.

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
  <a href="#readme-top" style="text-decoration: none; color: blue; font-weight: bold;">
    ↑ Back to Top ↑
  </a>
</p>
