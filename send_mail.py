import sendgrid
import os
from sendgrid.helpers.mail import *

api_key   = os.environ.get('SENDGRID_API_KEY')
from_addr = os.environ.get('SENDGRID_MAIL_FROM')
to_addr   = os.environ.get('SENDGRID_MAIL_TO')

sg = sendgrid.SendGridAPIClient(apikey=api_key)
from_email = Email(from_addr)
to_email = Email(to_addr)
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
