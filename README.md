# squatsmart - insight

## AWS

Instructions to get install and run squatsmart on an AWS EC2 instance.

Start with the [AWS Ubuntu Deep Learning Base AMI](https://aws.amazon.com/marketplace/pp/B07Y3VDBNS?qid=1591551938734&sr=0-1&ref_=srh_res_product_title).

Check the version of CUDA once you are logged in to the instance:

```
ubuntu@ip-172-31-25-30:~$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2018 NVIDIA Corporation
Built on Sat_Aug_25_21:08:01_CDT_2018
Cuda compilation tools, release 10.0, V10.0.130
```

Update packages:
```
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
python3-dev python3-pip git g++ wget make libprotobuf-dev protobuf-compiler libopencv-dev \
libgoogle-glog-dev libboost-all-dev libcaffe-cuda-dev libhdf5-dev libatlas-base-dev
```

replace cmake as old version has CUDA variable bugs
```
wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0-Linux-x86_64.tar.gz
mkdir ~/opt && tar xzf cmake-3.16.0-Linux-x86_64.tar.gz -C ~/opt
```

add this to your `$PATH`
```
export PATH="~/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"
```

and restart your bash shell.


Clone `openpose`:

```
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
```

and install pre-requisities:
```
cd openpose
sudo bash ./scripts/ubuntu/install_deps.sh
```

then install using
```
mkdir -p build
cmake -DBUILD_PYTHON=ON .. 
make -j `nproc`
``