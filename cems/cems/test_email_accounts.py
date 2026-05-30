import smtplib
from email.mime.text import MIMEText


def test_smtp(username, password, description):
    print(f"\nTesting {description}: {username}")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    try:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        print("   [SUCCESS] Login successful!")

        # Try to send a test mail to the user themselves
        msg = MIMEText("Utsav App Test Email")
        msg["Subject"] = "Utsav SMTP Test Success"
        msg["From"] = username
        msg["To"] = username
        server.sendmail(username, [username], msg.as_string())
        print("   [SUCCESS] Test email sent!")
        server.quit()
        return True
    except Exception as e:
        print(f"   [FAILED] {type(e).__name__}: {e}")
        try:
            server.quit()
        except Exception:
            pass
        return False


# Test the mallasajjit@gmail.com account
test_smtp("mallasajjit@gmail.com", "dnbgpmdpziuafzir", "Mallasajjit Account")

# Test the np03cs4a230357@heraldcollege.edu.np account
test_smtp(
    "np03cs4a230357@heraldcollege.edu.np", "mssfwzidmrajqrnn", "Herald College Account"
)
