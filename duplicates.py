from os import listdir
from os.path import isdir, getsize
from sys import argv


def all_files(dir_path):
    dir_content = listdir(dir_path)
    files = []

    for dir_item in dir_content:
        file_path = dir_path + "/" + dir_item
        if not isdir(file_path):
            file_inf = {"name": dir_item, "size": getsize(file_path), "path": dir_path}
            files.append(file_inf)
        else:
            child_dir_files = all_files(file_path)
            files.extend(child_dir_files)

    return files


def find_duplicates(files):
    uniq_items = []
    for file in files:
        short_file_inf = {"name": file["name"], "size": file["size"]}
        if short_file_inf not in uniq_items: uniq_items.append(short_file_inf)

    duplicates = []
    for item in uniq_items:
        sub_duplicates = []
        for file in files:
            if file["name"] == item["name"] and file["size"] == item["size"]:
                file_path = file["path"] + "/" + file["name"]
                sub_duplicates.append(file_path)

        if sub_duplicates.__len__() > 1:
            duplicates.extend(sub_duplicates)

    return duplicates


if __name__ == '__main__':
    try:
        files = all_files(argv[1])
        duplicates = find_duplicates(files)
        if duplicates.__len__() == 0:
            print("Duplicates not found")
        else:
            print("Directory contain duplicates:")
            for item in duplicates: print(item)
    except IndexError:
        print("Directory not specified!")
    except FileNotFoundError:
        print("Directory not found!")
    except NotADirectoryError:
        print("It is not a directory!")


