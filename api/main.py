# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
import routes
from scripts.move_log import check_log_file
from scripts.run_deletion import delete_old_files
from scripts.folder_renaming import rename_folders
import os

def create_folder_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print(f"{directory} already exists.")

create_folder_if_not_exists("./samples")

app = FastAPI()
app.include_router(routes.router)

check_log_file()
rename_folders()
delete_old_files()

@app.get("/")
def root():
    return {"Hello": "World"}