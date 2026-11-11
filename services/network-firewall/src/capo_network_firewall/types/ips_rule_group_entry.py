"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IpsRuleGroupEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.ips_rule_group
    import capo_network_firewall.types.ips_rule_group_override
    import capo_network_firewall.types.resource_arn


class IpsRuleGroupEntry(TypedDict, closed=True):
    resource_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of an existing IPS engine rule group to reference in this entry. Provide either <code>ResourceArn</code> to reference an existing rule group or <code>InlineRuleGroup</code> to embed a rule group in the policy.</p>"""
    inline_rule_group: NotRequired[
        "capo_network_firewall.types.ips_rule_group.IpsRuleGroup"
    ]
    """<p>An IPS engine rule group defined directly in the policy, instead of referenced by ARN. Provide either <code>InlineRuleGroup</code> to embed a rule group or <code>ResourceArn</code> to reference an existing rule group.</p>"""
    override: NotRequired[
        "capo_network_firewall.types.ips_rule_group_override.IpsRuleGroupOverride"
    ]
    """<p>The setting that allows the policy owner to change the behavior of the IPS engine rule group within this policy, such as changing a managed rule group's action from <code>DROP</code> to <code>ALERT</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IpsRuleGroupEntry) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "inline_rule_group" in value:
        import capo_network_firewall.types.ips_rule_group

        out["InlineRuleGroup"] = (
            capo_network_firewall.types.ips_rule_group.serialize_aws_json_1_0(
                value["inline_rule_group"]
            )
        )
    if "override" in value:
        import capo_network_firewall.types.ips_rule_group_override

        out["Override"] = (
            capo_network_firewall.types.ips_rule_group_override.serialize_aws_json_1_0(
                value["override"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IpsRuleGroupEntry:
    out: IpsRuleGroupEntry = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("InlineRuleGroup") is not None:
        import capo_network_firewall.types.ips_rule_group

        out["inline_rule_group"] = (
            capo_network_firewall.types.ips_rule_group.deserialize_aws_json_1_0(
                data["InlineRuleGroup"]
            )
        )
    if data.get("Override") is not None:
        import capo_network_firewall.types.ips_rule_group_override

        out["override"] = (
            capo_network_firewall.types.ips_rule_group_override.deserialize_aws_json_1_0(
                data["Override"]
            )
        )
    return out
