
**Policies in ec2**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|464.592|1436.0000110069318|43.4462|0.0|0.0|536.0056465631411|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|65.7464|1568.0112931262822|8.45269|0.0|768.0056465631412|800.0056465631411|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|600.416|1504.0113151398937|59.6976|0.0|704.0056685767524|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|258.095|1544.5170370698559|722.986|0.0|1.0|643.5225400248867|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|588.613|1702.5849735076529|2148.66|0.0|2.807354922057604|800.0056465631411|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|559.382|1702.5849735076529|637.183|0.0|2.807354922057604|800.0056465631411|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|211.727|2404.0112711553306|33.4653|0.0|704.0056465631411|800.0056465631411|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|208.016|2404.011271241322|47.9817|0.0|704.0056466491325|800.0056465631411|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|2295.45|2452.0168957045244|1663.41|0.0|776.0112711123351|800.0056465631411|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|SAT|80.8117|636.0056685767526|6.51364|0.0|0.0|632.0056685767526|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|307.244|809.0084615787482|42.3747|0.0|0.0|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|143.928|1703.90690160254|65.425|0.0|4.08746284125034|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|118.699|700.4798354148973|12.2939|0.0|4.08746284125034|696.392372573647|

**Policies in ec2**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|33218.8|1242.0774104173113|54.7874|0.0|0.0|342.0984311951053|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|301889|412.302556896222|10495.9|0.0|8.640244936222347|412.302556896222|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|50421.8|412.3025568962218|1101.94|0.0|6.807354922057604|412.3025568962218|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|29655.4|783.0737916340521|138.093|0.0|1.0|138.203073275|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|51124|1313.2815361184275|510.28|0.0|2.807354922057604|413.3025568962218|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|42978.9|1313.2815361184275|337.252|0.0|2.807354922057604|413.3025568962218|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|46305.6|652.3143482504807|1058.8|0.0|6.768184324776926|49.314348250480684|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|81605.5|1312.281536118428|2853.07|0.0|7.339850002884624|412.302556896222|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|468954|1583.4040475505933|18204.3|0.0|8.800899899920305|679.8247206060817|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|UNSAT|26081.2|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|31547.4|146.20588829060705|64.4489|0.0|0.0|137.20307327499998|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|34180.6|1312.281536118428|243.66|0.0|4.08746284125034|412.302556896222|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|31574.5|412.302556896222|41.7346|0.0|1.5849625007211563|412.302556896222|
