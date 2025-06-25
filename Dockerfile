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
    git \
    libssl-dev \
    libcurl4-openssl-dev \
    cmake \
    gcc \
    g++ \
    r-base \
    libharfbuzz-dev \
    libfribidi-dev \
    libfontconfig1-dev

ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH

RUN ARCH=$(uname -m) && \
    if [ "$ARCH" = "x86_64" ]; then \
        wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh; \
    elif [ "$ARCH" = "aarch64" ]; then \
        wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh -O /tmp/miniconda.sh; \
    fi && \
    bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh && \
    conda clean -afy


RUN conda create -n gt python=3.10 -c conda-forge
RUN conda config --add channels conda-forge
RUN conda config --set channel_priority strict
RUN conda install -n gt graph-tool graph-tool-base
RUN conda install -n gt pip


RUN apt-get update && apt-get install -y \
    gcc-10 \
    g++-10
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 800 --slave /usr/bin/g++ g++ /usr/bin/g++-10

RUN R -e "install.packages(c('data.table', 'feather'), repos='http://cran.rstudio.com/')"


WORKDIR /app
COPY . /app
WORKDIR /app  # Return to base
RUN conda run -n gt pip install networkit==11.0.1
RUN conda run -n gt pip install -r /app/requirements.txt
WORKDIR /app/cm_pipeline
RUN conda run -n gt pip install -r /app/cm_pipeline/requirements.txt

ENV KMP_DUPLICATE_LIB_OK=True
ENV OMP_NUM_THREADS=1
