import json

def generate_json(algorithm, raw_params, input_file):

    print(algorithm)

    formated_param = [raw_params]

    print(formated_param)
    
    pipeline = {
        "title": "example",
        "name": "example",
        "input_file": input_file,
        "output_dir": "../api/samples/",
        "algorithm": algorithm,
        "params": formated_param,
        "stages": [
            # 1
            {
                "name": "cleanup"
            },
            # 2
            {
                "name": "clustering",
                "parallel_limit": 2
            },
            # 3
            {
                "name": "stats",
                "parallel_limit": 2
            }, 
            # 4
            {
                "name": "filtering",
                "scripts": [
                    "../cm_pipeline/scripts/subset_graph_nonetworkit_treestar.R",
                    "../cm_pipeline/scripts/make_cm_ready.R"
                ]
            },
            # 5
            # 6
            {
                "name": "filtering",
                "scripts": [
                    "../cm_pipeline/scripts/post_cm_filter.R"
                ]
            },
            # 7
            {
                "name": "stats",
                "parallel_limit": 2,
                "universal_before": False,
                "summarize": False
            }

        ]
    }


    connectivity_modifier = {
    "name": "connectivity_modifier",
    "memprof": False,
    "threshold": "1log10",
    "nprocs": 4,
    "quiet": True
    }
    
    if algorithm == "infomap":
        connectivity_modifier["clusterer_file"]="../../../cm_pipeline/hm01/clusterers/external_clusterers/infomap_wrapper.py"
    elif algorithm == "sbm":
        connectivity_modifier["clusterer_file"]="../../../cm_pipeline/hm01/clusterers/external_clusterers/sbm_wrapper.py"

    pipeline["stages"].insert(4,connectivity_modifier)


    with open("../api/pipeline_test.json", "w") as f:
        json.dump(pipeline, f)

    return "pipeline_test", pipeline["output_dir"] + pipeline["name"]