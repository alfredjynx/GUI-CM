FROM python:3.10-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    build-essential \
    cmake \
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
    python3-graph-tool && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


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
    gcc \
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

RUN python -m pip install --upgrade pip


WORKDIR /app/cm_pipeline
RUN ls
RUN pip install -r requirements.txt
WORKDIR /app  # Return to base


RUN pip install -r /app/requirements.txt


CMD ["bash"]
    

