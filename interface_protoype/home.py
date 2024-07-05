import streamlit as st
import pandas as pd
import os
import requests
import json



if 'cm' not in st.session_state:
    st.session_state.cm = False

if 'param' not in st.session_state:
    st.session_state.param = {}

st.title("CM Interface")

input = st.sidebar.selectbox(
    'What is your input file?',
    (['network'])
)

algorithm = st.sidebar.selectbox(
    'What is your clustering algorithm?',
    ('Leiden-CPM', 'Leiden-Mod', 'IKC')
)

if algorithm == 'Leiden-CPM':
    st.session_state.param = {}
    resolution = st.sidebar.number_input(label= "resolution", value= 0.001, format="%f")
    iteration = st.sidebar.number_input(label= "iterations", value= 2)
    st.session_state.param["i"] = int(iteration)
    st.session_state.param["res"] = float(resolution)
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
        "params": st.session_state.param 
    }
    res = requests.post('http://127.0.0.1:8000/pipeline', data= json.dumps(data))
    st.write(res)






