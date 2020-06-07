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

Update packages and install openpose:

```
./install_deps.sh
```

Put this in `~/.bashrc`

```
export PATH="${HOME}/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"
export PYTHONPATH="${HOME}/openpose/build/python/openpose:${PYTHONPATH}"
```
