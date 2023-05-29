"""
This module contains a function to download data (json format)
"""

# MANAGE ENVIRONNEMENT
from pathlib import Path
import re
import os
import requests


def create_folder(dirpath_name: str, subdir_names: list) -> None:
    """create directories and sub-directories for data"""

    dirpath = Path(os.path.join(dirpath_name))

    if dirpath.is_dir():
        print()
        print(f"The directory '{dirpath_name}' already exists")

        # Check and create the subdirectory
        for subdir_name in subdir_names:

            subdir = Path(os.path.join(subdir_name))
            subpath = dirpath / subdir
            if subpath.is_dir():
                print(f"The subdirectory '{subdir_name}' already exists")
            else:
                subpath.mkdir()
                print(f"The subdirectory '{subdir_name}' has been created")
    else:
        # Create the directory
        dirpath.mkdir()

        # Create subdirectories
        for subdir_name in subdir_names:

            subdir = Path(os.path.join(subdir_name))
            subpath = dirpath / subdir
            subpath.mkdir()

        subdir_names_str = ', '.join(f"'{subdir_name}'"
                                     for subdir_name in subdir_names)
        print()
        print(
            f"The directory '{dirpath_name}' and sub-directory {subdir_names_str} "
            "have been created"
            )


filenames = [
    "MMM_EcoCompt_X2H19070220_archive.json",
    "MMM_EcoCompt_X2H20042632_archive.json",
    'MMM_EcoCompt_X2H20042634_archive.json',
    'MMM_EcoCompt_X2H20063162_archive.json'
]


def load_json_files(file_names: list = filenames) -> None:
    """loads json files"""

    print()
    print("Please wait, json files are being pre-processed...")
    print()

    for filename in file_names:

        var_name = re.search(r"X2H\d+", filename).group()

        url = "https://data.montpellier3m.fr/sites/default/files/ressources/"\
              + filename
        response = requests.get(url)

        data_path = os.path.join("data", "raw", var_name + ".json")

        with open(data_path, "w") as f:
            f.write(response.text)
