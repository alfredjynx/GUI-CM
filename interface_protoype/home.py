import shutil
import streamlit as st
import os
import requests
import json
from io import StringIO
from datetime import datetime
import pandas as pd


if 'cm' not in st.session_state:
    st.session_state.cm = False

if 'param' not in st.session_state:
    st.session_state.param = {}

st.title("CM Interface")

file_path = ""

file_select = st.sidebar.selectbox(
    'File Options',
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
        'Input File'
    )

    if uploaded_file is not None:

        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        date = "-".join(str(datetime.now()).split('.')[0].split(' '))

        print(date)

        os.makedirs("../api/data/", exist_ok=True)

        with open(f'../api/data/file_{date}.tsv', 'w') as fd:
            stringio.seek(0)
            shutil.copyfileobj(stringio, fd)

        file_path = f'./data/file_{date}.tsv'


algorithm = st.sidebar.selectbox(
    'Algorithm',
    ('Leiden-CPM', 'Leiden-Mod', 'Infomap','Stochastic Block Model (SBM)')
)

if algorithm == 'Leiden-CPM':
    st.session_state.param = {}
    resolution = st.sidebar.number_input(label= "Resolution", value= 0.001, format="%f")
    iteration = st.sidebar.number_input(label= "Iterations", value= 2)
    st.session_state.param["res"] = float(resolution)
    st.session_state.param["i"] = int(iteration)
    clustering_algorithm = 'leiden'
elif algorithm == 'Leiden-Mod':
    st.session_state.param = {}
    iteration = st.sidebar.number_input(label= "Iterations", min_value=1, max_value=100, step=1, value=1)
    clustering_algorithm = 'leiden_mod'
    if iteration is not None:
        print(iteration)
        st.session_state.param["i"] = int(iteration)
elif algorithm == 'Infomap':
    st.session_state.param = {}
    clustering_algorithm = 'infomap'
elif algorithm == "Stochastic Block Model (SBM)":
    st.session_state.param = {}
    
    block_state = st.sidebar.selectbox(
        "Select block state:",
        options=["Non Nested", "Planted Partition Model"]
    )
    
    block_state_dict = {"Non Nested":"non_nested_sbm", "Planted Partition Model": "planted_partition_model"}

    degree_corrected = st.sidebar.checkbox(
        "Degree corrected", value=False
    )
    st.session_state.param["block_state"] = block_state_dict[block_state]
    st.session_state.param["degree_corrected"] = degree_corrected 
    clustering_algorithm = 'sbm'

post_treatment = st.sidebar.selectbox(
    'Post Clustering Treatment',
    ('None', 'CM', 'CM-CC', 'CM-WCC')
)

if post_treatment == "CM-CC":
    st.session_state.post_treatment = "cm-cc"
elif post_treatment == "CM-WCC":
    st.session_state.post_treatment = "cm-wcc"
elif post_treatment == "CM":
    st.session_state.post_treatment = "cm"
else:
    st.session_state.post_treatment = ""


filter_select = st.sidebar.selectbox(
    'Filter',
    ('ON', 'OFF')
)


if st.button("Run CM Pipeline"):
    
    data = {
        "algo_name" : clustering_algorithm,
        "params": st.session_state.param,
        "file_path": file_path,
        "post_treatment": st.session_state.post_treatment,
        "filter_select": filter_select == "ON"
    }
    res = requests.post('http://127.0.0.1:8000/pipeline', data= json.dumps(data))

    if res.status_code == 201:
        st.success("Pipeline executed successfully! The resource has been created.")

        df = pd.read_csv(res.json()["path"])

        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode("utf-8")

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name=clustering_algorithm+".csv",
            mime="text/csv",
        )
        
    else:
        
        st.error(f"Error: Unable to execute the pipeline. Status Code: {res.status_code}")
        st.write(res.text)  






