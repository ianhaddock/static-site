# copy_static.py

import os
import shutil


def recursive_copy(source: str, destination: str) -> None:
    """ clear destination, then recursively copy all contents from source to destination"""

    if not os.path.exists(source):
        raise Exception('Source directory not found')
    if not os.path.exists(destination):
        os.mkdir(destination)

    for item in os.listdir(source):
        if os.path.isdir(os.path.join(source, item)):
            recursive_copy(os.path.join(source, item), os.path.join(destination, item))
        elif os.path.isfile(os.path.join(source, item)):
            shutil.copy(os.path.join(source, item), destination) 
    
    return
