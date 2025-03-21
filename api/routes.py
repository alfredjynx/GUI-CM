import os
from fastapi import APIRouter, status

from pipeline import AlgoIn
from datetime import datetime

router = APIRouter()

def extract_datetime(entry):
    _, date, time = entry.split('-')
    return datetime.strptime(date + time, "%Y%m%d%H:%M:%S")

@router.post("/pipeline", response_model=dict, status_code=status.HTTP_201_CREATED, tags=["items"])
def run_pipeline(algoIn: AlgoIn): 

    json_path, input_dir =  algoIn.callJSON()

    terminal_command = f"""
    cd ..
    cd cm_pipeline
    python -m main ../api/{json_path}.json
    """

    os.system(terminal_command)

    input_dir += sorted(os.listdir(input_dir))[-1]

    algoIn.postTreatment(input_dir)

    f_path, f_stats_path = algoIn.get_type_post(input_dir=input_dir)

    return {"path":f_path, "stats":f_stats_path}

