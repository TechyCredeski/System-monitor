import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv


# load .env file
load_dotenv()  


#Thresholds
CPU_THRESHOLD = 50
MEMORY_THRESHOLD = 50


#Email Settings


SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER = os.getenv("RECEIVER_EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASSWORD")

def send_alert(message):
    msg = MIMEText(message)
    msg['Subject'] = 'System Health Alert'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER
    
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASS)
            server.sendmail(SENDER_EMAIL, RECEIVER, msg.as_string())
        print("Alert email sent!")
    except Exception as e:
        print(f"Error sending email: {e}")
        
if __name__ == "__main__":
    send_alert("🚨   This is a test of your alert system.")
    

