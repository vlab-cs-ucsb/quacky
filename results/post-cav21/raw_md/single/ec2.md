
**Policies in ec2**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|41589.6|1242.0774104173113|51.6143|0.0|0.0|342.0984311951053|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|571368|462.3723862746307|21050.3|0.0|8.810571634741148|461.3723862729742|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|67460.5|412.7638880477745|1934.6|0.0|6.94251450533924|412.7638880477745|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|37043.7|776.8856146991324|145.74|0.0|1.0|123.06923575264415|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|67980.1|1431.4416685774345|590.04|0.0|2.807354922057604|531.4626893552286|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|56186.2|1431.4416685774345|406.484|0.0|2.807354922057604|531.4626893552286|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|64911.6|657.0692357526442|2453.77|0.0|6.94251450533924|54.069235752644154|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|133601|1331.068449425438|3872.19|0.0|7.507794640198696|431.08946581160654|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|869199|1583.4040475505933|29662.2|0.0|8.997179480937621|679.8247206060817|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|UNSAT|31727.6|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|37496.2|154.06923575264415|45.1167|0.0|0.0|122.06923575264415|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|43717.8|1312.7428672699807|296.334|0.0|4.08746284125034|412.7638880477748|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|39889|412.7638880477748|41.2632|0.0|1.5849625007211563|412.7638880477748|
