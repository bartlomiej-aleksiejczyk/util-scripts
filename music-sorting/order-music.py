from os import listdir
import os
import eyed3
from os.path import isfile, isdir, join
from pathlib import Path

files_and_dirs = listdir()

file_list = tuple(x for x in files_and_dirs if isfile(x))
dir_list = tuple(x for x in files_and_dirs if isdir(x))

def clean_string(string):
    return string.replace(' ', '-').replace('.', '').replace(',', '').replace('!', '').replace('%', '')\
        .replace(':','').replace('@', '').replace('?', '').replace('=', '').replace('+', '').replace('*', '')\
        .replace('/', '-').replace("&", ' ').replace("{", '(').replace("}", ')').replace("<", '(').replace("\"", '')\
        .replace(">", ')').replace("*", '').replace("$", '').replace("\'", '').replace("\\", '').replace("`", '')\
        .replace("|", '').replace("\n", '')

for file in file_list:
    if not file.endswith(".py"):
        file_info = eyed3.load(file)
        try:
            artist_name = clean_string(file_info.tag.artist)
        except AttributeError:
            artist_name = "unknown-artist"
        try:
            album_name = clean_string(file_info.tag.album)
        except AttributeError:
            album_name = "unknown-album"
        if album_name is None:
            album_name = "unknown-album"
        if artist_name is None:
            artist_name = "unknown-artist"
        destination = artist_name + "/" + album_name

        isExist = os.path.exists(destination)
        if not isExist:
            os.makedirs(destination)
        destination_file = artist_name + "/" + album_name + "/" + file
        Path(file).rename(destination_file)
