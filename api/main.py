# run: uvicorn main:app --reload

from fastapi import FastAPI # type: ignore
import routes
from scripts.move_log import check_log_file
from scripts.run_deletion import delete_old_files
from scripts.folder_renaming import rename_folders


app = FastAPI()
app.include_router(routes.router)

check_log_file()
rename_folders()
delete_old_files()

@app.get("/")
def root():
    return {"Hello": "World"}