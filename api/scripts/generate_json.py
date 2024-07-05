import json

def generate_json(algorithm, raw_params):

    formated_param = [raw_params]

    pipeline = {
            "title": "example",
            "name": "example",
            "input_file": "network.tsv",
            "output_dir": "../cm_pipeline/samples",
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
            "name": "filtering",
            "scripts": [
                "./scripts/subset_graph_nonetworkit_treestar.R",
                "./scripts/make_cm_ready.R"
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
                "./scripts/post_cm_filter.R"
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
    
    # pipeline = {
    #     "title": "example",
    #     "name": "example",
    #     "input_file": "network.tsv",
    #     "output_dir": "../cm_pipeline/samples/",
    #     "algorithm": "leiden",
    #     "params": [{
    #         "res": 0.001,
    #         "i": 2
    #     }],
    #     "stages": [
    #         {
    #             "name": "cleanup"
    #         },
    #         {
    #             "name": "clustering",
    #             "parallel_limit": 2
    #         },       

    #         {
    #             "name": "filtering",
    #             "scripts": [
    #                 "./scripts/subset_graph_nonetworkit_treestar.R",
    #                 "./scripts/make_cm_ready.R"
    #             ]
    #         },
    #         {
    #             "name": "connectivity_modifier",
    #             "memprof": False,
    #             "threshold": "1log10",
    #             "nprocs": 4,
    #             "quiet": True
    #         },
    #         {
    #             "name": "filtering",
    #             "scripts": [
    #                 "./scripts/post_cm_filter.R"
    #             ]
    #         },
    #         {
    #             "name": "stats",
    #             "parallel_limit": 2,
    #             "universal_before": False,
    #             "summarize": False
    #         }

    #     ]
    # }

    with open("../api/pipeline_test.json", "w") as f:
        json.dump(pipeline, f)

    return "pipeline_test"