import smtplib

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.revisamaster.contato@gmail.com"
EMAIL_HOST_PASSWORD = "nidz gesi ntpi prgx"

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    print("✅ SMTP connection successful!")
    server.quit()
except Exception as e:
    print(f"❌ SMTP Error: {e}")