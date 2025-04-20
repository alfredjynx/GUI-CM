import os

def rename_folders():
    
    base_path = "./samples"

    bad_char = '\uf03a'  

    for name in os.listdir(base_path):
        if bad_char in name:
            new_name = name.replace(bad_char, '-')
            old_path = os.path.join(base_path, name)
            new_path = os.path.join(base_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {name} → {new_name}")