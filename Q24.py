#Get the time stamp of file created
import os
import datetime

def get_file_creation_time(file_path):
    try:

        creation_time = os.path.getctime(file_path)

        creation_time_human_readable = datetime.datetime.fromtimestamp(creation_time)
        return creation_time_human_readable
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


file_path = 'path/to/your/file.txt'
creation_time = get_file_creation_time(file_path)

if creation_time:
    print(f"The file '{file_path}' was created on: {creation_time}")
