import os
from pathlib import Path

def get_file_sbm(directory):

    files = [
        "S3_example_sbm.degree_correctedFalse_block_statenon_nested_sbm_make_cm_ready.R.tsv",
        # "S3_example_sbm.degree_correctedTrue_block_stateplanted_partition_model_make_cm_ready.R.tsv",
        "S3_example_sbm.block_stateplanted_partition_model_make_cm_ready.R.tsv",
        # "S3_example_sbm.degree_correctedFalse_block_stateplanted_partition_model_make_cm_ready.R.tsv",
        "S3_example_sbm.degree_correctedTrue_block_statenon_nested_sbm_make_cm_ready.R.tsv",
    ]

    # List files in the directory
    directory_files = os.listdir(directory)

    # Check which file is present in the directory
    present_files = [file for file in files if file in directory_files]

    return present_files[0]


def get_dir_name_sbm(directory):

    # List files in the directory
    directory_files = os.listdir(directory)

    # Check which file is present in the directory
    # present_files = [file for file in directory_files if "sbm_" in file]
    # for file in directory_files:
    #     print(f"checking files to see if dir {directory}/{file}")
    present_files = [file for file in directory_files if Path(f"{directory}/{file}").is_dir() and "sbm_" in file]

    return present_files[0]


