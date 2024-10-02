import os

def list_files_in_directory(directory):
    try:

        files = os.listdir(directory)

        files = [f for f in files if os.path.isfile(os.path.join(directory, f))]
        return files
    except FileNotFoundError:
        return f"The directory '{directory}' does not exist."
    except PermissionError:
        return f"Permission denied to access '{directory}'."

directory_path = '/path/to/directory' 
file_list = list_files_in_directory(directory_path)
print(file_list)
