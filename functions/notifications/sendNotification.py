import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from api.notion.models.mail_templates import MailTemplate
from api.notion.models.status import Status

class MailNotification:

    def __init__(self, sender_email, password):
        self.sender_email = sender_email
        self.password = password

    def getTemplate(self, status: Status):
        try:
            return MailTemplate[status.name]
        except KeyError:
            return None
        
    def renderTemplate(self, template, context: dict):
        subject = template.value['subject']
        body = template.value['body']

        for key, value in context.items():
            subject = subject.replace(f"{{{{{key}}}}}", str(value))
            body = body.replace(f"{{{{{key}}}}}", str(value))
        
        return subject, body

    def sendEmail(self, subject, message, receiver_email):
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.send_message(msg)
            print("Email erfolgreich gesendet.")
        except Exception as e:
            print(f"Fehler: {e}")

    def sendNotification(self, status: Status, reciver_email, context: dict):
        template = self.getTemplate(status)

        if not template:
            print("Kein Template für diesen Status gefunden")
            return
        
        subject, body = self.renderTemplate(template, context)

        self.sendEmail(subject, body, reciver_email)