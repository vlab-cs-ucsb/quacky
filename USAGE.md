# (Re)using Quacky 
*Note: instructions for running experiments are in the `README`.*

## Analyzing Policies
Quacky's main purpose is to quantitatively assess the (relative) permissiveness of access control policies for the cloud. The entry point into this analysis is `quacky.py`.

#### Command-Line Arguments
```
$ cd src
$ python3 quacky.py -h
usage: quacky.py [-h] [-p1 POLICY1] [-p2 POLICY2] [-rd ROLE_DEFINITIONS]
                 [-ra1 ROLE_ASSIGNMENT1] [-ra2 ROLE_ASSIGNMENT2] [-r ROLES]
                 [-rb1 ROLE_BINDING1] [-rb2 ROLE_BINDING2] [-o OUTPUT] [-s]
                 [-e] [-c] -b BOUND [-f] [-v]

Quantitatively analyze permissiveness of access control policies

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
  -o OUTPUT, --output OUTPUT
                        output file
  -s, --smt-lib         use SMT-LIB syntax
  -e, --enc             use action encoding
  -c, --constraints     use resource type constraints
  -b BOUND, --bound BOUND
                        bound
  -f, --variable        count all variables
  -v, --verbose         Verbose

```

In the examples that follow, we reuse Quacky outside of our experiments.

#### Example: Basic Usage Example
*Note: this example is also covered in `INSTALL`.*

In this example, we analyze a simple AWS IAM policy. More specifically, we analyze the policy `iam_simplest_policy/policy.json` from our policy dataset and count the number of requests allowed up to a bound (string length/integer bitwidth) of 100. In other words, our arguments are
- policy1: ../samples/iam/exp_single/iam_simplest_policy/policy.json
- bound: `100`

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

#### Example: Analyze Multiple AWS IAM Policies
In this example, we analyze the relative permissiveness of Policies 2(a) and 2(b) in the technical paper.

First, we copy and paste Policy 2(a) into JSON files as shown below.

```
$ cd src
$ cat policy2a.json
{"Statement": [{
    "Effect": "Allow",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::myexamplebucket/*"},
  {
    "Effect": "Deny",
    "Principal": "*",
    "Action": "s3:GetObject",
    "Resource": "arn:aws:s3:::myexamplebucket/*"}]}
$ cat policy2b.json
{"Statement": [{
  "Effect": "Allow",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::myexamplebucket/*"},
{
  "Effect": "Deny",
  "Principal": "*",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::myexamplebucket/*",
  "Condition": {
    "StringNotLike": {
      "aws:userId": [
        "AROAEXAMPLEID:*", "AIDAEXAMPLEID", "111111111111"]}}}]}
```

First, we analyze Policy 2(a). Our arguments are
- policy1: policy2a.json
- bound: `100`

```
$ python3 quacky.py -p1 policy2a.json -b 100
Policy 1
╒═════════════════╤═════════╕
│ Solve Time (ms) │ 87.8023 │
├─────────────────┼─────────┤
│ Satisfiability  │ UNSAT   │
├─────────────────┼─────────┤
│ requests        │ 0       │
╘═════════════════╧═════════╛
```

Next, we analyze Policy 2(b). Our arguments are
- policy1: policy2b.json
- bound: `100`
- variable: `true`

```
$ python3 quacky.py -p1 policy2b.json -b 100 -f
Policy 1
╒═════════════════╤════════════════════╕
│ Solve Time (ms) │ 1239.3             │
├─────────────────┼────────────────────┤
│ Satisfiability  │ SAT                │
├─────────────────┼────────────────────┤
│ Count Time (ms) │ 154.561            │
├─────────────────┼────────────────────┤
│ lg(requests)    │ 2048.0169396894235 │
├─────────────────┼────────────────────┤
│ lg(principal)   │ 800.0056465631411  │
├─────────────────┼────────────────────┤
│ lg(action)      │ 0.0                │
├─────────────────┼────────────────────┤
│ lg(resource)    │ 560.0056465631411  │
╘═════════════════╧════════════════════╛
```

