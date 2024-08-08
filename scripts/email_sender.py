import smtplib
from email.mime.text import MIMEText
from contextlib import contextmanager
from timeit import default_timer as timer


class EmailSender:
    def __init__(self, sender, password, smtp_host="smtp.gmail.com", smtp_port=587):
        """
        Initialize the EmailSender with SMTP server details and credentials.

        :param sender: Email address of the sender
        :param password: Password for the sender's email account
        :param smtp_host: SMTP server host (default is "smtp.gmail.com")
        :param smtp_port: SMTP server port (default is 587)
        """
        self.sender = sender
        self.password = password
        self.smtp_host = smtp_host
        self.smtp_port = smtp_port

    @contextmanager
    def logined(self):
        """
        Context manager for establishing and managing the SMTP connection.

        Yields:
            SMTP object: The SMTP server connection object
        """
        start = timer()  # Start timing
        smtp_server = smtplib.SMTP(self.smtp_host, self.smtp_port, timeout=10)
        try:
            smtp_server.starttls()
            print("SMTP setup took (%.2f seconds)" % (timer() - start,))
            start = timer()
            smtp_server.login(self.sender, self.password)
            print("Login took %.2f seconds" % (timer() - start,))
            start = timer()
            yield smtp_server
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            print("Operations with smtp_server took %.2f seconds" % (timer() - start,))
            start = timer()
            smtp_server.quit()
            print("Quitting took %.2f seconds" % (timer() - start,))

    def send_emails(
        self, recipient, subject="Default Subject", body="Default body text", count=1
    ):
        """
        Sends emails using the provided SMTP configuration.

        :param recipient: Email address of the recipient
        :param subject: Subject line of the email (default is "Default Subject")
        :param body: Body text of the email (default is "Default body text")
        :param count: Number of emails to send (default is 1)
        """
        with self.logined() as smtp_server:
            for i in range(count):
                msg = MIMEText(body)
                msg["Subject"] = subject
                msg["From"] = self.sender
                msg["To"] = recipient
                smtp_server.send_message(msg)
            print("Email(s) sent successfully.")
