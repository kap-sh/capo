"""Generated from Smithy shape ``com.amazonaws.route53resolver#PutResolverRulePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.resolver_rule_policy


class PutResolverRulePolicyRequest(TypedDict, closed=True):
    arn: "capo_route53resolver.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the rule that you want to share with another account.</p>"""
    resolver_rule_policy: (
        "capo_route53resolver.types.resolver_rule_policy.ResolverRulePolicy"
    )
    """<p>An Identity and Access Management policy statement that lists the rules that you want to share with another Amazon Web Services account and the operations that you want the account to be able to perform. You can specify the following operations in the <code>Action</code> section of the statement:</p> <ul> <li> <p> <code>route53resolver:GetResolverRule</code> </p> </li> <li> <p> <code>route53resolver:AssociateResolverRule</code> </p> </li> <li> <p> <code>route53resolver:DisassociateResolverRule</code> </p> </li> <li> <p> <code>route53resolver:ListResolverRules</code> </p> </li> <li> <p> <code>route53resolver:ListResolverRuleAssociations</code> </p> </li> </ul> <p>In the <code>Resource</code> section of the statement, specify the ARN for the rule that you want to share with another account. Specify the same ARN that you specified in <code>Arn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutResolverRulePolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["ResolverRulePolicy"] = value["resolver_rule_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutResolverRulePolicyRequest:
    out: PutResolverRulePolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ResolverRulePolicy") is not None:
        out["resolver_rule_policy"] = data["ResolverRulePolicy"]
    else:
        out["resolver_rule_policy"] = ""
    return out
