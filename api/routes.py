import os
from fastapi import APIRouter, status

from pipeline import AlgoIn
from datetime import datetime

router = APIRouter()


@router.post("/pipeline", response_model=dict, status_code=status.HTTP_201_CREATED, tags=["items"])
def run_pipeline(algoIn: AlgoIn): 

    json_path, input_dir =  algoIn.callJSON()

    terminal_command = f"""
    cd ..
    cd cm_pipeline
    python -m main ../api/{json_path}.json
    """

    input_dir += "-" + datetime.now().strftime("%Y%m%d-%H:%M:%S")
    os.system(terminal_command)

    algoIn.postTreatment(input_dir)

    return {"path":algoIn.get_type_post(input_dir=input_dir)}

