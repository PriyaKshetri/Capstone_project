from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from project import main
import time

def task_on_creation(event):
    print('Watcher observed a file was added in daily progress report. File is getting ready to be emailed.')
    main()


if __name__ == '__main__':
    
    event_handler = FileSystemEventHandler()

    event_handler.on_created = task_on_creation
    
    path = r"\Users\kshet\Desktop\daily_progress"
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    