import os
from pathlib import Path

SUBDIRECTORIES = {
    'DOCUMENTS': ['.pdf', '.txt', '.csv', '.xlsx'],
    'AUDIO': ['.m4a', '.m4b', '.mp3'],
    'VIDEOS': ['.mov', '.avi', '.mpeg4', '.mp4'],
    'IMAGES': ['.jpg', '.jpeg', '.png', '.gif']
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


def organizeDirectory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickDirectory(filetype)
        directoryPath = Path(directory)
        if not directoryPath.is_dir():
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()
