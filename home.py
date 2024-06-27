import streamlit as st
import pandas as pd
import os


if 'cm' not in st.session_state:
    st.session_state.cm = False

st.title("CM Interface")

input = st.sidebar.selectbox(
    'What is your input file?',
    ('network', 'network and clustering')
)

algorithm = st.sidebar.selectbox(
    'What is your clustering algorithm?',
    ('Leiden-CPM', 'Leiden-Mod', 'IKC')
)

if algorithm == 'Leiden-CPM':
    resolution = st.sidebar.number_input(label= "resolution", value=0.01, min_value=0., max_value=1.0)
    # st.sidebar.number_input(label= "iterations")
    clustering_algorithm = 'leiden'
elif algorithm == 'Leiden-Mod':
    st.sidebar.number_input(label= "iterations")
    clustering_algorithm = 'leiden_mod'
elif algorithm == 'IKC':
    st.sidebar.number_input(label= "k-core value")
    clustering_algorithm = 'ikc'

if input == 'network':
    network = st.file_uploader(label="Input your network file here", type=['csv', 'tsv'])
    if network:
        pd.read_csv(network).to_csv("input_data/network.tsv", index= False)
    clustering = None
else:
    network = st.file_uploader(label="Input your network file here", type=['csv', 'tsv'])
    clustering = st.file_uploader(label="Input your clustering file here", type=['csv', 'tsv'])
    if network and clustering:
        pd.read_csv(network).to_csv("input_data/network.tsv", index= False)
        pd.read_csv(clustering).to_csv("input_data/clustering.tsv", index= False)
    
input_network = 'input_network.tsv' 
output_file = 'output.tsv'
connectivity_threshold = '1log10'

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read().encode('utf-8')

command_terminal = f"python -m hm01.cm -i input_data/network.tsv -c {clustering_algorithm} -g {resolution} -t 1log10 -n 32 -o output_data/output.tsv"

if clustering:
    command_terminal  += " -e input_data/clustering.tsv"


if st.button("Run CM Pipeline"):
    with st.spinner():
        os.system(command_terminal)

    st.session_state.cm = True


if st.session_state.cm:
    st.title("Results") 
    if os.path.exists('output_data/output.tsv'):
        df = pd.read_csv('output_data/output.tsv')
        st.download_button('Download output.tsv', df.to_csv(index=False).encode('utf-8') , 'output.tsv')
        st.download_button('Download output.tsv.after.json', read_json('output_data/output.tsv.after.json'), 'output.tsv.after.json')
        st.download_button('Download output.tsv.before.json', read_json('output_data/output.tsv.before.json'), 'output.tsv.before.json')
        st.download_button('Download CSV output.tsv.tree.json',read_json('output_data/output.tsv.tree.json'), 'output.tsv.tree.json')
    else:
        st.title("No results yet")
