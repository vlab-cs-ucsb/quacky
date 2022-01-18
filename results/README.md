# ERSP Results 

## Single Policy Results

**Policies in ec2**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|469.152|1436.0000110069318|43.6419|0.0|0.0|536.0056465631411|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|50.0598|1568.0112931262822|7.32879|0.0|768.0056465631412|800.0056465631411|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|520.295|1504.0113151398937|58.8216|0.0|704.0056685767524|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|160.54|1544.5170370698559|672.784|0.0|1.0|643.5225400248867|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|484.78|1702.5849735076529|2093.1|0.0|2.807354922057604|800.0056465631411|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|447.218|1702.5849735076529|603.489|0.0|2.807354922057604|800.0056465631411|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|118.969|2404.0112711553306|27.204|0.0|704.0056465631411|800.0056465631411|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|194.991|2404.011271241322|44.0981|0.0|704.0056466491325|800.0056465631411|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|2238.46|2452.0168957045244|1638.99|0.0|776.0112711123351|800.0056465631411|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|SAT|113.559|636.0056685767526|8.24029|0.0|0.0|632.0056685767526|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|313.01|809.0084615787482|42.0308|0.0|0.0|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|151.026|1703.90690160254|63.2997|0.0|4.08746284125034|800.0056465631411|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|127.49|700.4798354148973|12.8285|0.0|4.08746284125034|696.392372573647|

**Policies in ec2**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json](../samples/ec2/exp_single/ec2_prevent_running_classic/policy.json)|SAT|33322.3|1242.0774104173113|53.8453|0.0|0.0|342.0984311951053|
|[../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json](../samples/ec2/exp_single/ec2_require_mfa_session_token/policy.json)|SAT|303635|412.302556896222|10411.6|0.0|8.640244936222347|412.302556896222|
|[../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json](../samples/ec2/exp_single/ec2_launch_instance_specific_subnet/policy.json)|SAT|49379.9|412.3025568962218|1095.46|0.0|6.807354922057604|412.3025568962218|
|[../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json](../samples/ec2/exp_single/ec2_allow_ebs_volume_owners/policy.json)|SAT|29941.4|783.0737916340521|136.181|0.0|1.0|138.203073275|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/fixed.json)|SAT|51184.2|1313.2815361184275|525.158|0.0|2.807354922057604|413.3025568962218|
|[../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_single/ec2_limit_ebs_volume_size/initial.json)|SAT|42854.2|1313.2815361184275|335.783|0.0|2.807354922057604|413.3025568962218|
|[../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json](../samples/ec2/exp_single/ec2_restrict_to_specific_instance/policy.json)|SAT|46913.1|652.3143482504807|1047.6|0.0|6.768184324776926|49.314348250480684|
|[../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json](../samples/ec2/exp_single/ec2_enforce_project_tagging/policy.json)|SAT|82057|1312.281536118428|2837.52|0.0|7.339850002884624|412.302556896222|
|[../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json](../samples/ec2/exp_single/ec2_actions_region_aws-portal/policy.json)|SAT|469980|1583.4040475505933|18369|0.0|8.800899899920305|679.8247206060817|
|[../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json](../samples/ec2/exp_single/ec2_validate_attach_volume/policy.json)|UNSAT|26407.6|-|-|-|-|-|
|[../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json](../samples/ec2/exp_single/ec2_terminate_instance_ip/policy.json)|SAT|33052.2|146.20588829060705|67.5312|0.0|0.0|137.20307327499998|
|[../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_single/ec2_allow_some_instances/fixed.json)|SAT|34537.6|1312.281536118428|240.553|0.0|4.08746284125034|412.302556896222|
|[../samples/ec2/exp_single/ec2_allow_some_instances/initial.json](../samples/ec2/exp_single/ec2_allow_some_instances/initial.json)|SAT|31642.7|412.302556896222|41.6037|0.0|1.5849625007211563|412.302556896222|

