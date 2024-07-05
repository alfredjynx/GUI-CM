import json

def generate_json(algorithm, raw_params):

    print(algorithm)

    formated_param = [raw_params]

    print(formated_param)
    
    pipeline = {
        "title": "example",
        "name": "example",
        "input_file": "network.tsv",
        "output_dir": "../api/samples/",
        "algorithm": algorithm,
        "params": formated_param,
        "stages": [
            {
                "name": "cleanup"
            },
            {
                "name": "clustering",
                "parallel_limit": 2
            },
            {
                "name": "stats",
                "parallel_limit": 2
            }, 
            {
                "name": "filtering",
                "scripts": [
                    "../cm_pipeline/scripts/subset_graph_nonetworkit_treestar.R",
                    "../cm_pipeline/scripts/make_cm_ready.R"
                ]
            },
            {
                "name": "connectivity_modifier",
                "memprof": False,
                "threshold": "1log10",
                "nprocs": 4,
                "quiet": True
            },
            {
                "name": "filtering",
                "scripts": [
                    "../cm_pipeline/scripts/post_cm_filter.R"
                ]
            },
            {
                "name": "stats",
                "parallel_limit": 2,
                "universal_before": False,
                "summarize": False
            }

        ]
    }

    with open("../api/pipeline_test.json", "w") as f:
        json.dump(pipeline, f)

    return "pipeline_test"