import smtplib, ssl
def send_email(email_recipient,
               email_subject,
               email_message_text
               ):
    sender_email = 'web.user@treasuryquants.com'
    password='web.user@treasuryquants.com1Password1'
    port=587
    smtp_server = "smtp.ionos.co.uk"

    try:
        message = "From: "+sender_email+"\r\n"+"Subject: " + email_subject +"\r\n\r\n"+email_message_text
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, email_recipient, message)
    except:
        print("SMPT server connection error")
    return True
