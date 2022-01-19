
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
python3 runner_mutations.py [args]              # run in foreground
python3 runner_mutations.py [args] > out.txt &  # redirect output and run in background
python3 runner_mutations.py [args] > out.txt &! # redirect outupt, disown, and run in background
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
python3 runner_single.py -d ec2 [args] > ec2.txt
python3 runner_single.py -d iam [args] > iam.txt
python3 runner_single.py -d s3 [args] > s3.txt

$ sh bulkrun.sh &!
```
*Note: don't use for each loops!*

## Other Use Cases
### Translating Policies
You may wish to pass a formula into another constraint solver or model counter (e.g. to get a model).

#### Command-Line Arguments
```
$ cd src
$ python3 translator.py -h
usage: translator.py [-h] [-p1 POLICY1] [-p2 POLICY2] [-rd ROLE_DEFINITIONS]
                     [-ra1 ROLE_ASSIGNMENT1] [-ra2 ROLE_ASSIGNMENT2]
                     [-r ROLES] [-rb1 ROLE_BINDING1] [-rb2 ROLE_BINDING2]
                     [-d DOMAIN] [-o OUTPUT] [-s] [-e] [-c]

Translate access control policies to SMT formulas

optional arguments:
  -h, --help            show this help message and exit
  -p1 POLICY1, --policy1 POLICY1
                        policy 1 (AWS)
  -p2 POLICY2, --policy2 POLICY2
                        policy 2 (AWS)
  -rd ROLE_DEFINITIONS, --role-definitions ROLE_DEFINITIONS
                        role definitions (Azure)
  -ra1 ROLE_ASSIGNMENT1, --role-assignment1 ROLE_ASSIGNMENT1
                        role assignment 1 (Azure)
  -ra2 ROLE_ASSIGNMENT2, --role-assignment2 ROLE_ASSIGNMENT2
                        role assignment 2 (Azure)
  -r ROLES, --roles ROLES
                        roles (GCP)
  -rb1 ROLE_BINDING1, --role-binding1 ROLE_BINDING1
                        role binding 1 (GCP)
  -rb2 ROLE_BINDING2, --role-binding2 ROLE_BINDING2
                        role binding 2 (GCP)
  -d DOMAIN, --domain DOMAIN
                        domain file (not supported)
  -o OUTPUT, --output OUTPUT
                        output file
  -s, --smt-lib         use SMT-LIB syntax
  -e, --enc             use action encoding
  -c, --constraints     use resource type constraints
```

#### Example: Translate Multiple AWS IAM Policies, With Resource Type Constraints
```
cd src
python3 translator.py -p1 [file1].json -p2 [file2].json -c -s
```

*Note: we use the `-s` flag to use SMT-LIB syntax. By default, ABC supports PCRE syntax for regex.*

*Note: Quacky produces 2 formulas: `output_1.smt2` and `output_2.smt2`. To change the name, use `-o`.*

#### Example: Translate a Single Azure Role Definition and Role Assignment
```
cd src
python3 translator.py -rd [file].json -ra1 [file].json -s
```

*Note: although we pass in two files, they form a single "policy" in our policy model.*

### Mutating Policies
If you wish to mutate policies (in case you implement new/modified mutation types),
```
cd samples
python3 mutate.py -d [dir] # e.g. iam/exp_single
```

### Building Resource Type Constraints Offline
If you wish to rebuild resource type constraints or action encoding offline, do the following:

*Note: we recommend doing steps 1-2 once in a while.*

#### AWS
1. **(optional)** Download [Selenium WebDriver](https://selenium-python.readthedocs.io/installation.html#drivers) for your browser to `src/offline/aws`

2. **(optional)** Scrape AWS documentation

```
cd src/offline/aws
```

2a. Uncomment the line(s) corresponding to your WebDriver. For example, for Firefox,
```
$ vim awsscraper.py
16	# browser = webdriver.Chrome(options = options)
17	# browser = webdriver.Opera(options = options, executable_path = './operadriver')
18	browser = webdriver.Firefox(options = options, executable_path = './geckodriver')
...
84	# browser = webdriver.Chrome(options = options)
85	# browser = webdriver.Opera(options = options, executable_path = './operadriver')
86	browser = webdriver.Firefox(options = options, executable_path = './geckodriver')
```

*Note: you may have to rename the WebDriver executable for Opera and Firefox.*

2b. Run
```
python3 awsscraper.py
```

3. Update `resource_regex.json` and `resource_regex_z3.json`

4. Build action encoding
```
python3 encoder.py
```

5. Build resource type constraints
```
python3 constraintgen.py
python3 constraintgen_z3.py # with SMT-LIB syntax
python3 constraintgen_enc.py # with action encoding
python3 constraintgen_enc_z3.py
```

#### Azure
1. **(optional)** Download permissions CSV from [Azure portal](https://portal.azure.com) to `src/offline/azure/permissions.csv`

2. Scrape `permissions.csv`
```
cd src/offline/azure
python3 azurescraper.py
```

3. Build action encoding
```
python3 encoder.py
```

#### GCP
1. **(optional)** Download permissions from [GCP docs](https://cloud.google.com/iam/docs/permissions-reference) to `src/offline/gcp/permissions.html`

2. **(optional)** Download resource types from [GCP console](https://console.cloud.google.com) to `src/offline/gcp/resource_types.xml`

3. Scrape `permissions.html` and `resource_types.xml`
```
cd src/offline/gcp
python3 gcpscraper.py
```

4. Build action encoding
```
python3 encoder.py
```
