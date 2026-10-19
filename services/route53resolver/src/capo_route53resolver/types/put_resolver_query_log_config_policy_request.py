"""Generated from Smithy shape ``com.amazonaws.route53resolver#PutResolverQueryLogConfigPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.resolver_query_log_config_policy


class PutResolverQueryLogConfigPolicyRequest(TypedDict, closed=True):
    arn: "capo_route53resolver.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the account that you want to share rules with.</p>"""
    resolver_query_log_config_policy: "capo_route53resolver.types.resolver_query_log_config_policy.ResolverQueryLogConfigPolicy"
    """<p>An Identity and Access Management policy statement that lists the query logging configurations that you want to share with another Amazon Web Services account and the operations that you want the account to be able to perform. You can specify the following operations in the <code>Actions</code> section of the statement:</p> <ul> <li> <p> <code>route53resolver:AssociateResolverQueryLogConfig</code> </p> </li> <li> <p> <code>route53resolver:DisassociateResolverQueryLogConfig</code> </p> </li> <li> <p> <code>route53resolver:ListResolverQueryLogConfigs</code> </p> </li> </ul> <p>In the <code>Resource</code> section of the statement, you specify the ARNs for the query logging configurations that you want to share with the account that you specified in <code>Arn</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResolverQueryLogConfigPolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ResolverQueryLogConfigPolicy"] = value["resolver_query_log_config_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResolverQueryLogConfigPolicyRequest:
    out: PutResolverQueryLogConfigPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ResolverQueryLogConfigPolicy") is not None:
        out["resolver_query_log_config_policy"] = data["ResolverQueryLogConfigPolicy"]
    else:
        out["resolver_query_log_config_policy"] = ""
    return out
