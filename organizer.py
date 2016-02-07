import os
import time

from guessit import guessit
from datetime import datetime

finished_files = []


def titleInformation(filename, length):
    """Finds the needed information to rename the show.

    Takes the filename and formats it with information from guessit.
    Current format: Title S01E01.filename

    Args:
        filename: The name of the file for it to be decoded and renamed.
        length: length of the filename
    Returns:
        The new filename format.

    Raises:
        None
    """

    name = guessit(filename)
    title = name['title']
    season = name['season']
    episode = name['episode']

    file_ending = filename[length - 4:length]

    season = "{0:0>2}".format(name['season'])
    episode = "{0:0>2}".format(name['episode'])

    filename = "{0} S{1}E{2}{3}".format(title, season, episode, file_ending)
    return filename


def renamer():
    """Renames files needed to be renamed

    Checks if files are in the done list, if not it
    will rename it.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    global finished_files
    filetypes = [".mp4", ".avi", ".mkv"]
    files = os.listdir(".")

    for file in files:
        length = len(file)
        if file[length - 4:length] in filetypes and file not in finished_files:
            print(file)
            os.rename(file, titleInformation(file, length))
            finished_files.append(titleInformation(file, length))
   
def checkTime():
    now = datetime.now().time()
    if now.hour == 24:
        return True
    return False
    
if __name__ == "__main__":
    while True:
        if checkTime():
            renamer()
        else:
            time.sleep(420)
