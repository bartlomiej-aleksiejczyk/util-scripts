from os import listdir
import os
import eyed3
from os.path import isfile, isdir, join
from pathlib import Path

files_and_dirs = listdir()

file_list = tuple(x for x in files_and_dirs if isfile(x))
dir_list = tuple(x for x in files_and_dirs if isdir(x))

for path in Path('.').rglob('*.mp3'):
    Path(path).rename(path.name)