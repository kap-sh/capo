"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRuleGroupEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_rule_group_entry

FirewallRuleGroupEntries: TypeAlias = list[
    "capo_network_firewall.types.firewall_rule_group_entry.FirewallRuleGroupEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRuleGroupEntries) -> list:
    import capo_network_firewall.types.firewall_rule_group_entry

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_rule_group_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FirewallRuleGroupEntries:
    import capo_network_firewall.types.firewall_rule_group_entry

    out: FirewallRuleGroupEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_rule_group_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
