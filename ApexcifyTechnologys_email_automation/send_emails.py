import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Sender credentials (replace with your Gmail and app password)
sender_email = "ayeshashabbir053@gmail.com"
sender_password = "rerf qyer qens vcas"

# List of 20 recipient emails (replace with real ones for testing)
recipients = [
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
    "ayeshashabbir053@gmail.com",
]

# Email content
subject = "Automated Email"
body = """Dear Recipient,

This is a sample paragraph for the email automation system. It demonstrates sending the same message to multiple recipients simultaneously.

Thank you for your attention.

Best regards,
Email Automation System
"""

# Function to send email
def send_email(recipient):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient, text)
        server.quit()
        print(f"Email sent to {recipient}")
    except Exception as e:
        print(f"Failed to send to {recipient}: {e}")

# Send to all recipients
for recipient in recipients:
    send_email(recipient)
