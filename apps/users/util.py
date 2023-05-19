from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings

# Util class
class Util:

    # static method send email
    @staticmethod
    def send_email(data):
        EmailMultiAlternatives()
        email = EmailMessage(data["full_name"], data["message"], "settings.EMAIL_HOST_USER", [data["email"]])
        email.send(fail_silently=False) # send email
