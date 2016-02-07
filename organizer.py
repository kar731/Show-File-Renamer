import os

from guessit import guessit

finished_files = []

def titleInformation(filename):
    """Finds the needed information to rename the show.

    Takes the filename and formats it with information from guessit.
    Current format: Title S01E01.filename

    Args:
        filename: The name of the file for it to be decoded and renamed.

    Returns:
        The new filename format.

    Raises:
        None
    """

    name = guessit(filename)
    title = name['title']
    season = name['season']
    episode = name['episode']

    file_ending = filename[len(filename) - 4:len(filename)]

    if int(season) < 10:
        season = "0{}".format(season)
    if int(episode) < 10:
        episode = "0{}".format(episode)

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
        if file[len(file) - 4:len(file)] in filetypes and file not in finished_files:
            print(file)
            os.rename(file, titleInformation(file))
            finished_files.append(titleInformation(file))

if __name__ == "__main__":
    renamer()
