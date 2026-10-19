"""Generated from Smithy shape ``com.amazonaws.route53resolver#PutFirewallRuleGroupPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.arn
    import capo_route53resolver.types.firewall_rule_group_policy


class PutFirewallRuleGroupPolicyRequest(TypedDict, closed=True):
    arn: "capo_route53resolver.types.arn.Arn"
    """<p>The ARN (Amazon Resource Name) for the rule group that you want to share.</p>"""
    firewall_rule_group_policy: (
        "capo_route53resolver.types.firewall_rule_group_policy.FirewallRuleGroupPolicy"
    )
    """<p>The Identity and Access Management (Amazon Web Services IAM) policy to attach to the rule group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFirewallRuleGroupPolicyRequest) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FirewallRuleGroupPolicy"] = value["firewall_rule_group_policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFirewallRuleGroupPolicyRequest:
    out: PutFirewallRuleGroupPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("FirewallRuleGroupPolicy") is not None:
        out["firewall_rule_group_policy"] = data["FirewallRuleGroupPolicy"]
    else:
        out["firewall_rule_group_policy"] = ""
    return out
