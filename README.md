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
