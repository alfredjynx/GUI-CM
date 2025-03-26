import os
from fastapi import APIRouter, status

from pipeline import AlgoIn

from scripts.move_log import check_log_file
from scripts.run_deletion import delete_old_files
from scripts.folder_renaming import rename_folders

router = APIRouter()

import subprocess

def run_pipeline_command(json_path):
    command = [
        "python3", "main.py", f"../api/{json_path}.json"
    ]

    try:
        result = subprocess.run(
            command,
            cwd="../cm_pipeline", 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            text=True 
        )
        print("PIPELINE STDOUT:\n", result.stdout)
        print("PIPELINE STDERR:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print("🚨 Pipeline command failed:")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
        raise


@router.post("/pipeline", response_model=dict, status_code=status.HTTP_201_CREATED, tags=["items"])
def run_pipeline(algoIn: AlgoIn): 
    
    delete_old_files()
    

    json_path, input_dir =  algoIn.callJSON()

    run_pipeline_command(json_path=json_path)
    check_log_file()
    rename_folders()

    base_path = os.path.dirname(__file__)  # /app/api
    input_dir = os.path.join(base_path, "samples")

    latest_sample = sorted(os.listdir(input_dir))[-1]

    input_dir = os.path.join(input_dir, latest_sample)

    algoIn.postTreatment(input_dir)

    f_path, f_stats_path = algoIn.get_type_post(input_dir=input_dir)

    return {"path":f_path, "stats":f_stats_path}

