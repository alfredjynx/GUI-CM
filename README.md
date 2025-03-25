# CM API

## How to Set Up, Run the Backend API and Run the Interface Locally

### Requirements

- **Operating System**: macOS or Linux
- **Python**: Version 3.9 or higher
- **CMake**: Version 3.2.0 or higher
- **GCC**: Any version (used version in analysis: 9.2.0)
- **R**: With the following packages:
  - `data.table`
  - `feather`


# Local Setup Instructions

  1. **Create and Activate a Virtual Environment in the main Directory**
  
      Ensure that your terminal is in dashboard-cm directory
    
      Create a virtual environment:
      ```bash
      python -m venv env --system-site-packages
      ```
      OR
      ```bash
      python3 -m venv env --system-site-packages
      ```
      Activate the environment:
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
      ```

      Install Graph Tool:
      ```bash
        sudo apt install -y wget lsb-release && \
        wget https://downloads.skewed.de/skewed-keyring/skewed-keyring_1.1_all_$(lsb_release -s -c).deb && \
        dpkg -i skewed-keyring_1.1_all_$(lsb_release -s -c).deb && \
        echo "deb [signed-by=/usr/share/keyrings/skewed-keyring.gpg] https://downloads.skewed.de/apt $(lsb_release -s -c) main" \
        > /etc/apt/sources.list.d/skewed.list && \
        apt-get update && \
        apt-get install -y python3-graph-tool
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

      Navigate to the `interface_prototype` directory
          
        Install the requiremnts
        ```bash
        pip install -r requirements.txt
        ```

        ```bash
        streamlit run home.py
        ```

Now the interface server should be running locally.



## Docker Setup - 

  1. **Change Branches on Repository**

      The repository includes a branch called Docker, that has all files needed to automatically install and run the GUI inside a Docker Container.
      
      Ensure your local repo is in the Docker branch by running this command:
      ```bash
      git checkout Docker
      ```


  1. **Update Submodule**

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
  
  2. **Initialize and Run Docker Container/Image**

      Run the `docker-compose` file with this command.
      ```bash
      docker compose up --build --force-recreate
      ```

      This will recreate the Image any time you run it, if you want to maintain the original image, run this:
      ```bash
      docker compose up --build -d
      ```