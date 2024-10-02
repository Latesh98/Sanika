 #Check permission of file

import os

def check_file_permission(file_path):
    permissions = {
        'readable': os.access(file_path, os.R_OK),
        'writable': os.access(file_path, os.W_OK),
        'executable': os.access(file_path, os.X_OK)
    }

    return permissions

# Example usage
file_path = 'path/to/your/file.txt'  # Change this to your target file
permissions = check_file_permission(file_path)

if permissions['readable']:
    print(f"The file '{file_path}' is readable.")
else:
    print(f"The file '{file_path}' is not readable.")

if permissions['writable']:
    print(f"The file '{file_path}' is writable.")
else:
    print(f"The file '{file_path}' is not writable.")

if permissions['executable']:
    print(f"The file '{file_path}' is executable.")
else:
    print(f"The file '{file_path}' is not executable.")
