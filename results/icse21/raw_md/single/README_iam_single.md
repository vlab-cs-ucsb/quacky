
**Policies in iam**

bound: `100`, variables: `True`, constraints: `True`, smt-lib: `False`

|Policy|SAT/UNSAT|Solve Time (ms)|lg(tuple)|Count Time (ms)|lg(principal)|lg(action)|lg(resource)|
|-|-|-|-|-|-|-|-|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/fixed.json)|SAT|999.888|802.5906090638623|57.6846|0.0|4.392317422778761|800.0056465631411|
|[../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json](../samples/iam/exp_single/iam_user_access_to_s3_uploads_fail/initial.json)|SAT|626.023|696.0056465631412|13.7946|0.0|3.0|696.0056465631412|
|[../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json](../samples/iam/exp_single/iam_role_policy_modify_iam_but_not_own_policies/policy.json)|SAT|902.851|802.3275746580285|9.26771|0.0|2.321928094887362|800.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy2.json)|SAT|399.48|1326.5190877664809|31.5258|800.0056465631411|6.507794640198696|520.0056465631411|
|[../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json](../samples/iam/exp_single/iam_specify_all_users_in_account_bucket_policy/policy1.json)|SAT|351.421|0.0|5.03261|0.0|0.0|0.0|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/fixed.json)|SAT|950.297|575.1754929842821|5.78805|0.0|1.0|574.1754929842821|
|[../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json](../samples/iam/exp_single/iam_policy_allow_adding_deleting_users/initial.json)|SAT|908.496|1601.0112931262822|4.38244|0.0|1.0|800.0056465631411|
|[../samples/iam/exp_single/iam_simplest_policy/policy.json](../samples/iam/exp_single/iam_simplest_policy/policy.json)|SAT|2269.45|807.8636275582688|75.5522|0.0|7.857980995127572|800.0056465631411|
