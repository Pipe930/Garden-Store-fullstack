from django.core.mail import EmailMessage

# Util class
class Util:

    # static method send email
    @staticmethod
    def send_email(data):
        email = EmailMessage(subject=data["full_name"], body=data["message"], to=[data["email"]])
        email.send() # send email
