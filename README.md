# CM API

## How to Set Up and Run the Backend API

### Requirements

- **Operating System**: macOS or Linux
- **Python**: Version 3.9 or higher
- **CMake**: Version 3.2.0 or higher
- **GCC**: Any version (used version in analysis: 9.2.0)
- **R**: With the following packages:
  - `data.table`
  - `feather`

### Step-by-Step Setup

### Clone the Repository
```bash
git clone https://github.com/alessitomas/ISE-workflow
```
```bash
cd ISE-workflow
```
## Setup Instructions

### Initialize and Update Submodule

The repository includes a submodule cm_pipeline that needs initialization.
```bash
git submodule init
```
```bash
git submodule update
```

### Create and Activate a Virtual Environment
Ensure you have Python 3.10 installed before proceeding
```bash
python3.10 -m venv env
```
```bash
source env/bin/activate 
```

### Install cm_pipeline Requirements
Make sure to be in the cm_pipeline directory
```bash
cd cm_pipeline
```
Install the requiremnts
```bash
pip install -r requirements.txt
```




1. **Create a Virtual Environment and Install Requirements for CM Pipeline**

    Navigate to the `cm_pipeline` directory:
    ```bash
    cd cm_pipeline
    ```

    Install the requirements:
    ```bash
    pip install -r requirements.txt && pip install .
    ```

2. **Install Backend API Requirements**

    Navigate to the `api` directory:
    ```bash
    cd api
    ```

    Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Backend Server Locally**

    Within the `api` directory, start the backend server:
    ```bash
    uvicorn main:app --reload
    ```

Now your environment is set up and the backend server should be running locally.
