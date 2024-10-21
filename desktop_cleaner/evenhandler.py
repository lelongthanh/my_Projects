# This file will determine what type of directory subfolder will be stored based on types of file
# 's'hutil': a module for file operations
import shutil
from datetime import date
# 'Path' is a class from the 'pathlib' module that represents file system paths.
from pathlib import Path
# 'FileSystemEventHandler' is a class from the 'watchdog.events' module that provides event handlers for file system events.
from watchdog.events import FileSystemEventHandler

from extensions import extension_paths

def add_date_to_path(path: Path):
    # this function is a utility that helps organize destination paths based on the current year and month, creating the necessary directories if they don’t already exist.
    # date.today().year = get the current year
    # date.today().strftime("%B").upper() = get the current month in full text: September => Sep
    current_year = date.today().year
    current_month = date.today().strftime('%B')
    dated_path = path / f"{current_year}" / f"{current_month}"
    # mkdir, pathLib, Path. Create a new directory at this given path
    # parents=True. ensures that parent directories are also created if they don't exist.
    # exist_ok=True. prevents an error if the directories already exist.
    dated_path.mkdir(parents=True, exist_ok=True)
    return dated_path

def rename_file(source: Path, destination_path: Path):
    # This function helps ensure that files are moved to a destination directory with a unique name to prevent overwriting existing files
    # Check if a file with the same name already exists in the destination folder
    if Path(destination_path / source.name).exists():
        increase = 0

        while True:
            increase += 1
            # if file_name exist, adding file_name(increase) until uniq name is found
            new_name = destination_path / f"{source.stem}_{increase}{source.suffix}"
            if not new_name.exists():
                return new_name
    
    else:
        # if no file with same_name it's return original file_name
        return destination_path / source.name

class EvenHandler(FileSystemEventHandler):
    def __init__(self, watch_path: Path, destination_root: Path):
        # The constructor initializes the watch_path and destination_root attributes by resolving the provided paths
        self.watch_path = watch_path.resolve()
        self.destination_root = destination_root.resolve()

    
    # This method is called when a file is modified in the watched directory
    def on_modified(self, event):
        for child in self.watch_path.iterdir():
            # checks if the file is a regular file and has an extension specified in
            if child.is_file() and child.suffix.lower() in extension_paths:
                destination_path = self.destination_root / extension_paths[child.suffix.lower()]
                destination_path = add_date_to_path(path=destination_path)
                destination_path = rename_file(source=child, destination_path=destination_path)
                #  moves the file to the calculated destination path using
                shutil.move(src=child, dst=destination_path)