**Policies in iam**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|158.264|1288.0112931262822|54.642|0.0|704.0056465631411|800.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|66.4235|696.0056465631412|13.9958|0.0|3.0|696.0056465631412|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|22.667|802.3275746580285|16.0199|0.0|2.321928094887362|800.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|51.2675|2096.0169396894235|5.8178|800.0056465631411|776.0056465631412|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|7.57766|0.0|5.11043|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|71.3957|575.1754929842821|5.91204|0.0|1.0|574.1754929842821|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|27.8804|1601.0112931262822|4.47402|0.0|1.0|800.0056465631411|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|14.7946|1600.0112931262822|3.14417|0.0|800.0056465631411|800.0056465631411|

**Policies in iam**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|1458.14|587.8130014851988|120.432|0.0|4.392317422778761|584.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|964.034|586.3275746580285|11.1434|0.0|3.0|584.0056465631411|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|1475|482.8226191555779|10.8984|0.0|2.321928094887362|480.5006910606906|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|940.195|1324.918183721891|33.0196|800.0056465631411|4.906890595608519|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|643.284|0.0|4.20958|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|911.294|416.40090563401435|14.5651|0.0|1.0|415.40090563401435|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|1101.89|1281.5063376238318|10.9058|0.0|1.0|480.5006910606906|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|6129.55|684.7316112016902|1007.77|0.0|7.857980995127572|679.8247206060817|

**Policies in s3**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json](../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json)|SAT|191.711|3032.0112711124193|108.976|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json)|SAT|320.847|1400.0112931262822|114.95|0.0|776.0056465631412|800.0056465631411|
|[../samples/s3/exp_single/s3_allow_all_except_delete/initial.json](../samples/s3/exp_single/s3_allow_all_except_delete/initial.json)|SAT|104.891|1400.0112931262822|18.3366|0.0|776.0056465631412|624.0056465631411|
|[../samples/s3/exp_single/s3_public_access/policy.json](../samples/s3/exp_single/s3_public_access/policy.json)|SAT|93.3809|1944.0169396894232|9.29216|800.0056465631411|0.0|544.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/policy1.json](../samples/s3/exp_single/s3_object_query_permissions/policy1.json)|SAT|263.76|3056.0112711124193|194.389|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/fix.json](../samples/s3/exp_single/s3_object_query_permissions/fix.json)|SAT|11.5795|2.0|5.14614|0.0|1.0|0.0|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json)|SAT|49.2317|657.5906090638623|9.71628|0.0|2.0|656.0056465631411|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json)|SAT|221.919|1344.0112931262822|36.5388|0.0|776.0056465631412|568.0056465631411|
|[../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json](../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json)|SAT|47.4305|1408.0112931262822|5.18907|0.0|776.0056465631412|632.0056465631412|
|[../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json](../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json)|SAT|1831.87|3080.0112711124193|220.052|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json)|SAT|1428.63|2056.0169396894235|155.515|800.0056465631411|0.0|568.0056465631411|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json)|UNSAT|169.215|-|-|-|-|-|
|[../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json](../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json)|SAT|299.628|2376.0169396894235|5404.85|800.0056465631411|776.0056465631412|800.0056465631411|
|[../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json](../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json)|SAT|66.4583|1384.0112931262825|8.97079|800.0056465631411|0.0|584.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json)|SAT|1803.14|3120.0112711124193|92.4641|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json)|SAT|163.576|3104.0112711124193|73.7798|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json)|SAT|66.6507|776.0056465631412|46.0743|0.0|776.0056465631412|1.0|
|[../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json](../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json)|SAT|83.5961|1416.0112931262822|46.8636|800.0056465631411|776.0056465631412|616.0056465631411|
|[../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json](../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json)|SAT|66049.7|2872.0225862529|119130|800.0056465631411|800.0056465631411|632.0056465631412|
|[../samples/s3/exp_single/s3_policy_or_condition/policy.json](../samples/s3/exp_single/s3_policy_or_condition/policy.json)|SAT|681.169|2192.0169396894235|126.325|800.0056465631411|0.0|664.0056465631412|

