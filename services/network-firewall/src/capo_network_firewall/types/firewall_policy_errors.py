"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicyErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_error

FirewallPolicyErrors: TypeAlias = list[
    "capo_network_firewall.types.firewall_policy_error.FirewallPolicyError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicyErrors) -> list:
    import capo_network_firewall.types.firewall_policy_error

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_policy_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FirewallPolicyErrors:
    import capo_network_firewall.types.firewall_policy_error

    out: FirewallPolicyErrors = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_policy_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
