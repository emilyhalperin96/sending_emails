import os 
import requests
from dotenv import load_dotenv 

load.dotenv()

DOMAIN = os.getenv('MAILGUN_DOMAIN')

def send_simple_message(to, subject, body):
    return requests.post(
		f"https://api.mailgun.net/v3/{domain}/messages",
		auth=("api", os.getenv('MAILGUN_API_KEY')),
		data={"from": "Emily Halperin <mailgun@{domain}>",
			"to": [to],
			"subject": subject,
			"text": body}
            )
def send_user_registration_email(email, username):
    return send_simple_message(
        email,
        "successfully signed up",
        f'Hi {username} you have successfully signed up to the Stores REST API'
    )