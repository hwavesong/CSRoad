## Install Python From Source

1. Install required dependencies.

sudo apt-get update
sudo apt-get install gdebi-core

sudo apt-get install \
    curl \
    gcc \
    libbz2-dev \
    libev-dev \
    libffi-dev \
    libgdbm-dev \
    liblzma-dev \
    libncurses-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    make \
    tk-dev \
    wget \
    zlib1g-dev

export PYTHON_VERSION=3.11.9
export PYTHON_MAJOR=3

2. Download and extract Python

curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz
tar -xvzf Python-${PYTHON_VERSION}.tgz
cd Python-${PYTHON_VERSION}

./configure \
    --prefix=/opt/python/${PYTHON_VERSION} \
    --enable-shared \
    --enable-optimizations \
    --enable-ipv6 \
    LDFLAGS=-Wl,-rpath=/opt/python/${PYTHON_VERSION}/lib,--disable-new-dtags
make
sudo make install

3. Install pip

curl -O https://bootstrap.pypa.io/get-pip.py
sudo /opt/python/${PYTHON_VERSION}/bin/python${PYTHON_MAJOR} get-pip.py

4. Verify Python installation

/opt/python/${PYTHON_VERSION}/bin/python${PYTHON_MAJOR} --version

5. Add Python to the system PATH

PATH=/opt/python/<PYTHON-VERSION>/bin/:$PATH


