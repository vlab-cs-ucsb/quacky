
**Policies in s3**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json](../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json)|SAT|1751.56|2260.960065941997|87.8575|0.0|5.044394119358453|457.11157034269354|
|[../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json)|SAT|2197.13|628.9125371587496|87.1336|0.0|6.266786540694902|624.0056465631411|
|[../samples/s3/exp_single/s3_allow_all_except_delete/initial.json](../samples/s3/exp_single/s3_allow_all_except_delete/initial.json)|SAT|934.47|628.9125371587496|51.8959|0.0|4.906890595608519|624.0056465631411|
|[../samples/s3/exp_single/s3_public_access/policy.json](../samples/s3/exp_single/s3_public_access/policy.json)|SAT|764.559|1944.0169396894232|8.9024|800.0056465631411|0.0|544.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/policy1.json](../samples/s3/exp_single/s3_object_query_permissions/policy1.json)|SAT|1902.46|2284.906890620335|129.077|0.0|5.044394119358453|480.0056466622347|
|[../samples/s3/exp_single/s3_object_query_permissions/fix.json](../samples/s3/exp_single/s3_object_query_permissions/fix.json)|SAT|750.972|2.0|4.79351|0.0|1.0|0.0|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json)|SAT|683.527|657.5906090638623|6.33196|0.0|2.0|656.0056465631411|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json)|SAT|1337.44|572.9125371587496|45.8661|0.0|4.906890595608519|568.0056465631411|
|[../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json](../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json)|SAT|1090.94|636.9125371587497|72.0487|0.0|6.22881869049588|632.0056465631412|
|[../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json](../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json)|SAT|3991.11|2308.9068906171065|159.204|0.0|5.044394119358453|504.00564656314117|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json)|SAT|2539.37|2056.0169396894235|165.919|800.0056465631411|0.0|568.0056465631411|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json)|UNSAT|131.151|-|-|-|-|-|
|[../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json](../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json)|SAT|12697.6|1484.7372577648314|7040.84|800.0056465631411|6.507794640198696|679.8247206060817|
|[../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json](../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json)|SAT|720.853|1384.0112931262825|4.90342|800.0056465631411|0.0|584.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json)|SAT|3014.18|2348.9068906171065|94.6059|0.0|5.044394119358453|544.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json)|SAT|1425.84|2332.9068906171065|87.3443|0.0|5.0|528.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json)|SAT|970.564|5.0|34.6915|0.0|5.0|1.0|
|[../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json](../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json)|SAT|1541.43|1416.0112931262822|57.7337|800.0056465631411|5.523561956057013|616.0056465631411|
|[../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json](../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json)|SAT|96229.9|2076.923830285368|13773.4|800.0056465631411|4.906890595608519|632.0056465631412|
|[../samples/s3/exp_single/s3_policy_or_condition/policy.json](../samples/s3/exp_single/s3_policy_or_condition/policy.json)|SAT|952.071|2192.0169396894235|134.454|800.0056465631411|0.0|664.0056465631412|
