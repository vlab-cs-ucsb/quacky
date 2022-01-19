# Sample Policies

## Contents
- `azure`: Azure role definitions and role assignments from Azure portal
- `ec2`: AWS IAM policies for the EC2 service
- `iam`: AWS IAM policies for the IAM service
- `s3`: AWS IAM policies for the S3 service
- `manual_enumerative`: toy policies for testing the enumerative model counting approach
- `mutations`: AWS IAM policies synthesized by mutating policies in `ec2`, `iam`, `s3`

Some directories contain a subdirectory called `exp_single` and/or a subdirectory called `exp_multiple`.

- policies in `exp_single` are meant for permissiveness analysis (by themselves)
- policies in `exp_multiple` are meant for relative permissiveness analysis (between two policies)
