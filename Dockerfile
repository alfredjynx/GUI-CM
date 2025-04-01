FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    software-properties-common \
    wget \
    curl \
    gnupg \
    build-essential \
    cmake \
    libboost-all-dev \
    libcgal-dev \
    libcgal-qt5-dev \
    libeigen3-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libxml2-dev \
    libxslt-dev \
    libyaml-dev \
    libffi-dev \
    graphviz \
    lsb-release \
    bzip2 \
    ca-certificates \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git

ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh && \
    conda clean -afy

RUN conda create -y -n gt -c conda-forge python=3.10 graph-tool && \
    conda run -n gt pip install --no-cache-dir \
        numpy==1.26.4 \
        scipy \
        matplotlib && \
    conda clean -afy


RUN apt-get update && apt-get install -y \
    gcc-10 \
    g++-10

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 800 --slave /usr/bin/g++ g++ /usr/bin/g++-10

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    wget \
    curl \
    gnupg \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    zlib1g-dev \
    cmake \
    # gcc \
    g++ \
    git \
    r-base \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    libssl-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libharfbuzz-dev \
    libfribidi-dev \
    libfontconfig1-dev \
    r-base \
    && R -e "install.packages(c('data.table', 'feather'), repos='http://cran.rstudio.com/')"


WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

SHELL ["conda", "run", "-n", "gt", "/bin/bash", "-c"]

WORKDIR /app/cm_pipeline
RUN ls
RUN pip install -r requirements.txt
WORKDIR /app  # Return to base


RUN pip install -r /app/requirements.txt


ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "gt"]
CMD ["bash"]
    