**Policies in s3**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json](../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json)|SAT|1723.02|2260.960065941997|90.3484|0.0|5.044394119358453|457.11157034269354|
|[../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json)|SAT|2225.77|628.9125371587496|84.3113|0.0|6.266786540694902|624.0056465631411|
|[../samples/s3/exp_single/s3_allow_all_except_delete/initial.json](../samples/s3/exp_single/s3_allow_all_except_delete/initial.json)|SAT|850.636|628.9125371587496|50.0403|0.0|4.906890595608519|624.0056465631411|
|[../samples/s3/exp_single/s3_public_access/policy.json](../samples/s3/exp_single/s3_public_access/policy.json)|SAT|660.547|1944.0169396894232|8.31278|800.0056465631411|0.0|544.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/policy1.json](../samples/s3/exp_single/s3_object_query_permissions/policy1.json)|SAT|1854.7|2284.906890620335|124.165|0.0|5.044394119358453|480.0056466622347|
|[../samples/s3/exp_single/s3_object_query_permissions/fix.json](../samples/s3/exp_single/s3_object_query_permissions/fix.json)|SAT|719.799|2.0|4.91582|0.0|1.0|0.0|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json)|SAT|713.797|657.5906090638623|6.03135|0.0|2.0|656.0056465631411|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json)|SAT|1221.2|572.9125371587496|45.1688|0.0|4.906890595608519|568.0056465631411|
|[../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json](../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json)|SAT|1068.41|636.9125371587497|70.4942|0.0|6.22881869049588|632.0056465631412|
|[../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json](../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json)|SAT|3941.64|2308.9068906171065|155.061|0.0|5.044394119358453|504.00564656314117|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json)|SAT|2576.38|2056.0169396894235|166.001|800.0056465631411|0.0|568.0056465631411|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json)|UNSAT|187.692|-|-|-|-|-|
|[../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json](../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json)|SAT|12344.1|1484.7372577648314|6845.91|800.0056465631411|6.507794640198696|679.8247206060817|
|[../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json](../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json)|SAT|735.125|1384.0112931262825|4.94107|800.0056465631411|0.0|584.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json)|SAT|3059.71|2348.9068906171065|91.1049|0.0|5.044394119358453|544.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json)|SAT|1483.68|2332.9068906171065|85.0203|0.0|5.0|528.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json)|SAT|1084.25|5.0|33.8904|0.0|5.0|1.0|
|[../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json](../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json)|SAT|1538.45|1416.0112931262822|55.7757|800.0056465631411|5.523561956057013|616.0056465631411|
|[../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json](../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json)|SAT|93683.1|2076.923830285368|13429.8|800.0056465631411|4.906890595608519|632.0056465631412|
|[../samples/s3/exp_single/s3_policy_or_condition/policy.json](../samples/s3/exp_single/s3_policy_or_condition/policy.json)|SAT|1039.74|2192.0169396894235|132.387|800.0056465631411|0.0|664.0056465631412|

## Multiple Policy Results

**Policies in ec2**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/fixed.json)|[../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/initial.json)|UNSAT|2823.08|-|-|-|-|-|SAT|2316.01|1443.5281656028455|766.489|0.0|0.0|643.5225190397044|
|[../samples/ec2/exp_multiple/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_multiple/ec2_allow_some_instances/fixed.json)|[../samples/ec2/exp_multiple/ec2_allow_some_instances/initial.json](../samples/ec2/exp_multiple/ec2_allow_some_instances/initial.json)|SAT|641.993|1703.90690160254|5737.97|0.0|4.08746284125034|800.0056465631411|UNSAT|649.978|-|-|-|-|-|

**Policies in ec2**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/fixed.json](../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/fixed.json)|[../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/initial.json](../samples/ec2/exp_multiple/ec2_limit_ebs_volume_size/initial.json)|UNSAT|56906.3|-|-|-|-|-|SAT|45348.2|937.2087198381412|112.275|0.0|0.0|137.20307327499998|
|[../samples/ec2/exp_multiple/ec2_allow_some_instances/fixed.json](../samples/ec2/exp_multiple/ec2_allow_some_instances/fixed.json)|[../samples/ec2/exp_multiple/ec2_allow_some_instances/initial.json](../samples/ec2/exp_multiple/ec2_allow_some_instances/initial.json)|SAT|34815|1212.308203459363|408.864|0.0|3.9068905956085187|412.302556896222|UNSAT|36399.2|-|-|-|-|-|

