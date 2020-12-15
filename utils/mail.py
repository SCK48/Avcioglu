import threading
from django.core.mail import EmailMessage

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
        msg = EmailMessage(self.subject, self.html_content, self.sender, self.recipient_list)
        msg.content_subtype = 'html'
        if self.file:
            msg.attach_file(self.file)
        msg.send()


def send_html_mail(subject, html_content, recipient_list=[settings.EMAIL_SEND_USER], sender=settings.EMAIL_HOST_USER, file=None):
    EmailThread(subject, html_content, recipient_list, sender, file).start()