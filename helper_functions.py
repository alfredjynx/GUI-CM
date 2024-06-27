import json


def generate_json(algorithm, raw_params):

    formated_param = [raw_params]

    pipeline = {    
        "title": "network",
        "name": "network",
        "input_file": "../input_data/network.tsv",
        "output_dir": "../output_files/",
        "algorithm": algorithm,
        "params": formated_param,
        "stages": [
            {
                "name": "cleanup"
            },
            {
                "name": "clustering",
            },
            {
                "name": "connectivity_modifier",
                "memprof": False,
                "threshold": "1log10",
                "nprocs": 4,
                "quiet": True
            }
        ]
    }

    with open("./cm_pipeline/pipeline.json", "w") as f:
        json.dump(pipeline, f)