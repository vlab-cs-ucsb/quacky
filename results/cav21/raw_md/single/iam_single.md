
**Policies in iam**

bound: `100`, variables: `True`, constraints: `False`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|177.16|1288.0112931262822|55.9881|0.0|704.0056465631411|800.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|65.5511|696.0056465631412|14.2168|0.0|3.0|696.0056465631412|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|24.2035|802.3275746580285|17.1294|0.0|2.321928094887362|800.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|62.4442|2096.0169396894235|5.54523|800.0056465631411|776.0056465631412|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|7.89966|0.0|5.22989|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|108.466|567.155313995549|8.15402|0.0|1.0|566.155313995549|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|30.6762|1601.0112931262822|6.73464|0.0|1.0|800.0056465631411|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|6.79653|1600.0112931262822|1.34504|0.0|800.0056465631411|800.0056465631411|

**Policies in iam**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|1507.29|587.8130014851988|131.126|0.0|4.392317422778761|584.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|942.496|586.3275746580285|11.236|0.0|3.0|584.0056465631411|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|1458.47|482.8226191555779|11.7221|0.0|2.321928094887362|480.5006910606906|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|936.239|1324.918183721891|32.8775|800.0056465631411|4.906890595608519|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|594.009|0.0|4.22425|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|1068.59|409.8463317267081|17.3035|0.0|1.0|408.8463317267081|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|1089.53|1281.5063376238318|11.105|0.0|1.0|480.5006910606906|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|6112.06|684.7316112016902|1024.11|0.0|7.857980995127572|679.8247206060817|