**Policies in iam**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/fixed.json)|[../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|508.675|1288.0112931262822|61.4912|0.0|704.0056465631411|800.0056465631411|UNSAT|196.029|-|-|-|-|-|
|[../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy2.json)|[../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|109.53|2096.0169396894235|114.972|800.0056465631411|776.0056465631412|520.0056465631411|SAT|194.152|288.0|5.10556|0.0|0.0|0.0|
|[../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json)|[../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json)|SAT|211.141|1295.181139547423|948.037|0.0|1.0|574.1754929842821|SAT|200.144|1601.0112931262822|33.2935|0.0|1.0|800.0056465631411|

**Policies in iam**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/fixed.json)|[../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_multiple/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|1885.39|587.1755715645834|122.27|0.0|3.8073549220576037|584.0056465631411|UNSAT|1157.75|-|-|-|-|-|
|[../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy2.json)|[../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_multiple/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|1714.8|1324.918183721891|151.685|800.0056465631411|4.906890595608519|520.0056465631411|SAT|885.739|288.0|4.68836|0.0|0.0|0.0|
|[../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/fixed.json)|[../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_multiple/iam_policy_allow_adding_deleting_users/initial.json)|SAT|4135.24|1136.4065521971556|6107.82|0.0|1.0|415.40090563401435|SAT|1250.91|1281.5063376238318|26.8641|0.0|1.0|480.5006910606906|

**Policies in s3**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_multiple/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_multiple/s3_allow_all_except_delete/fixed.json)|[../samples/s3/exp_multiple/s3_allow_all_except_delete/initial.json](../samples/s3/exp_multiple/s3_allow_all_except_delete/initial.json)|SAT|823.414|802.5906090781941|115.314|0.0|776.0056465631412|800.0056465631411|UNSAT|224.257|-|-|-|-|-|
|[../samples/s3/exp_multiple/s3_object_query_permissions/policy1.json](../samples/s3/exp_multiple/s3_object_query_permissions/policy1.json)|[../samples/s3/exp_multiple/s3_object_query_permissions/fix.json](../samples/s3/exp_multiple/s3_object_query_permissions/fix.json)|SAT|560.61|3056.0112711124193|208.514|0.0|776.0056465631412|696.0056465631412|SAT|402.524|308.0|7.13992|0.0|1.0|0.0|
|[../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy2.json)|[../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy1.json)|SAT|238.799|657.5906090638623|6.50113|0.0|2.0|656.0056465631411|SAT|337.278|1344.0112931262822|33.7289|0.0|776.0056465631412|568.0056465631411|
|[../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy2.json)|[../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy1.json)|SAT|2696.7|2056.0169396894235|165.537|800.0056465631411|0.0|568.0056465631411|UNSAT|222.015|-|-|-|-|-|
|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json)|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy2.json)|SAT|2212.23|3120.0112711124193|97.1826|0.0|776.0056465631412|696.0056465631412|SAT|1333.61|3104.0112711124193|77.8397|0.0|776.0056465631412|528.0056465631411|
|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json)|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy2.json)|SAT|2202.27|3120.0112711124193|96.3591|0.0|776.0056465631412|696.0056465631412|SAT|1341.09|3104.0112711124193|78|0.0|776.0056465631412|528.0056465631411|

