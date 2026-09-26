"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#FirewallTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.policy_firewall_type

FirewallTypeList: TypeAlias = list[
    "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType"
]


# --- restJson1 ser/de ---
def serialize_json(value: FirewallTypeList) -> list:
    import capo_network_security_manager.types.policy_firewall_type

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.policy_firewall_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> FirewallTypeList:
    import capo_network_security_manager.types.policy_firewall_type

    out: FirewallTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                item
            )
        )
    return out
