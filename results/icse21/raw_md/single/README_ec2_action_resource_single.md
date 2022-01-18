
**Policies in ec2**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|33808.7|1242.0774104173113|54.9728|0.0|0.0|342.0984311951053|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|312824|412.302556896222|10846.1|0.0|8.640244936222347|412.302556896222|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|50658.8|412.3025568962218|1121.86|0.0|6.807354922057604|412.3025568962218|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|30583.1|783.0737916340521|139.925|0.0|1.0|138.203073275|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|53046.1|1313.2815361184275|519.618|0.0|2.807354922057604|413.3025568962218|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|44338.7|1313.2815361184275|344.822|0.0|2.807354922057604|413.3025568962218|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|48019.2|652.3143482504807|1078.2|0.0|6.768184324776926|49.314348250480684|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|83919.6|1312.281536118428|2923.39|0.0|7.339850002884624|412.302556896222|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|465147|1583.4040475505933|18553.6|0.0|8.800899899920305|679.8247206060817|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|UNSAT|26848.2|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|33753.1|146.20588829060705|68.2379|0.0|0.0|137.20307327499998|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|36105.2|1312.281536118428|246.051|0.0|4.08746284125034|412.302556896222|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|33412.9|412.302556896222|42.4672|0.0|1.5849625007211563|412.302556896222|
