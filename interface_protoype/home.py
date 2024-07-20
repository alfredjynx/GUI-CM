import shutil
import streamlit as st
import pandas as pd
import os
import requests
import json
from io import StringIO
from datetime import datetime


if 'cm' not in st.session_state:
    st.session_state.cm = False

if 'param' not in st.session_state:
    st.session_state.param = {}

st.title("CM Interface")

file_path = ""

file_select = st.sidebar.selectbox(
    'File Read Options',
    ('Relative Path', 'Upload','Default')
)

if file_select == "Relative Path":
    file_path = st.sidebar.text_input(
        "Enter the Relative Path Here! 👇"
    )

    if file_path:
        st.write("You entered: ", file_path)

elif file_select == 'Upload':

    uploaded_file = st.sidebar.file_uploader(
        'What is your input file?'
    )

    if uploaded_file is not None:

        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        date = "-".join(str(datetime.now()).split('.')[0].split(' '))

        print(date)

        with open(f'../api/data/file_{date}.tsv', 'w') as fd:
            stringio.seek(0)
            shutil.copyfileobj(stringio, fd)

        file_path = f'./data/file_{date}.tsv'


algorithm = st.sidebar.selectbox(
    'What is your clustering algorithm?',
    ('Leiden-CPM', 'Leiden-Mod', 'IKC')
)

if algorithm == 'Leiden-CPM':
    st.session_state.param = {}
    resolution = st.sidebar.number_input(label= "resolution", value= 0.001, format="%f")
    iteration = st.sidebar.number_input(label= "iterations", value= 2)
    st.session_state.param["res"] = float(resolution)
    st.session_state.param["i"] = int(iteration)
    clustering_algorithm = 'leiden'
elif algorithm == 'Leiden-Mod':
    st.session_state.param = {}
    st.sidebar.number_input(label= "iterations")
    iteration = clustering_algorithm = 'leiden_mod'
    st.session_state.param["i"] = int(iteration)
elif algorithm == 'IKC':
    st.session_state.param = {}
    k = st.sidebar.number_input(label= "k-core value")
    st.session_state.param["k"] = float(k)
    clustering_algorithm = 'ikc'

# if input == 'network':
#     network = st.file_uploader(label="Input your network file here", type=['csv', 'tsv'])
#     if network:
#         pd.read_csv(network).to_csv("cm_pipeline/network.tsv", index= False)
#     clustering = None
# else:
#     network = st.file_uploader(label="Input your network file here", type=['csv', 'tsv'])
#     clustering = st.file_uploader(label="Input your clustering file here", type=['csv', 'tsv'])
#     if network and clustering:
#         pd.read_csv(network).to_csv("input_data/network.tsv", index= False)
#         pd.read_csv(clustering).to_csv("input_data/clustering.tsv", index= False)
    


if st.button("Run CM Pipeline"):
    
    data = {
        "algo_name" : clustering_algorithm,
        "params": st.session_state.param,
        "file_path": file_path
    }
    res = requests.post('http://127.0.0.1:8000/pipeline', data= json.dumps(data))
    st.write(res)






