"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_metadata

FirewallPolicies: TypeAlias = list[
    "capo_network_firewall.types.firewall_policy_metadata.FirewallPolicyMetadata"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallPolicies) -> list:
    import capo_network_firewall.types.firewall_policy_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_policy_metadata.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> FirewallPolicies:
    import capo_network_firewall.types.firewall_policy_metadata

    out: FirewallPolicies = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_policy_metadata.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FirewallPolicies) -> list:
    import capo_network_firewall.types.firewall_policy_metadata

    out: list = []
    for item in value:
        out.append(
            capo_network_firewall.types.firewall_policy_metadata.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> FirewallPolicies:
    import capo_network_firewall.types.firewall_policy_metadata

    out: FirewallPolicies = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_firewall.types.firewall_policy_metadata.deserialize_cbor(item)
        )
    return out
