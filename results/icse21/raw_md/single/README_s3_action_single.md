
**Policies in s3**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json](../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json)|SAT|1775.81|2497.000000021498|166.525|0.0|6.507794640198696|696.0056465631412|
|[../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json)|SAT|1497.41|802.3275746580285|154.947|0.0|6.507794640198696|800.0056465631411|
|[../samples/s3/exp_single/s3_allow_all_except_delete/initial.json](../samples/s3/exp_single/s3_allow_all_except_delete/initial.json)|SAT|1597.76|630.5134412033399|123.167|0.0|6.507794640198696|624.0056465631411|
|[../samples/s3/exp_single/s3_public_access/policy.json](../samples/s3/exp_single/s3_public_access/policy.json)|SAT|477.729|1944.0169396894232|8.42006|800.0056465631411|0.0|544.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/policy1.json](../samples/s3/exp_single/s3_object_query_permissions/policy1.json)|SAT|2092.23|2497.000000021498|209.832|0.0|6.507794640198696|696.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/fix.json](../samples/s3/exp_single/s3_object_query_permissions/fix.json)|SAT|401.233|2.0|4.75475|0.0|1.0|0.0|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json)|SAT|541.07|657.5906090638623|6.21427|0.0|2.0|656.0056465631411|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json)|SAT|2742.11|574.5134412033399|108.694|0.0|6.507794640198696|568.0056465631411|
|[../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json](../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json)|SAT|436.887|638.5134412033399|30.3218|0.0|6.507794640198696|632.0056465631412|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json)|SAT|1508.26|2056.0169396894235|162.598|800.0056465631411|0.0|568.0056465631411|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json)|UNSAT|279.031|-|-|-|-|-|
|[../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json](../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json)|SAT|10176.6|1606.5190877664807|5320.98|800.0056465631411|6.507794640198696|800.0056465631411|
|[../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json](../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json)|SAT|364.769|1384.0112931262825|4.33175|800.0056465631411|0.0|584.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json)|SAT|7676.21|2497.000000021498|150.411|0.0|6.507794640198696|696.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json)|SAT|2044.33|2496.000000021498|145.166|0.0|6.507794640198696|696.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json)|SAT|838.454|6.539158811108032|82.5973|0.0|6.507794640198696|1.0|
|[../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json](../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json)|SAT|1118.64|1416.0112931262822|108.729|800.0056465631411|6.507794640198696|616.0056465631411|
|[../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json](../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json)|SAT|658340|2079.874920684887|123359|800.0056465631411|7.857980995127572|632.0056465631412|
|[../samples/s3/exp_single/s3_policy_or_condition/policy.json](../samples/s3/exp_single/s3_policy_or_condition/policy.json)|SAT|1369.23|2192.0169396894235|125.448|800.0056465631411|0.0|664.0056465631412|

