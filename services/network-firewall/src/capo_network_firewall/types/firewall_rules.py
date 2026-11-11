"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_rule

FirewallRules: TypeAlias = list[
    "capo_network_firewall.types.firewall_rule.FirewallRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRules) -> list:
    import capo_network_firewall.types.firewall_rule

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_rule.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FirewallRules:
    import capo_network_firewall.types.firewall_rule

    out: FirewallRules = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_rule.deserialize_aws_json_1_0(item)
        )
    return out
