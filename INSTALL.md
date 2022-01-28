# Installation

1. Install Git and pip3
```
sudo apt install git python3-pip # replace "apt" with your package manager
```

2. Install ABC by following [these steps](https://github.com/vlab-cs-ucsb/ABC/blob/master/INSTALL.md)

3. Download Quacky from from [the latest release on GitHub](https://github.com/vlab-cs-ucsb/quacky/releases)
```
unzip quacky.zip # the latest release's assets may be named differently
cd quacky
```

*Note: Alternatively, you can just clone Quacky from GitHub.*
```
git clone https://github.com/vlab-cs-ucsb/quacky.git
cd quacky
```

4. Install the required Python 3 packages
```
sudo pip3 install -r requirements.txt
```

## Basic Usage Example (Sanity Check)
1. Analyze a simple AWS IAM policy
```
cd src
python3 quacky.py -p1 ../samples/iam/exp_single/iam_simplest_policy/policy.json -b 100
```

`iam_simplest_policy/policy.json` is shown below.
```
$ cat ../samples/iam/exp_single/iam_simplest_policy/policy.json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "*",
      "Resource": "*"
    }
  ]
}
```

Quacky's output is shown below.
```
Policy 1
╒═════════════════╤════════════════════╕
│ Solve Time (ms) │ 12.1562            │
├─────────────────┼────────────────────┤
│ Satisfiability  │ sat                │
├─────────────────┼────────────────────┤
│ Count Time (ms) │ 2.97606            │
├─────────────────┼────────────────────┤
│ lg(requests)    │ 1600.0112931262822 │
╘═════════════════╧════════════════════╛

```
