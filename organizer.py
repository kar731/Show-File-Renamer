import os
import time
import json

from guessit import guessit
from datetime import datetime

finished_files = []


def titleInformation(filename, extension):
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

    season = "{0:0>2}".format(name['season'])
    episode = "{0:0>2}".format(name['episode'])

    filename = "{0} S{1}E{2}{3}".format(title, season, episode, extension)
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

    filetypes = [".mp4", ".avi", ".mkv"]
    files = os.listdir(".")

    for show in files:
        title, extension = os.path.splitext(show)
        finished_files = json.load(open("files.json"))

        if extension in filetypes and show not in finished_files["files"]:
            print(title)

            os.rename(show, titleInformation(show, extension))
            finished_files["files"].append(titleInformation(show, extension))

            json.dump(finished_files, open("files.json", "w"),
                      indent=4, sort_keys=True)


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
