from os import listdir
from os.path import isdir, getsize, sep
from sys import argv
from operator import itemgetter


def find_files(directory):
    content = listdir(directory)
    files = []
    for item_name in content:
        path = directory + sep + item_name
        if not isdir(path):
            files.append((path, item_name + " " + str(getsize(path))))
        else:
            child_dir_files = find_files(path)
            files.extend(child_dir_files)
    files.sort(key=itemgetter(1))
    return files


def recognize_duplicates(files):
    unique_names_and_sizes = []
    duplicates = []

    for item in files:
        if item[1] in unique_names_and_sizes:
            duplicates.append(item[0])
        else:
            unique_names_and_sizes.append(item[1])
    return duplicates


def fetch_files():
    try:
        directory_path = argv[1]
        files = find_files(directory_path)
        return files
    except IndexError:
        print("Directory not specified!")
    except FileNotFoundError:
        print("Directory not found!")
    exit()


def print_duplicates():
    files = fetch_files()
    duplicates = recognize_duplicates(files)
    if len(duplicates) > 0:
        print("Directory contain duplicates:")
        for item in duplicates:
            print(item)
    else:
        print("Duplicates not found!")

if __name__ == '__main__':
    print_duplicates()
