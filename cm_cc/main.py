import os

network = "orkut"

itr = "100"

terminal_command = f"""
    cd ..
    cd cm_pipeline
    python3 -m hm01.cm -i ../cm_cc/data/{network}/edge_list_iids.tsv -e ../cm_cc/data/{network}/{network}_output_itr_{itr}_clustering.tsv  -o ../cm_cc/output/{network}/{network}_output_itr_{itr}_cc.tsv -c nop --threshold 0.1 --nprocs 4 --quiet
"""


os.system(terminal_command)


terminal_command = f"""
    cd ..
    cd cm_pipeline
    python3 -m hm01.cm -i ../cm_cc/data/{network}/edge_list_iids.tsv -e ../cm_cc/data/{network}/{network}_output_itr_{itr}_clustering.tsv  -o ../cm_cc/output/{network}/{network}_output_itr_{itr}_wcc.tsv -c nop --threshold 1log10 --nprocs 4 --quiet
"""


os.system(terminal_command)

# terminal_command = '''
#     cd ..
#     cd cm_pipeline
#     python3 -m hm01.cm -i ../cm_cc/data/test/network.tsv -e ../cm_cc/data/test/clustering.tsv -o ../cm_cc/output/test/output.tsv -c nop --threshold 0.1 --nprocs 4 --quiet
# '''

# os.system(terminal_command)