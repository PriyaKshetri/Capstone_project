#import neccessary watchdog libraires
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from project import main
import time

#create an event function that detects a file getting added
def task_on_creation(event):
    print('Watcher observed a file was added in daily progress report. File is getting ready to be emailed.')
    main()


if __name__ == '__main__':
    #assign a variable for event handler
    event_handler = FileSystemEventHandler()

    #use on_created method for event handling of th above function
    event_handler.on_created = task_on_creation
    
    #specify the path of the folder you want to keep track of
    path = r"\Users\kshet\Desktop\daily_progress"
    #create a variable for oberver()
    observer = Observer()
    #start the observation
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    #handle the error
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    #join() the observer variable.
    observer.join()
    