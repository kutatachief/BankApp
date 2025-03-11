from django.core.mail import EmailMessage
from django.conf import settings
from django.utils import timezone
from .models import User, OTPCODE
import pyotp



# function that generate otp code to user
def generate_otp():
    otpcode = pyotp.TOTP(pyotp.random_base32())
    return otpcode.now()


def send_otp(email):
    subject = "One Time Password (OTP) Generation"
    otp = generate_otp()
    user = User.objects.get(email=email)
    otp_record, create_otp = OTPCODE.objects.get_or_create(user=user)
    otp_record.email_otp=otp
    otp_record.created_at = timezone.now()
    otp_record.save()

    # compose the email body
    body = f"{user.username} your otp verification code is {otp}. this will expire in 30 minutes"
    email_from = settings.EMAIL_HOST_USER
    email_sender = EmailMessage(subject=subject, from_email=email_from, body=body, to=[email])

