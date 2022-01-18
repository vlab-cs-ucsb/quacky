# Manual Analysis
These policies were hand-crafted for count verification. When translated with the given domain in each folder, they allow a small number of request contexts that can be verified by manual analysis and iteration over the models that Z3 produces. They are variations on [this policy](../../samples/william/exp_single/s3_restrict_access_to_certain_roles/policy.json). 

**Counts**
|Policy|ABC Count|Z3 Count|
|-|-|-|
|[s3_allow_prefix/policy.json](s3_allow_prefix/policy.json)|2|2|
|[s3_allow_notprincipal/policy.json](s3_allow_notprincipal/policy.json)|15|15|
|[s3_allow_notresource/policy.json](s3_allow_notresource/policy.json)|12|12|
|[s3_allow_pstar/policy.json](s3_allow_pstar/policy.json)|6|6|
|[s3_allow_3/policy.json](s3_allow_3/policy.json)|3|3|
|[s3_allow_rstar/policy.json](s3_allow_rstar/policy.json)|9|9|
|[s3_deny_resource/policy.json](s3_deny_resource/policy.json)|12|12|
|[s3_allow_principals/policy.json](s3_allow_principals/policy.json)|6|6|
|[s3_deny_notresource/policy.json](s3_deny_notresource/policy.json)|3|3|

**Percentage of Domain Allowed**
|Policy|ABC Policy Count|log2(ABC Domain Count)|ABC Policy Count/ ABC Domain Count|
|-|-|-|-|
|[../samples/manual_s3/exp_single/s3_allow_prefix/policy.json](../samples/manual_s3/exp_single/s3_allow_prefix/policy.json)|2|7.813781191217037|0.008888888888888889|
|[../samples/manual_s3/exp_single/s3_allow_notprincipal/policy.json](../samples/manual_s3/exp_single/s3_allow_notprincipal/policy.json)|15|10.621136113274641|0.009523809523809525|
|[../samples/manual_s3/exp_single/s3_allow_notresource/policy.json](../samples/manual_s3/exp_single/s3_allow_notresource/policy.json)|12|7.813781191217037|0.05333333333333334|
|[../samples/manual_s3/exp_single/s3_allow_pstar/policy.json](../samples/manual_s3/exp_single/s3_allow_pstar/policy.json)|6|10.621136113274641|0.0038095238095238095|
|[../samples/manual_s3/exp_single/s3_allow_3/policy.json](../samples/manual_s3/exp_single/s3_allow_3/policy.json)|3|7.813781191217037|0.013333333333333334|
|[../samples/manual_s3/exp_single/s3_allow_rstar/policy.json](../samples/manual_s3/exp_single/s3_allow_rstar/policy.json)|9|8.29920801838728|0.02857142857142857|
|[../samples/manual_s3/exp_single/s3_deny_resource/policy.json](../samples/manual_s3/exp_single/s3_deny_resource/policy.json)|12|7.813781191217037|0.05333333333333334|
|[../samples/manual_s3/exp_single/s3_allow_principals/policy.json](../samples/manual_s3/exp_single/s3_allow_principals/policy.json)|6|10.621136113274641|0.0038095238095238095|
|[../samples/manual_s3/exp_single/s3_deny_notresource/policy.json](../samples/manual_s3/exp_single/s3_deny_notresource/policy.json)|3|7.813781191217037|0.013333333333333334|
