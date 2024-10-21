# This file is a main Python file organizer that continuously watches three directories for modifications and organizes files
from pathlib import Path
# pauses the execution of the script for a specified number of seconds.
from time import sleep
# monitor different directories for filesystem events
from watchdog.observers import Observer
from evenhandler import EvenHandler

if '__name__' == '__name__':
    # returns the home directory of the current user
    watch_path_1 =Path.home() / 'Downloads'
    watch_path_2 =Path.home() / 'Pictures'
    watch_path_3 =Path.home() / 'Desktop' 

    destination_root_1 = Path.home() / 'Downloads/holder of things'
    destination_root_2 = Path.home() / 'Pictures/holder of things'
    destination_root_3 = Path.home() / 'Desktop/holder of things'

    event_handle_1 = EvenHandler(watch_path=watch_path_1, destination_root=destination_root_1)
    event_handle_2 = EvenHandler(watch_path=watch_path_2, destination_root=destination_root_2)
    event_handle_3 = EvenHandler(watch_path=watch_path_3, destination_root=destination_root_3)

    observer_1 = Observer()
    observer_1.schedule(event_handle_1, f"{watch_path_1}", recursive=True)
    observer_1.start()

    observer_2 = Observer()
    observer_2.schedule(event_handle_2, f"{watch_path_2}", recursive=True)
    observer_2.start()

    observer_3 = Observer()
    observer_3.schedule(event_handle_3, f"{watch_path_3}", recursive=True)
    observer_3.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        #  called for each observer to stop monitoring
        observer_1.stop()
        observer_2.stop()
        observer_3.stop()
    # called for each observer to wait for the observer's thread to finish.
    observer_1.join()
    observer_2.join()
    observer_3.join()


