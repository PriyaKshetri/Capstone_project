import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import re
from email import encoders
import shutil

   

    
def file_to_be_sent():
    path_file = glob.iglob(r'C:/Users/kshet/Desktop/daily_progress/*')
    attachment = max(path_file, key=os.path.getctime)
    return attachment

def validate_email(email):
    if not re.match(r'[a-z0-9\.-]+@[a-z]+\.[a-z]+', email):
        return 'please use correct email'
        exit(1)
    return True

def send_email(attachment):
    subject = 'Progress report'
    sender = 'kshetripriya934@gmail.com'
    receiver = 'kshettri.priya@gmail.com'
    password = 'pwarnucsmybzqxsx'
    body = ''' Hello!

    I have attached a complete report for today.
    Hope you have a wonderful rest of the day.

    Regards. 
    Priya'''

    validate_email(sender)
    validate_email(receiver)
    
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))
    
    with open(attachment, "rb") as attaches:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attaches.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename = os.path.basename(attachment))
    message.attach(part)

    text = message.as_string()
   
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, message['To'], text)
    server.close()

    return 'Your email is sent sucessfully.'
    
