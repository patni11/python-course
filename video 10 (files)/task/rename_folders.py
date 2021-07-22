import os


def rename(path, split):
    if split == "_":
        seperator = " "
    else:
        seperator = "_"
    for dir in os.listdir(path):
        if ".DS_Store" and "." not in dir:
            print(dir)
            if split in dir:
                dir_name = dir.split(split)
                new_name = f"{dir_name[1]}{seperator}{dir_name[0]}{seperator}{dir_name[2]}"
                os.rename(dir, new_name)
                print("renaming")


rename(os.getcwd(), "_")
