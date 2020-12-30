import threading
from django.core.mail import EmailMessage
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, sender, file=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.sender = sender
        self.file = file
        threading.Thread.__init__(self)

    def run(self):
        message = Mail(
            from_email=self.sender,
            to_emails=self.recipient_list,
            subject=self.subject,
            html_content=self.html_content)
        try:
            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)


def send_html_mail(subject, html_content, recipient_list=[settings.EMAIL_SEND_USER], sender=settings.EMAIL_HOST_USER, file=None):
    EmailThread(subject, html_content, recipient_list, sender, file).start()