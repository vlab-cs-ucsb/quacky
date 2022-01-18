
**Policies in ec2**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|440.241|1436.0000110069318|43.8628|0.0|0.0|536.0056465631411|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|49.5297|1568.0112931262822|7.26773|0.0|768.0056465631412|800.0056465631411|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|551.545|1504.0113151398937|58.6386|0.0|704.0056685767524|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|208.989|1544.5170370698559|705.047|0.0|1.0|643.5225400248867|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|546.122|1702.5849735076529|2164.96|0.0|2.807354922057604|800.0056465631411|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|526.667|1702.5849735076529|627.715|0.0|2.807354922057604|800.0056465631411|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|181.792|2404.0112711553306|31.0837|0.0|704.0056465631411|800.0056465631411|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|248.673|2404.011271241322|47.322|0.0|704.0056466491325|800.0056465631411|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|2228.12|2452.0168957045244|1708.39|0.0|776.0112711123351|800.0056465631411|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|SAT|52.2811|636.0056685767526|4.77369|0.0|0.0|632.0056685767526|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|206.938|809.0084615787482|41.6478|0.0|0.0|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|112.21|1703.90690160254|61.9955|0.0|4.08746284125034|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|76.8222|700.4798354148973|9.81423|0.0|4.08746284125034|696.392372573647|
