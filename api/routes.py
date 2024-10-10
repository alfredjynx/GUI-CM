import os
from fastapi import APIRouter, HTTPException, status

from pipeline import AlgoIn
from datetime import datetime

router = APIRouter()


@router.post("/pipeline", response_model=str, status_code=status.HTTP_201_CREATED, tags=["items"])
def run_pipeline(algoIn: AlgoIn): 

    if algoIn.algo_name == "sbm":
        algoIn.generate_cargs_json()

        timestamp = "-" + datetime.now().strftime("%Y%m%d-%H:%M:%S")
        folder_name = "example" + timestamp

        terminal_command = f"""
        cd ..
        cd cm_pipeline
        python3 -m hm01.cm -i ../api/{algoIn.file_path} -o ../api/samples/{folder_name}/output.tsv -c external  -cargs ../api/cargs.json -cfile /home/tomasa/dashboard-cm/cm_pipeline/hm01/clusterers/external_clusterers/sbm_wrapper.py
        ..
        """

        os.system(terminal_command)

        eturn "Success"


    else:
        json_path, input_dir =  algoIn.callJSON()

        terminal_command = f"""
        cd ..
        cd cm_pipeline
        python -m main ../api/{json_path}.json
        """

        input_dir += "-" + datetime.now().strftime("%Y%m%d-%H:%M:%S")
        os.system(terminal_command)

        algoIn.postTreatment(input_dir)

        return "Success"
   