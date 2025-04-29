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
st.session_state.param = {}
clustering = False


uploaded_file = st.sidebar.file_uploader(
    'Edge List File'
)

if uploaded_file is not None:

    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    date = "-".join(str(datetime.now()).split('.')[0].split(' '))


    os.makedirs("../api/data/", exist_ok=True)

    with open(f'../api/data/file_{date}.tsv', 'w') as fd:
        stringio.seek(0)
        shutil.copyfileobj(stringio, fd)

    file_path = f'./data/file_{date}.tsv'


clustering = st.sidebar.checkbox(
    "Upload Existing Clustering?", value=False
)

if clustering:

    cluster_uploaded_file = st.sidebar.file_uploader(
        'Existing Clustering File'
    )

    if cluster_uploaded_file is not None:

        stringio = StringIO(cluster_uploaded_file.getvalue().decode("utf-8"))

        date = "-".join(str(datetime.now()).split('.')[0].split(' '))


        os.makedirs("../api/clustering/", exist_ok=True)

        with open(f'../api/clustering/file_{date}.tsv', 'w') as fd:
            stringio.seek(0)
            shutil.copyfileobj(stringio, fd)

        st.session_state.param["existing_clustering"] = f'clustering/file_{date}.tsv'


algorithm = st.sidebar.selectbox(
    'Algorithm',
    ('Leiden-CPM', 'Leiden-Mod', 'Infomap','Stochastic Block Model (SBM)')
)

if algorithm == 'Leiden-CPM':
    resolution = st.sidebar.number_input(label= "Resolution", value= 0.001, format="%.3f", min_value=0.0, step=0.001)
    iteration = st.sidebar.number_input(label= "Iterations", min_value=1, max_value=100, step=1, value=1)
    st.session_state.param["res"] = float(resolution)
    st.session_state.param["i"] = int(iteration)
    clustering_algorithm = 'leiden'
elif algorithm == 'Leiden-Mod':
    iteration = st.sidebar.number_input(label= "Iterations", min_value=1, max_value=100, step=1, value=1)
    clustering_algorithm = 'leiden_mod'
    if iteration is not None:
        st.session_state.param["i"] = int(iteration)
elif algorithm == 'Infomap':
    clustering_algorithm = 'infomap'
elif algorithm == "Stochastic Block Model (SBM)":
    
    block_state = st.sidebar.selectbox(
        "Select block state:",
        options=["Non Nested", "Planted Partition Model"]
    )
    
    block_state_dict = {"Non Nested":"non_nested_sbm", "Planted Partition Model": "planted_partition_model"}

    if block_state == "Non Nested":
        degree_corrected = st.sidebar.checkbox(
            "Degree corrected", value=False
        )
        st.session_state.param["degree_corrected"] = degree_corrected 
        
    st.session_state.param["block_state"] = block_state_dict[block_state]
    clustering_algorithm = 'sbm'

post_treatment = st.sidebar.selectbox(
    'Post Clustering Treatment',
    ('None', 'CM', 'CM-CC', 'CM-WCC') if not clustering else ('CM', 'CM-CC', 'CM-WCC')
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
    'Post Clustering Filter',
    ('ON', 'OFF')
)

if "pipeline_complete" not in st.session_state:
    st.session_state.pipeline_complete = False
if "df" not in st.session_state:
    st.session_state.df = None
if "df_stats" not in st.session_state:
    st.session_state.df_stats = None

if st.button("Run CM Pipeline") and len(file_path) > 0:
    
    print(st.session_state.param)

    st.session_state.pipeline_complete = False  # Reset state
    
    data = {
        "algo_name" : clustering_algorithm,
        "params": st.session_state.param,
        "file_path": file_path,
        "post_treatment": st.session_state.post_treatment,
        "filter_select": filter_select == "ON"
    }
    res = requests.post('http://backend:8000/pipeline', data= json.dumps(data))

    if res.status_code == 201:
        st.session_state.pipeline_complete = True
        
        print(res.json()["path"])

        try:
            st.session_state.df = pd.read_csv(res.json()["path"], sep="\t", header=None)
            if res.json()["stats"] != "":
                st.session_state.df_stats = pd.read_csv(res.json()["stats"])
        except:
            st.error("Pipeline executed successfully, but the filtering stage left a blank document")
            st.session_state.pipeline_complete = False
            
    else:
        st.error(f"Error: Unable to execute the pipeline. Status Code: {res.status_code}")
        st.write(res.text)  
    
    
if st.session_state.pipeline_complete:
    st.success("Pipeline executed successfully! The resource has been created.")

    def convert_df(df):
        return df.to_csv(index=False, sep="\t", header=None).encode("utf-8")

    csv = convert_df(st.session_state.df)

    st.download_button(
        label="Download Clustering data as TSV",
        data=csv,
        file_name=clustering_algorithm + ".tsv",
        mime="text/csv",
    )

    if st.session_state.df_stats is not None and "cc" not in st.session_state.post_treatment:
        csv_stats = convert_df(st.session_state.df_stats)
        st.download_button(
            label="Download Stats data as CSV",
            data=csv_stats,
            file_name=clustering_algorithm + "_stats.csv",
            mime="text/csv",
        )
