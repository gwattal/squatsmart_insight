#!/bin/sh
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
	python3-dev python3-pip git g++ wget make libprotobuf-dev protobuf-compiler libopencv-dev \
	libgoogle-glog-dev libboost-all-dev libcaffe-cuda-dev libhdf5-dev libatlas-base-dev

# Install a newer version of cmake in the ~/opt directory
cd ~ && wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0-Linux-x86_64.tar.gz
mkdir ~/opt && tar xzf ~/cmake-3.16.0-Linux-x86_64.tar.gz -C ~/opt
rm ~/cmake-3.16.0-Linux-x86_64.tar.gz
export PATH="${HOME}/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"

git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
cd openpose
sudo bash ./scripts/ubuntu/install_deps.sh

mkdir -p build
cmake -DBUILD_PYTHON=ON .. 
# Running this a second time is needed since the models might not be downloaded
cmake -DBUILD_PYTHON=ON .. 
make -j `nproc`

echo "Make sure models are downloaded"