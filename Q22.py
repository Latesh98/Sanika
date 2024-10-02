#22. Delete file from directory

import os

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"The file '{file_path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to delete the file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = 'path/to/your/file.txt'
delete_file(file_path)
