#!/bin/sh
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
python3-dev python3-pip git g++ wget make libprotobuf-dev protobuf-compiler libopencv-dev \
libgoogle-glog-dev libboost-all-dev libcaffe-cuda-dev libhdf5-dev libatlas-base-dev

wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0-Linux-x86_64.tar.gz
mkdir ~/opt && tar xzf cmake-3.16.0-Linux-x86_64.tar.gz -C ~/opt

git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

export PATH="~/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"

cd openpose
sudo bash ./scripts/ubuntu/install_deps.sh

mkdir -p build
cmake -DBUILD_PYTHON=ON .. 
make -j `nproc`