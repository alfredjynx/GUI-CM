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
    lsb-release

RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && \
    apt-get install -y python3.10 python3.10-dev python3.10-distutils

RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1

RUN python3.10 -m pip install --no-cache-dir \
    numpy==1.26.4 \
    scipy \
    matplotlib


RUN apt-get install -y wget lsb-release && \
    wget https://downloads.skewed.de/skewed-keyring/skewed-keyring_1.1_all_$(lsb_release -s -c).deb && \
    dpkg -i skewed-keyring_1.1_all_$(lsb_release -s -c).deb && \
    echo "deb [signed-by=/usr/share/keyrings/skewed-keyring.gpg] https://downloads.skewed.de/apt $(lsb_release -s -c) main" \
    > /etc/apt/sources.list.d/skewed.list && \
    apt-get update && \
    apt-get install -y python3-graph-tool

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


WORKDIR /app/cm_pipeline
RUN ls
RUN pip install -r requirements.txt
WORKDIR /app  # Return to base


RUN pip install -r /app/requirements.txt


CMD ["bash"]
    

