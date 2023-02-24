"""This script is used to collect the path of every json file in this directory and all subdirectories and creates
a index.txt file. This index.txt file then is used by the transistordatabase to update the local database.
"""

import urllib.request
import urllib.parse
import os

def get_file_list(folder):
    rel_file_paths = []
    for path, subdirs, files in os.walk(folder):
        rel_path = os.path.relpath(path, folder)
        for file in files:
            if file.endswith(".json"):
                rel_file_paths.append(os.path.join(rel_path, file))

    return rel_file_paths

if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    text_file_path = os.path.join(directory, "index.txt")
    base_url = r"https://raw.githubusercontent.com/upb-lea/transistordatabase_File_Exchange/main/"

    with open(text_file_path, "w") as fd:
        for rel_file_path in get_file_list(directory):
            url = urllib.parse.urljoin(base_url, urllib.request.pathname2url(rel_file_path))
            fd.write(f"{url}\n")

