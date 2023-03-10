import os

def list_files(root_path):
    files = []
    for dirpath, dirnames, filenames in os.walk(root_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                files.append(filepath)
    return files

def get_folders_with_many_files(root_path, threshold, level=3):
    folders = {}
    for dirpath, dirnames, filenames in os.walk(root_path):
        # check if current directory is from this level
        if dirpath.count(os.sep) == level:
            num_files = len(list_files(dirpath))
            # check if directory has more than threshold files
            if num_files > threshold:
                folders[dirpath] = num_files
    return folders

root_path = "./"
threshold = 5000
level=3
folders_with_many_files = get_folders_with_many_files(root_path, threshold, level=level)
print("List of files with more than " + str(threshold) + " files on level " + str(level) + ":")
for key, value in folders_with_many_files.items():
    print(key + ": " + str(value))
