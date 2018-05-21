#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import loginfo.creds as Secrets
from read_json import *

fromEmail = Secrets.login['fromEmail']
toEmail = Secrets.login['toEmail']
emailLogin = Secrets.login['emailLogin']
emailPass = Secrets.login['emailPass']
emailServer = Secrets.login['emailServer']
emailPort = Secrets.login['emailPort']

raceTitle = output_config()["title"]

def send_email(emailSubject,emailBody):
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = emailSubject

    body = emailBody

    msg.attach(MIMEText(body,'plain'))

    s = smtplib.SMTP(emailServer,emailPort)
    s.ehlo()
    s.starttls()
    s.login(emailLogin,emailPass)
    text = msg.as_string()
    s.sendmail(fromEmail,toEmail,text)
    s.quit()

if __name__ == "__main__":
    send_email("New Race to watch!",raceTitle)
