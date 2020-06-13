import os
from pathlib import Path


absolutePath = "/Users/handrywahyudi/Documents/"
picturesPath = "/Users/handrywahyudi/Pictures/"


SUBDIRECTORIES = {
    absolutePath + "Docs": ['.doc', '.txt', '.docx', '.zip'],
    absolutePath + "Books": ['.pdf', '.epub'],
    absolutePath + "Installer": ['.dmg','.iso', '.app', '.exe'],
    picturesPath: ['.jpg', '.jpeg'],
    absolutePath + "Movies": ['.mp4', '.mkv', '.mp3', '.srt']
}


def pickDirectory(value):
    for category, extensions in SUBDIRECTORIES.items():
        for extension in extensions:
            if extension == value:
                return category
    return absolutePath + 'Misc'


def organizeDirectory(filetype):
    for item in os.scandir():
        if item.is_dir():
            continue
        filePath = Path(item)
        fileType = filePath.suffix.lower()
        fileType = filetype.replace('.', '')

        if fileType == 'pdf':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'doc':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))
           
        if fileType == 'txt':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'docx':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'zip':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))
           
        if fileType == 'epub':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'dmg':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'iso':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'app':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'exe':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'jpg':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'jpeg':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'mp4':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'mkv':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))
           
        if fileType == 'mp3':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'srt':
           directory = pickDirectory(fileType) 
           directoryPath = Path(directory)
           filePath.rename(directoryPath.joinpath(filePath))

        if fileType == 'all':
            filePath = Path(item)
            fileType = filePath.suffix.lower()
            directory = pickDirectory(fileType)
            directoryPath = Path(directory)

            if fileType == '.py':
                continue

            filePath.rename(directoryPath.joinpath(filePath))


organizeDirectory()

