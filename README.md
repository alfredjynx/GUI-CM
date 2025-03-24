# CM API

## How to Set Up, Run the Backend API and Run the Interface

### Requirements

- **Operating System**: macOS or Linux
- **Python**: Version 3.9 or higher
- **CMake**: Version 3.2.0 or higher
- **GCC**: Any version (used version in analysis: 9.2.0)
- **R**: With the following packages:
  - `data.table`
  - `feather`


## Setup Instructions

  1. **Create and Activate a Virtual Environment in the main Directory**
  
      Ensure that your terminal is in dashboard-cm directory
    
      Create a virtual enviroment:
      ```bash
      python -m venv env --system-site-packages
      ```
      OR
      ```bash
      python3 -m venv env --system-site-packages
      ```
      Activate the enviroment:
      ```bash
      source env/bin/activate 
      ```

  2. **Installing Graph-Tool**
    
      This GUI requires the use of Graph-Tool for SBM.
      
      Ensure your terminal has the venv activated and is in the base of the repo, and install Graph-Tool and its dependencies:
      ```bash
        sudo apt update
        sudo apt install python3-pip python3-dev \
        build-essential cmake \
        libboost-all-dev \
        libcgal-dev \
        libcgal-qt5-dev \
        libeigen3-dev \
        zlib1g-dev \
        libbz2-dev \
        liblzma-dev \
        python3-numpy \
        python3-scipy \
        python3-matplotlib \
        graphviz \
        libxml2-dev \
        libxslt-dev \
        libyaml-dev \
        libffi-dev \
        python3-graph-tool
      ```
      Verify the instalation:
      ```bash
      python3 -c "import graph_tool.all as gt; print(gt.__version__)"
      ```


  3. **Initialize and Update Submodule**
    
      The repository includes a submodule cm_pipeline that needs initialization.
      
      Ensure your terminal is in the cm_pipeline directory:
      ```bash
      cd cm_pipeline
      ```
      Initialize the submodule:
      ```bash
      git submodule init
      ```
      Update the submodule:
      ```bash
      git submodule update
      ```

      ```bash
      git submodule update --init --recursive  
      ```

  4. **Install cm_pipeline Requirements**
   
      Navigate to the `cm_pipeline` directory:
    
      Install the requiremnts
      ```bash
      pip install -r requirements.txt
      ```

  5. **Install Requirements**
  
      Navigate to the base directory:
      
      Install the requiremnts
      ```bash
      pip install -r requirements.txt
      ```


  6. **Run the Backend Server Locally**

    Within the `api` directory, start the backend server:
    ```bash
    uvicorn main:app --reload
    ```

Now your environment is set up and the backend server should be running locally.

  7. **Run the Interface Server Locally**

   Navigate to the `interface_protoype` directory
      
    Install the requiremnts
    ```bash
    pip install -r requirements.txt
    ```

     ```bash
    streamlit run home.py
    ```

Now the interface server should be running locally.
