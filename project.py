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