#### Example: Analyze Multiple AWS IAM Policies, With Resource Type Constraints
In this example, our arguments are
- policy1: ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json
- policy2: ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json
- bound: `100`
- constraints: `true`

```
cd src
python3 quacky.py -p1 ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json -p2 ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json -b 100 -c
```

#### Example: Analyze a Single Azure Role Definition and Role Assignment
In this example, our arguments are
- roledefinition: ../samples/azure/role_definitions/compute.json
- roleassignment1: ../samples/azure/role_assignments/compute_user_login.json
- bound: `150`

```
cd src
python3 translator.py -rd ../samples/azure/role_definitions/compute.json -ra1 ../samples/azure/role_assignments/compute_user_login.json -b 150
```

## Other Use Cases
### Translating Policies
By default, Quacky uses the model counting constraint solver [ABC](https://github.com/vlab-cs-ucsb/ABC). While ABC is useful for counting the number of allowed requests for policies in a single call, you may instead wish to get an instance (i.e. a satisfying assignment or model) of an allowed request. That is, you may wish to  translate the policy into a SMT formula and pass that into another constraint solver, bypassing ABC. The entry point into this translation is `translator.py`.

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
In this example, our arguments are
- policy1: ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json
- policy2: ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json
- constraints: `true`
- smt-lib: `true`

```
cd src
python3 translator.py -p1 ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json -p2 ../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json -c -s
```

*Note: we use the `-s` flag to use SMT-LIB syntax. By default, ABC supports PCRE syntax for regex.*

*Note: Quacky produces 2 formulas: `output_1.smt2` and `output_2.smt2`. To change the name, use `-o`.*

We can read the SMT formula as shown below.

```
$ cat output_1.smt2 | head -n10
(set-logic ALL)
(set-option :produce-models true)

(declare-const principal String)
(declare-const action String)
(declare-const resource String)
(declare-const aws.username String)
(declare-const aws.username.exists Bool)

(assert (= aws.username.exists (not (= aws.username ""))))
```

If you had Z3 installed (not required), you could get a model as shown below.

```
$ z3 output_1.smt2
sat
(
  (define-fun resource () String
    "arn:aws:iam::000000000000:*")
  (define-fun action () String
    "iam:createuser")
  (define-fun aws.username () String
    "G")
  (define-fun p0.s0.cStringNotLikeaws.username () Bool
    true)
  (define-fun p0.s0.a () Bool
    true)
  (define-fun p1.neutral () Bool
    true)
  (define-fun p0.allows () Bool
    true)
  (define-fun p1.allows () Bool
    false)
  (define-fun p1.denies () Bool
    false)
  (define-fun p1.s0.allows () Bool
    false)
  (define-fun p1.s0.denies () Bool
    false)
  (define-fun p1.s0.r () Bool
    false)
  (define-fun p1.s0.a () Bool
    true)
  (define-fun p1.s0.pr () Bool
    true)
  (define-fun p0.neutral () Bool
    false)
  (define-fun p0.denies () Bool
    false)
  (define-fun p0.s0.allows () Bool
    true)
  (define-fun p0.s0.denies () Bool
    false)
  (define-fun p0.s0.pr () Bool
    true)
  (define-fun aws.username.exists () Bool
    true)
  (define-fun p0.s0.r () Bool
    true)
  (define-fun principal () String
    "")
)
```

#### Example: Translating a Single AWS IAM Policy to Count a Variable with ABC
In this example, we translate Policy 2(b) into an SMT formula and count the number of allowed `aws:userId`s, this time allowing strings with all ASCII characters up to length 64. 

*Note: because we are using ABC, we do not need to use `-s`.*

```
$ python3 translator.py -p1 policy2b.json
$ abc -i output_1.smt2 -bs 64 -v 0 --count-variable aws.userId
attribute
I20220221 17:01:33.239962  3843 main.cpp:211] Done solving
sat
I20220221 17:01:33.240065  3843 main.cpp:299] report is_sat: SAT time: 1257.07 ms
I20220221 17:01:33.240087  3843 main.cpp:326] report var: aws.userId
I20220221 17:01:33.525513  3843 main.cpp:340] report bound: 64 count: 2592376348197053329223197286403023685601586992016789095233916844213356044063966062059565531136138371951338086372640620804 time: 285.417 ms
I20220221 17:01:33.525573  3843 main.cpp:380] done.

```

#### Example: Translate a Single Azure Role Definition and Role Assignment
In this example, our arguments are
- roledefinition: ../samples/azure/role_definitions/compute.json
- roleassignment1: ../samples/azure/role_assignments/compute_user_login.json

```
cd src
python3 translator.py -rd ../samples/azure/role_definitions/compute.json -ra1 ../samples/azure/role_assignments/compute_user_login.json
```

*Note: although we pass in two files, they form a single "policy" in our policy model.*

```
$ cat output_1.smt2 | head -n15
(set-logic ALL)
(set-option :produce-models true)

(declare-const action String)
(declare-const resource String)
(declare-const principal String)

; Principal: p0.s0.pr
(declare-const p0.s0.pr Bool)
(assert (= p0.s0.pr (or (= principal "foo"))))

; Action: p0.s0.a
(declare-const p0.s0.a Bool)
(assert (= p0.s0.a (or (= action "microsoft.network/publicipaddresses/read") (= action "microsoft.network/virtualnetworks/read") (= action "microsoft.network/loadbalancers/read") (= action "microsoft.network/networkinterfaces/read") (in action /microsoft\.compute\/virtualmachines\/.*\/read/) (= action "microsoft.compute/virtualmachines/login/action"))))
```

### Mutating Policies
In our technical paper, we implemented three types of mutations. In case you implement new/modified mutation types, you may wish to mutate the real-world AWS IAM policies again. The entry point into this mutation is in `mutate.py` within the `samples` directory, not `src`.

```
cd samples
python3 mutate.py -d [dir] # e.g. iam/exp_single
```

### Building Resource Type Constraints Offline
In our technical paper, we describe the purpose and implementation of resource type constraints and the numeric action encoding. There is a separate entry point into the resource type constraint generation for each currently supported cloud service provider (AWS, Azure, GCP). If you wish to rebuild the resource type constraints or action encoding offline, do the following:

*Note: we recommend doing steps 1-2 once in a while.*

#### AWS
1. **(optional)** Download [Selenium WebDriver](https://selenium-python.readthedocs.io/installation.html#drivers) for your browser to `src/offline/aws`

2. **(optional)** Scrape AWS documentation

```
cd src/offline/aws
```

First, uncomment the line(s) corresponding to your WebDriver. For example, for Firefox,
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

Second, run
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

# Extending Quacky
Quacky is written in Python because of its ease of development and package library (for a list of packages used, please see `REQUIREMENTS`). The high-level architecture comprises four components, namely the 
1. frontend
2. backend
3. model counter
4. resource type constraint generator,
each of which can be extended separately.

## Frontend
The frontend takes access control policies as input, and it outputs instances of the policy model as described by the technical paper. The entry point into the frontend is `frontend.py`.

## Backend
The backend takes instances of the policy model as input, and it outputs SMT formulas that encode the semantics of each policy. The classes for nodes of the policy model, and the functions to visit them, are implemented in `policy_model.py`. The entry point into the backend is `backend.py`. The backend calls `expressions.py` to generate S-expressions in SMT-LIB2. In addition, it calls `conditions` and `constraints` files for each cloud service provider as they have provider-specific implementations.

## Resource Type Constraint Generator
For a more precise quantitative analysis, the backend may add resource type constraints, which capture a cloud service provider's valid resource types, actions, and pairings thereof, to the formula. The `offline` directory implements resource type constraints and action encoding for each cloud service provider.

## Auxiliary Components
- `utilities.py` contains helper functions that do not entirely fit into the frontend or backend.
- the `utils` directory contains classes and functions to interact with ABC.
- the `re2smt` directory contains classes and functinos to translate regular expressions in PCRE syntax to SMT-LIB2 syntax.