# Overview
Lambda code for the Data Marketplace in AWS.

## Purpose
Data Marketplace is where you discover, understand, and request access to data at Duke Energy.

## Installing Rancher
- Submit a Modify AD Group Request in BAP for NAMG_RancherDesktop_Access
- Go to the Software Center
- Install Rancher Desktop Pre-Requisite
- Install Rancher Desktop
- Test by running `which docker` in your git bash terminal

## Running Docker
After installing docker locally, first run the following command if you are on a physical laptop, not the VDI:
```
rdctl set --experimental.virtual-machine.networking-tunnel=true
```
and then in the top level directory of this codebase, run:
```
./run_tests.sh
```
This will run the local test suite.

If you want to rebuild your image if a new image has been installed, you can do that by running:
```
docker-compose build --no-cache
```