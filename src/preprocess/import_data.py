"""
This module contains a function to download data (json format)
"""

# MANAGE ENVIRONNEMENT
from pathlib import Path
import re
import os
import requests


def create_folder(dirpath_name: str, subdir_name: str) -> None:
    """create directories and sub-directories for data"""

    dirpath = Path(os.path.join("..", "..", dirpath_name))
    subdir = Path(os.path.join("..", "..", dirpath_name,  subdir_name))

    if dirpath.is_dir():
        print(f"The directory '{dirpath_name}' already exists")
        # Check and create the subdirectory
        subpath = dirpath / subdir
        if subpath.is_dir():
            print(f"The subdirectory '{subdir_name}' already exists")
        else:
            subpath.mkdir()
            print(f"The subdirectory '{subdir_name}' has been created")
    else:
        # Create the directory and subdirectory
        subpath = dirpath / subdir
        subpath.mkdir(parents=True)
        print(f"The directory '{dirpath_name}' and\
              sub-directory '{subdir_name}' have been created")


create_folder(dirpath_name='dataaa', subdir_name="raw")
create_folder(dirpath_name='dataaa', subdir_name="preprocess")


def load_json_files(file_names: list) -> None:
    """loads json files"""

    for filename in file_names:

        var_name = re.search(r"X2H\d+", filename).group()

        url = "https://data.montpellier3m.fr/sites/default/files/ressources/"\
              + filename
        response = requests.get(url)

        data_path = os.path.join("..", "..", "data", "raw", var_name + ".json")

        with open(data_path, "w") as f:
            f.write(response.text)


filenames = [
    "MMM_EcoCompt_X2H19070220_archive.json",
    "MMM_EcoCompt_X2H20042632_archive.json",
    'MMM_EcoCompt_X2H20042634_archive.json',
    'MMM_EcoCompt_X2H20063162_archive.json'
]

load_json_files(file_names=filenames)
