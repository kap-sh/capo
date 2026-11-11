"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPoliciesV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_v2_metadata

FirewallPoliciesV2: TypeAlias = list[
    "capo_network_firewall.types.firewall_policy_v2_metadata.FirewallPolicyV2Metadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPoliciesV2) -> list:
    import capo_network_firewall.types.firewall_policy_v2_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_policy_v2_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FirewallPoliciesV2:
    import capo_network_firewall.types.firewall_policy_v2_metadata

    out: FirewallPoliciesV2 = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_policy_v2_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out
