from email.mime.text import MIMEText
import smtplib

def send_email(email, height):
    from_email= "jaribio99@gmail.com"
    password = "7Gh-T58-zCx-gn4"
    to_email = email

    subject = "Height Data"
    message = "Hey There, you mentioned that your height is <strong> %s. </strong>" %height

    msg = MIMEText(message, 'html')
    msg['Subject']= subject
    msg['To']= to_email
    msg['From']=from_email

    gmail= smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, password)
    gmail.sendmail(from_email, to_email, msg)
    # gmail.sendmail(msg)
    gmail.quit()
