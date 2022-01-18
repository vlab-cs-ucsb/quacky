# Installation

1. [Install ABC](https://github.com/vlab-cs-ucsb/ABC/blob/master/INSTALL.md)

*Note: Build the `policy` branch, not `master`!*
```
git clone --recursive https://github.com/vlab-cs-ucsb/ABC.git
git checkout policy
```
2. Clone Quacky
```
git clone git@github.com:vlab-cs-ucsb/quacky.git
cd quacky
```
3. Install the required Python 3 packages
```
sudo pip3 install -r requirements.txt
```

## Basic Usage Example (Sanity Check)
1. Analyze a simple AWS IAM policy
```
cd src
python3 quacky.py -p1 ../samples/iam/exp_single/iam_simplest_policy/policy.json
```

## Copy of Accepted Paper

- [Quantifying Permissiveness of Access Control Policies (PDF)](../Quantifying%20Permissiveness%20of%20Access%20Control%20Policies.pdf)

*Note: This is the accepted version of the paper, not the camera-ready version!*
