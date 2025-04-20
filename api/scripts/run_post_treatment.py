import os

def apply(treatment, edge_list_path, cluster_path, output_file_path):
    if treatment == "cc":

        terminal_command = f"""
            python3 -m hm01.cm -i {edge_list_path} -e {cluster_path} -o {output_file_path} -c nop --threshold 0.1 --nprocs 4
        """

        os.system(terminal_command)

    elif treatment == "wcc":

        terminal_command = f"""
            python3 -m hm01.cm -i {edge_list_path} -e {cluster_path} -o {output_file_path} -c nop --threshold 1log10 --nprocs 4
        """
        os.system(terminal_command)
    
