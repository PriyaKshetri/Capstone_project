#import required libraries
import os
import glob
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import re
from email import encoders
import shutil
from memory_profiler import profile

#write a main function that calls related functions  
def main():

    #give a variable for file_to_be_sent function
    x=file_to_be_sent()
    send_email(x)
    move_file(x)
    
@profile
def file_to_be_sent():

    #Return a list of files that matches the path specified in the function argument
    path_file = glob.iglob(r'C:/Users/kshet/Desktop/daily_progress/*')
    attachment = max(path_file, key=os.path.getctime)
    return attachment


def validate_email(email):

    #validate emails using regex pattern
    if not re.match(r'[a-z0-9\.-]+@[a-z]+\.[a-z]+', email):
        return 'please use correct email'
        exit(1)
    return True


def send_email(attachment):
    #fill in fields required to send an email
    subject = 'Progress report'
    sender = 'kshetripriya934@gmail.com'
    receiver = 'kshettri.priya@gmail.com'
    #generate an app password so that your password is not displayed.
    password = 'pwarnucsmybzqxsx' """This password is generated from App password"""
    body = ''' Hello!

    I have attached a complete report for today.
    Hope you have a wonderful rest of the day.

    Regards. 
    Priya'''
#call validate_email functions to check emails of sender and receiver.
    validate_email(sender)
    validate_email(receiver)
    
    #A subclass of MIMENonMultipart, the MIMEText class is used to create MIME objects of major type text.
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = subject
    message.attach(MIMEText(body,'plain'))
    
    #open attachment and use the generic 'application/octet-stream'
    with open(attachment, "rb") as attaches:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attaches.read())
    
    #encode for transporting using base64 encoding
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename = os.path.basename(attachment))
    message.attach(part)

    text = message.as_string() 
    """send as string"""
    
   
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    """specify the server with its parameters"""

    server.ehlo()
    server.login(sender, password)
    server.sendmail(sender, message['To'], text)
    server.close()

    return 'Your email is sent sucessfully.'
    
    
def move_file(attachment):
    #after sending email move it to another folder to keep tracks of things that have been sent successfully.
    shutil.move(attachment, (r'C:/Users/kshet/Desktop/submitted_reports/'))
    return True
    


if __name__ == '__main__':
    main()  