
**Policies in s3**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json](../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json)|SAT|183.535|3032.0112711124193|109.821|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json)|SAT|390.667|1400.0112931262822|121.937|0.0|776.0056465631412|800.0056465631411|
|[../samples/s3/exp_single/s3_allow_all_except_delete/initial.json](../samples/s3/exp_single/s3_allow_all_except_delete/initial.json)|SAT|77.2545|1400.0112931262822|14.591|0.0|776.0056465631412|624.0056465631411|
|[../samples/s3/exp_single/s3_public_access/policy.json](../samples/s3/exp_single/s3_public_access/policy.json)|SAT|72.4349|1944.0169396894232|8.46625|800.0056465631411|0.0|544.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/policy1.json](../samples/s3/exp_single/s3_object_query_permissions/policy1.json)|SAT|273.808|3056.0112711124193|210.059|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/fix.json](../samples/s3/exp_single/s3_object_query_permissions/fix.json)|SAT|10.0254|2.0|4.50336|0.0|1.0|0.0|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json)|SAT|39.7048|657.5906090638623|8.11582|0.0|2.0|656.0056465631411|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json)|SAT|224.653|1344.0112931262822|34.0082|0.0|776.0056465631412|568.0056465631411|
|[../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json](../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json)|SAT|26.0454|1408.0112931262822|3.11946|0.0|776.0056465631412|632.0056465631412|
|[../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json](../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json)|SAT|1900.08|3080.0112711124193|235.243|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json)|SAT|1457.66|2056.0169396894235|162.084|800.0056465631411|0.0|568.0056465631411|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json)|UNSAT|108.924|-|-|-|-|-|
|[../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json](../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json)|SAT|185.641|2376.0169396894235|4761.2|800.0056465631411|776.0056465631412|800.0056465631411|
|[../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json](../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json)|SAT|67.1766|1384.0112931262825|9.39618|800.0056465631411|0.0|584.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json)|SAT|1774.44|3120.0112711124193|94.7906|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json)|SAT|225.829|3104.0112711124193|79.1101|0.0|776.0056465631412|696.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json)|SAT|74.854|776.0056465631412|37.9037|0.0|776.0056465631412|1.0|
|[../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json](../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json)|SAT|108.174|1416.0112931262822|49.9523|800.0056465631411|776.0056465631412|616.0056465631411|
|[../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json](../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json)|SAT|67367|2872.0225862529|119443|800.0056465631411|800.0056465631411|632.0056465631412|
|[../samples/s3/exp_single/s3_policy_or_condition/policy.json](../samples/s3/exp_single/s3_policy_or_condition/policy.json)|SAT|660.829|2192.0169396894235|130.519|800.0056465631411|0.0|664.0056465631412|

**Policies in s3**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json](../samples/s3/exp_single/s3_iam_user_cannot_create_folder_through_console/policy.json)|SAT|1709.69|2260.960065941997|88.6068|0.0|5.044394119358453|457.11157034269354|
|[../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json](../samples/s3/exp_single/s3_allow_all_except_delete/fixed.json)|SAT|2214.6|628.9125371587496|86.5559|0.0|6.266786540694902|624.0056465631411|
|[../samples/s3/exp_single/s3_allow_all_except_delete/initial.json](../samples/s3/exp_single/s3_allow_all_except_delete/initial.json)|SAT|973.227|628.9125371587496|49.641|0.0|4.906890595608519|624.0056465631411|
|[../samples/s3/exp_single/s3_public_access/policy.json](../samples/s3/exp_single/s3_public_access/policy.json)|SAT|829.56|1944.0169396894232|13.2618|800.0056465631411|0.0|544.0056465631412|
|[../samples/s3/exp_single/s3_object_query_permissions/policy1.json](../samples/s3/exp_single/s3_object_query_permissions/policy1.json)|SAT|1990.79|2284.906890620335|127.836|0.0|5.044394119358453|480.0056466622347|
|[../samples/s3/exp_single/s3_object_query_permissions/fix.json](../samples/s3/exp_single/s3_object_query_permissions/fix.json)|SAT|705.284|2.0|4.91379|0.0|1.0|0.0|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy2.json)|SAT|754.812|657.5906090638623|6.52347|0.0|2.0|656.0056465631411|
|[../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json](../samples/s3/exp_single/s3_policy_for_lambda_function/policy1.json)|SAT|1263.06|572.9125371587496|46.0218|0.0|4.906890595608519|568.0056465631411|
|[../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json](../samples/s3/exp_single/s3_restrict_access_to_certain_roles/policy.json)|SAT|972.742|636.9125371587497|68.9939|0.0|6.22881869049588|632.0056465631412|
|[../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json](../samples/s3/exp_single/s3_bucket_folder_restrict_by_user/policy.json)|SAT|3824.75|2308.9068906171065|157.63|0.0|5.044394119358453|504.00564656314117|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy2.json)|SAT|2434.88|2056.0169396894235|163.776|800.0056465631411|0.0|568.0056465631411|
|[../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json](../samples/s3/exp_single/s3_remove_permissions_individual_files/policy1.json)|UNSAT|207.64|-|-|-|-|-|
|[../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json](../samples/s3/exp_single/s3_policy_failing_not_sure_why/policy.json)|SAT|12369.7|1484.7372577648314|6846.32|800.0056465631411|6.507794640198696|679.8247206060817|
|[../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json](../samples/s3/exp_single/s3_bucket_policy_grant_read_specific_file_type/policy.json)|SAT|732.057|1384.0112931262825|4.91525|800.0056465631411|0.0|584.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy3.json)|SAT|2902.99|2348.9068906171065|92.2619|0.0|5.044394119358453|544.0056465631412|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy2.json)|SAT|1458.78|2332.9068906171065|87.7017|0.0|5.0|528.0056465631411|
|[../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json](../samples/s3/exp_single/s3_policy_provides_programmatic_access/policy1.json)|SAT|943.887|5.0|34.3542|0.0|5.0|1.0|
|[../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json](../samples/s3/exp_single/s3_policy_public_and_principal_specific_permissions/policy.json)|SAT|1528.54|1416.0112931262822|56.3554|800.0056465631411|5.523561956057013|616.0056465631411|
|[../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json](../samples/s3/exp_single/s3_sos_bucket_policy_problem/policy.json)|SAT|94804|2076.923830285368|13462.1|800.0056465631411|4.906890595608519|632.0056465631412|
|[../samples/s3/exp_single/s3_policy_or_condition/policy.json](../samples/s3/exp_single/s3_policy_or_condition/policy.json)|SAT|1012.25|2192.0169396894235|132.473|800.0056465631411|0.0|664.0056465631412|
