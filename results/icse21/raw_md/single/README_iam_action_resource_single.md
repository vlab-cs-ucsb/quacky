
**Policies in iam**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|1539.64|587.8130014851988|130.766|0.0|4.392317422778761|584.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|904.718|586.3275746580285|11.4283|0.0|3.0|584.0056465631411|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|1427.67|482.8226191555779|11.704|0.0|2.321928094887362|480.5006910606906|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|859.917|1324.918183721891|34.3344|800.0056465631411|4.906890595608519|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|672.525|0.0|4.41689|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|1016.82|416.40090563401435|15.7391|0.0|1.0|415.40090563401435|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|998.588|1281.5063376238318|11.1803|0.0|1.0|480.5006910606906|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|6236.52|684.7316112016902|1038.85|0.0|7.857980995127572|679.8247206060817|

