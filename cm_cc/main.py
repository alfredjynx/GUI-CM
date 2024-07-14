import os

network = "cen"

itr = "1000"

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

terminal_command = f"""
    cd ..
    cd cm_pipeline
    Rscript ./scripts/analysis.R ../cm_cc/data/{network}/edge_list_iids.tsv   ../cm_cc/data/{network}/{network}_output_itr_{itr}_clustering.tsv   ../cm_cc/output/{network}/{network}_output_itr_{itr}_cc.tsv
"""


os.system(terminal_command)


terminal_command = f"""
    cd ..
    cd cm_pipeline
    Rscript ./scripts/analysis.R ../cm_cc/data/{network}/edge_list_iids.tsv   ../cm_cc/output/{network}/stats/{network}_output_itr_{itr}_cc_stats.tsv   ../cm_cc/output/{network}/{network}_output_itr_{itr}_cc.tsv
"""


os.system(terminal_command)

terminal_command = f"""
    cd ..
    cd cm_pipeline
    Rscript ./scripts/analysis.R ../cm_cc/data/{network}/edge_list_iids.tsv   ../cm_cc/output/{network}/stats/{network}_output_itr_{itr}_wcc_stats.tsv   ../cm_cc/output/{network}/{network}_output_itr_{itr}_wcc.tsv
"""


os.system(terminal_command)
