import streamlit as st
from email_sender import (
    EmailSender,
)  # Import the EmailSender class from email_sender.py

# Application title
st.title("Email Sending Application")

# Email and password input fields on the left
with st.sidebar:
    st.header("Login Information")
    sender_email = st.text_input(
        "Email", placeholder="Enter your email address", key="email_input"
    )
    app_password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your Google App Password",
        key="password_input",
    )
    st.markdown(
        """
        **Note:** To use this application, you need a Google App Password. 
        This is a one-time password that allows access to your Google account securely. 
        Follow these steps to generate one:
        
        1. Go to [Google Account Security](https://myaccount.google.com/security).
        2. Under "Signing in to Google," select "App passwords."
        3. Follow the instructions to create an App Password.
        """
    )

# Email composing area on the right
st.header("Compose Your Email")
recipient_emails = st.text_area(
    "Recipient Emails (comma-separated)",
    placeholder="Enter email addresses here, separated by commas",
    key="recipient_emails_input",
)
subject = st.text_input(
    "Subject", placeholder="Enter the subject of the email", key="subject_input"
)
message = st.text_area(
    "Message", placeholder="Enter the message body here", key="message_input"
)
count = st.slider("Number of Recipients", 1, 100, 1)

# Convert recipient_emails to a list of emails
recipient_email_list = [
    email.strip()
    for email in recipient_emails.split(",")
    if email.strip()  # Filter out empty strings
]

# Send button
if st.button("SEND"):
    # Check if any required fields are empty
    if (
        not sender_email
        or not app_password
        or not recipient_email_list
        or not subject
        or not message
    ):
        st.error("All fields must be filled out before sending the email.")
    else:
        try:
            # Create an EmailSender instance
            email_sender = EmailSender(sender_email, app_password)

            # Send emails
            total_sent = 0
            for recipient_email in recipient_email_list:
                email_sender.send_emails(recipient_email, subject, message, count)
                total_sent += 1

            # If successful
            st.success(
                f"Email sent to {total_sent} recipient(s) with subject '{subject}'! Total emails: {total_sent * count}"
            )
        except Exception as e:
            # If there's an error, display it
            st.error(f"An error occurred: {str(e)}")

# Developer info
st.sidebar.info(
    """
    Developed by [Harun Çetin](https://www.linkedin.com/in/harun-berkin-cetin/). 
    Check out [GitHub](https://github.com/berkincetin).
    """
)

# Spacer to push the content above higher
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

# Add GitHub and LinkedIn links aligned to the right at the bottom of the page
st.markdown("---")
st.markdown(
    """
    <div style="text-align: right;">
        <a href="https://github.com/berkincetin" target="_blank">GitHub</a> |
        <a href="https://www.linkedin.com/in/harun-berkin-cetin/" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)
