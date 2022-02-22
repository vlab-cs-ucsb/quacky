# Quacky

Quacky quantitatively assesses the (relative) permissiveness of access control policies for the cloud. It

1. translates policies into constraint formulas that conform to the [SMT-LIB 2](http://smtlib.cs.uiowa.edu/language.shtml) standard, and
2. counts models satisfying the formulas using the model counting constraint solver [ABC](https://github.com/vlab-cs-ucsb/ABC). 

Quacky supports access control policies written in the following policy languages:

1. [Amazon Web Services (AWS) Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
2. [Microsoft Azure](https://docs.microsoft.com/en-us/azure/role-based-access-control/overview)
3. [Google Cloud Platform (GCP)](https://cloud.google.com/iam)

## Getting Quacky
You can download the Quacky ICSE 2022 artifact from either of the following sources:

- [GitHub releases](https://github.com/vlab-cs-ucsb/quacky/releases)
- Zenodo

The artifact is a .zip file containing the following:

- source code for Quacky (under `src`),
- sample policies used in experiments (under `samples`),
- experimental results (under `results`)
- a copy of the accepted technical paper (under `docs`).

*Note: To unzip the artifact, you can double click on the .zip file or use the `unzip` utility.*

## Installing Quacky
See `REQUIREMENTS` and `INSTALL`.

## Using Quacky
See `USAGE`.

## Running Experiments
The commands to get the raw data from each experiment are shown below. First,
```
cd src
```

### Quacky Benchmarking
#### Table 1
```
# without transformation
python3 runner_single_nolog.py -d ec2 -b 100 -c
python3 runner_single_nolog.py -d iam -b 100 -c
python3 runner_single_nolog.py -d s3 -b 100 -c

# with transformation
python3 runner_single_nolog.py -d ec2 -b 100 -c -e
python3 runner_single_nolog.py -d iam -b 100 -c -e
python3 runner_single_nolog.py -d s3 -b 100 -c -e
```

#### Table 2
```
# without resource type constraints
python3 runner_single_nolog.py -d ec2 -b 100
python3 runner_single_nolog.py -d iam -b 100
python3 runner_single_nolog.py -d s3 -b 100

# with resource type constraints
python3 runner_single_nolog.py -d ec2 -b 100 -c -e
python3 runner_single_nolog.py -d iam -b 100 -c -e
python3 runner_single_nolog.py -d s3 -b 100 -c -e
```

### Relative Permissiveness Quantification
#### Table 3
```
python3 runner_mutations_nolog.py -d ec2 -b 100 -t 600 -c -e
python3 runner_mutations_nolog.py -d iam -b 100 -t 600 -c -e
python3 runner_mutations_nolog.py -d s3 -b 100 -t 600 -c -e
```

### Comparison with Enumerative Model Counting
#### Figure 2
```
python3 runner_enumerative.py -d manual_enumerative -b 16 -t 1200
python3 runner_enumerative.py -d manual_enumerative -b 17 -t 1200
python3 runner_enumerative.py -d manual_enumerative -b 18 -t 1200
python3 runner_enumerative.py -d manual_enumerative -b 19 -t 1200
python3 runner_enumerative.py -d manual_enumerative -b 20 -t 1200
python3 runner_enumerative.py -d manual_enumerative -b 21 -t 1200
```

#### Table 4
```
# enumerative approach
python3 runner_enumerative_z3_only.py -d ec2 -b 100 -t 600 -c -e
python3 runner_enumerative_z3_only.py -d iam -b 100 -t 600 -c -e
python3 runner_enumerative_z3_only.py -d s3 -b 100 -t 600 -c -e

# quacky
python3 runner_single_nolog.py -d ec2 -b 100 -c -e
python3 runner_single_nolog.py -d iam -b 100 -c -e
python3 runner_single_nolog.py -d s3 -b 100 -c -e
```

### Microsoft Azure Policies
#### Table 5
```
python3 quacky.py -rd ../samples/azure/role_definitions/compute.json \
  -ra1 ../samples/azure/role_assignments/compute_user_login.json -b 150 -c

python3 quacky.py -rd ../samples/azure/role_definitions/compute.json \
  -ra1 ../samples/azure/role_assignments/compute_admin_login.json -b 150 -c
  
python3 quacky.py -rd ../samples/azure/role_definitions/storage.json \
  -ra1 ../samples/azure/role_assignments/storage_data_reader.json -b 150 -c

python3 quacky.py -rd ../samples/azure/role_definitions/storage.json \
  -ra1 ../samples/azure/role_assignments/storage_data_contributor.json -b 150 -c
  
python3 quacky.py -rd ../samples/azure/role_definitions/storage.json \
  -ra1 ../samples/azure/role_assignments/storage_data_owner.json -b 150 -c
```

### Tips and Tricks
Some experiments are long (they can take a couple hours). To facilitate these, we recommend the following:

#### Run experiments in the background.
```
# note: this example command is the same as the one used for Table 3.
python3 runner_mutations_nolog.py -d ec2 -b 100 -t 600 -c -e # run in foreground
python3 runner_mutations_nolog.py -d ec2 -b 100 -t 600 -c -e > out.txt &  # redirect output and run in background
python3 runner_mutations_nolog.py -d ec2 -b 100 -t 600 -c -e > out.txt &! # redirect output, run in background, and disown
```
*Note: to terminate a background process, do*
```
fg
^C
```
*Note: to terminate a disowned process, do*
```
ps -e | grep "python3" # find the runner's PID
ps -e | grep "abc"     # find ABC's PID, if applicable
sudo kill -9 [PID]
```

#### Run experiments in bulk.
```
$ cat bulkrun.sh
python3 runner_single.py -d ec2 -b 100 -c -e > ec2.txt # run for EC2
python3 runner_single.py -d iam -b 100 -c -e > iam.txt # run for IAM
python3 runner_single.py -d s3 -b 100 -c -e > s3.txt # run for S3

$ sh bulkrun.sh &!
```
*Note: don't use for each loops!*