#25. Create a directory in given Path

import os

def create_directory(directory_path):
    try:

        os.makedirs(directory_path, exist_ok=True)
        print(f"The directory '{directory_path}' has been created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


directory_path = 'path/to/your/new_directory'
create_directory(directory_path)

