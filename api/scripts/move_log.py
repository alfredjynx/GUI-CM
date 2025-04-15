import os
import shutil

def move_file_to_directory(file_path, directory_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return

    file_name = os.path.basename(file_path)
    destination_path = os.path.join(directory_path, file_name)

    try:
        shutil.move(file_path, destination_path)
        print(f"Moved '{file_path}' to '{destination_path}'")
    except Exception as e:
        print(f"Error moving file: {e}")


def check_log_file():
    
    log_files = [f for f in os.listdir("./samples") if "log" in f]
    
    for f in log_files:
        file_path = os.path.join("./samples", f)
        dir_path = os.path.join("./samples", [d for d in os.listdir("./samples") if f.split("_")[-1].split(".")[0] in d and ".log" not in d][0])

        move_file_to_directory(file_path=file_path, directory_path=dir_path)
