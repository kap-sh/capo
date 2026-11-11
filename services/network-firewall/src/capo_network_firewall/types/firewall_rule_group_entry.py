"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRuleGroupEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_rule_group
    import capo_network_firewall.types.priority
    import capo_network_firewall.types.resource_arn


class FirewallRuleGroupEntry(TypedDict, closed=True):
    priority: NotRequired["capo_network_firewall.types.priority.Priority"]
    """<p>The priority of the rule group entry within the firewall section. Network Firewall evaluates the firewall section's entries in order of increasing priority value. Each entry in the firewall section must have a unique priority.</p>"""
    resource_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of an existing firewall engine rule group to reference in this entry. Provide either <code>ResourceArn</code> to reference an existing rule group or <code>InlineRuleGroup</code> to embed a rule group in the policy.</p>"""
    inline_rule_group: NotRequired[
        "capo_network_firewall.types.firewall_rule_group.FirewallRuleGroup"
    ]
    """<p>A firewall engine rule group defined directly in the policy, instead of referenced by ARN. Provide either <code>InlineRuleGroup</code> to embed a rule group or <code>ResourceArn</code> to reference an existing rule group. An embedded rule group can't use a domain list rules source; to filter on a domain list, reference a standalone rule group by ARN instead.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRuleGroupEntry) -> dict:
    out: dict = {}
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "inline_rule_group" in value:
        import capo_network_firewall.types.firewall_rule_group

        out["InlineRuleGroup"] = (
            capo_network_firewall.types.firewall_rule_group.serialize_aws_json_1_0(
                value["inline_rule_group"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FirewallRuleGroupEntry:
    out: FirewallRuleGroupEntry = {}  # type: ignore[typeddict-item]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("InlineRuleGroup") is not None:
        import capo_network_firewall.types.firewall_rule_group

        out["inline_rule_group"] = (
            capo_network_firewall.types.firewall_rule_group.deserialize_aws_json_1_0(
                data["InlineRuleGroup"]
            )
        )
    return out
