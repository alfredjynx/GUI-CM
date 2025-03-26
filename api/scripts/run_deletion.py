import os
import shutil
from datetime import datetime, timedelta

def extract_datetime(entry):
    _, date, time = entry.split('-')
    return datetime.strptime(date + time, "%Y%m%d%H:%M:%S")


def clear_directory(directory_path):
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a directory.")
        return

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path) 
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path) 
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

def delete_old_files():
    dirs = [f for f in os.listdir("./samples") if "log" not in f]
    
    for d in dirs:
        dt = extract_datetime(d)
        
        if datetime.now() - dt > timedelta(hours=24):
            clear_directory(os.path.join("./samples", d))
            os.rmdir(os.path.join("./samples", d))