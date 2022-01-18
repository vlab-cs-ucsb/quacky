
**Policies in iam**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|2205.95|587.8130014851988|130.431|0.0|4.392317422778761|584.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|1471.07|586.3275746580285|11.2831|0.0|3.0|584.0056465631411|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|1482.87|482.8226191555779|11.4608|0.0|2.321928094887362|480.5006910606906|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|1432.44|1324.918183721891|33.478|800.0056465631411|4.906890595608519|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|1143.25|0.0|4.2271|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|1044.34|409.8463317267081|17.5168|0.0|1.0|408.8463317267081|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|1060.98|1281.5063376238318|11.0851|0.0|1.0|480.5006910606906|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|8714.43|684.7316112016902|1304.6|0.0|8.108524456778168|679.8247206060817|