**Policies in s3**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_multiple/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_multiple/s3_allow_all_except_delete/fixed.json)|[../samples/s3/exp_multiple/s3_allow_all_except_delete/initial.json](../samples/s3/exp_multiple/s3_allow_all_except_delete/initial.json)|SAT|2771.46|5.554588851677638|31.0341|0.0|5.554588851677638|1.0|UNSAT|1291.85|-|-|-|-|-|
|[../samples/s3/exp_multiple/s3_object_query_permissions/policy1.json](../samples/s3/exp_multiple/s3_object_query_permissions/policy1.json)|[../samples/s3/exp_multiple/s3_object_query_permissions/fix.json](../samples/s3/exp_multiple/s3_object_query_permissions/fix.json)|SAT|2315.63|2284.906890620335|125.802|0.0|5.044394119358453|480.0056466622347|SAT|1166.84|308.0|6.79936|0.0|1.0|0.0|
|[../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy2.json)|[../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_multiple/s3_policy_for_lambda_function/policy1.json)|SAT|1011.55|657.5906090638623|6.45665|0.0|2.0|656.0056465631411|SAT|1432.96|572.9125371587496|43.3726|0.0|4.906890595608519|568.0056465631411|
|[../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy2.json)|[../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_multiple/s3_remove_permissions_individual_files/policy1.json)|SAT|3926.78|2056.0169396894235|164.994|800.0056465631411|0.0|568.0056465631411|UNSAT|268.263|-|-|-|-|-|
|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json)|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy2.json)|SAT|3915.05|2348.9068906171065|63.499|0.0|5.0|544.0056465631412|SAT|4175.99|2332.9068906171065|64.2562|0.0|4.954196310386876|528.0056465631411|
|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy3.json)|[../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_multiple/s3_policy_provides_programmatic_access/policy1.json)|SAT|3308.52|2348.9068906171065|93.7492|0.0|5.044394119358453|544.0056465631412|SAT|3066.03|630.000000000021|43.8865|0.0|4.954196310386876|1.0|

**Policies in og**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/og/exp_multiple/delete/delete-more-permissive-2.json](../samples/og/exp_multiple/delete/delete-more-permissive-2.json)|[../samples/og/exp_multiple/delete/delete-more-permissive-1.json](../samples/og/exp_multiple/delete/delete-more-permissive-1.json)|UNSAT|79.3317|-|-|-|-|-|SAT|118.329|1600.0112931259464|20.9961|0.0|800.0056465628053|800.0056465631411|
|[../samples/og/exp_multiple/prefix/s3-prefix-incomparable-2.json](../samples/og/exp_multiple/prefix/s3-prefix-incomparable-2.json)|[../samples/og/exp_multiple/prefix/s3-prefix-incomparable-1.json](../samples/og/exp_multiple/prefix/s3-prefix-incomparable-1.json)|SAT|591.494|2144.0169396894235|167.03|800.0056465631411|0.0|584.0056465631411|SAT|534.011|2056.0169396894235|129.114|800.0056465631411|0.0|584.0056465631411|
|[../samples/og/exp_multiple/numeric/numeric-equivalent-1.json](../samples/og/exp_multiple/numeric/numeric-equivalent-1.json)|[../samples/og/exp_multiple/numeric/numeric-equivalent-2.json](../samples/og/exp_multiple/numeric/numeric-equivalent-2.json)|UNSAT|114.635|-|-|-|-|-|UNSAT|85.5334|-|-|-|-|-|

**Policies in og**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy 1|Policy 2|P1 =>P2 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|P2 =>P1 SAT/UNSAT|Time (ms)|log base 2 Count|Count Time (ms)|log base 2 Principal Count|log base 2 Action Count|log base 2 Resource Count|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|[../samples/og/exp_multiple/delete/delete-more-permissive-2.json](../samples/og/exp_multiple/delete/delete-more-permissive-2.json)|[../samples/og/exp_multiple/delete/delete-more-permissive-1.json](../samples/og/exp_multiple/delete/delete-more-permissive-1.json)|UNSAT|3108.78|-|-|-|-|-|SAT|6076.13|467.2792770072253|37.3918|0.0|1.5849625007211563|467.2792770072253|
|[../samples/og/exp_multiple/prefix/s3-prefix-incomparable-2.json](../samples/og/exp_multiple/prefix/s3-prefix-incomparable-2.json)|[../samples/og/exp_multiple/prefix/s3-prefix-incomparable-1.json](../samples/og/exp_multiple/prefix/s3-prefix-incomparable-1.json)|SAT|1555.59|2144.0169396894235|155.1|800.0056465631411|0.0|584.0056465631411|SAT|1281.92|2056.0169396894235|122.425|800.0056465631411|0.0|584.0056465631411|
|[../samples/og/exp_multiple/numeric/numeric-equivalent-1.json](../samples/og/exp_multiple/numeric/numeric-equivalent-1.json)|[../samples/og/exp_multiple/numeric/numeric-equivalent-2.json](../samples/og/exp_multiple/numeric/numeric-equivalent-2.json)|UNSAT|731.227|-|-|-|-|-|UNSAT|726.008|-|-|-|-|-|
