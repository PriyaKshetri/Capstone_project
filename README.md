# Capstone_project

I created this project out of necessity. Organisations may have a tight schedule and sending out reports, progress files, spreadhseet, daily expenditures or some files that needs to be sent in a timely basis, on repeat; could be one of the most important tasks. 

My program helps a user to automate sending a file as soon as it gets added to a directory, through an email(specifically in this case). Discovery watchdog has been the most exciting part of journey in learning pyhton. The benefits of watchdog have no limitations. Therefore, in my program, I have used watchdog to observe if a file is added to a folder, and then when this observation will be made, that file will be sent through email as well as be moved to another folder so that, I could tack all my sent files so far. 

Watchdog is literraly a watch-dog. watchdog not only watches any changes that happens somewhere in our computer but also leads event handler to take some kind of action in that given case. 

You can install it using the command:  
pip install watchdog (Make sure you are using upgraded version of pip)

You will also need to import these required libraries:
import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

