import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

def send_verification_email(to_email: str, token: str):
    if not SMTP_USER or not SMTP_PASSWORD:
        print("SMTP Credentials missing. Skipping email sending.")
        return

    subject = "Verify your account for PPU Chatbot"
    verification_link = f"http://localhost:5173/verify?token={token}"
    
    html = f"""
    <html>
      <body>
        <h2>Welcome to PPU AI Chatbot</h2>
        <p>Please click the link below to verify your email address and activate your account:</p>
        <p><a href="{verification_link}">{verification_link}</a></p>
        <p>If you did not request this, please ignore this email.</p>
      </body>
    </html>
    """

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    part = MIMEText(html, "html")
    msg.attach(part)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, to_email, msg.as_string())
            print(f"Verification email sent to {to_email}")
    except Exception as e:
        print(f"Error sending email: {e}")
