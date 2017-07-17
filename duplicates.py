from os import listdir
from os.path import isdir, getsize
from sys import argv


def find_files(directory):
    content = listdir(directory)
    files = []

    for item_name in content:
        path = directory + "/" + item_name
        if not isdir(path):
            files.append({"name_and_size": item_name+str(getsize(path)), "path": path})
        else:
            child_dir_files = find_files(path)
            files.extend(child_dir_files)

    return files


def recognize_duplicates(files):
    unique_names_and_sizes = []
    duplicates = []

    for item in files:
        if item["name_and_size"] in unique_names_and_sizes:
            duplicates.append(item["path"])
        else:
            unique_names_and_sizes.append(item["name_and_size"])

    return duplicates


if __name__ == '__main__':
    try:
        files = find_files(argv[1])
    except IndexError:
        print("File not specified!")
        exit()

    duplicates = recognize_duplicates(files)
    if len(duplicates) > 0:
        for item in duplicates:
            print(item)
    else:
        print("Duplicates not found!")
