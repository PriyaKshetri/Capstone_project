#import libraries
import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import re
from email import encoders
import shutil
from dotenv import load_dotenv

#define a main function to call on functions.
load_dotenv()


def main():
    x=file_to_be_sent()
    send_email(x)
    move_file(x)

   
def file_to_be_sent():
    path_file = glob.iglob('C:/Users/kshet/Desktop/daily_progress/*')
    attachment = max(path_file, key=os.path.getctime)
    return attachment

def validate_email(email):
    if not re.match(r'[a-z0-9\.-]+@[a-z]+\.[a-z]+', email):
        return 'please use correct email'
        exit(1)
    return True
    
    
        
def send_email(attachment):
    subject = 'Progress report'
    sender = os.getenv("email_address")
    receiver = 'kshettri.priya@gmail.com'
    password = os.getenv("passwordd")  #Use App password to use an encrypted password that works only in your device.
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
    message.attach(MIMEText(body))
    
    with open(attachment, "rb") as attaches:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attaches.read())

    text = message.as_string()
   
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, message['To'], text)
    server.close()

    return 'Your email is sent sucessfully.'
    

#move the file to a folder after being sent as an email to keep track of sent files.
def move_file(attachment):
    shutil.move(attachment, (r'C:/Users/kshet/Desktop/submitted_reports/'))
    return True
    


if __name__ == '__main__':
    main()  
