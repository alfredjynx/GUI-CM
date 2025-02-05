import json

def generate_json(algorithm, raw_params, input_file, include_cm, filtering):

    

    formated_param = [raw_params]

    
    
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
            # 4 Possible Filtering
            # 5 Possible CM treatment
            # 6 Possible pos CM filter

            # 7
            {
                "name": "stats",
                "parallel_limit": 2,
                "universal_before": False,
                "summarize": False
            }

        ]
    }
    
    
    if filtering:
        
        filtering_dict =    {
        "name": "filtering",
        "scripts": [
            "../cm_pipeline/scripts/subset_graph_nonetworkit_treestar.R",
            "../cm_pipeline/scripts/make_cm_ready.R"
        ]
        }
        
        pipeline["stages"].insert(3,filtering_dict)


    if include_cm:
        connectivity_modifier = {
        "name": "connectivity_modifier",
        "memprof": False,
        "threshold": "1log10",
        "nprocs": 4,
        "quiet": True
        }
        
        filter_pos_cm =   {
                "name": "filtering",
                "scripts": [
                    "../cm_pipeline/scripts/post_cm_filter.R"
                ]
                }

        if algorithm == "infomap":
            connectivity_modifier["clusterer_file"]="../../../cm_pipeline/hm01/clusterers/external_clusterers/infomap_wrapper.py"
        elif algorithm == "sbm":
            connectivity_modifier["clusterer_file"]="../../../cm_pipeline/hm01/clusterers/external_clusterers/sbm_wrapper.py"

        pipeline["stages"].insert(4,connectivity_modifier)
        pipeline["stages"].insert(5,filter_pos_cm)


    with open("../api/pipeline_test.json", "w") as f:
        json.dump(pipeline, f)

    return "pipeline_test", pipeline["output_dir"] + pipeline["name"]