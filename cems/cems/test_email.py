import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cems.settings")
django.setup()

from django.core.mail import send_mail
from django.conf import settings

print("Testing SMTP email sending...")
print(f"EMAIL_HOST: {settings.EMAIL_HOST}")
print(f"EMAIL_PORT: {settings.EMAIL_PORT}")
print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
print(f"EMAIL_USE_TLS: {settings.EMAIL_USE_TLS}")
print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")

try:
    send_mail(
        subject="Utsav SMTP Test",
        message="This is a test email to verify SMTP configuration.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=["mallasajjit@gmail.com"],
        fail_silently=False,
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"Email failed: {type(e).__name__}: {e}")
