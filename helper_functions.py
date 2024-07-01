import json


def generate_json(algorithm, raw_params):

    formated_param = [raw_params]

    pipeline = {
            "title": "example",
            "name": "example",
            "input_file": "network.tsv",
            "output_dir": "samples/",
            "algorithm": algorithm,
            "params": formated_param,
            "stages": [
                {
                    "name": "clustering",
                    "parallel_limit": 2
                },        
                {
                    "name": "connectivity_modifier",
                    "memprof": False,
                    "threshold": "1log10",
                    "nprocs": 1,
                    "quiet": True
                }
            ]
        }

    with open("./cm_pipeline/pipeline.json", "w") as f:
        json.dump(pipeline, f)