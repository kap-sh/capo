"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#OutOfSyncReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.firewall_sync_reason
    import capo_network_security_manager.types.policy_firewall_type

OutOfSyncReasons: TypeAlias = dict[
    "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType",
    "capo_network_security_manager.types.firewall_sync_reason.FirewallSyncReason",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: OutOfSyncReasons) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_network_security_manager.types.firewall_sync_reason
        import capo_network_security_manager.types.policy_firewall_type

        out[
            capo_network_security_manager.types.policy_firewall_type.serialize_json(key)
        ] = capo_network_security_manager.types.firewall_sync_reason.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> OutOfSyncReasons:
    out: OutOfSyncReasons = {}
    for key, value in data.items():
        import capo_network_security_manager.types.policy_firewall_type

        if value is None:
            continue
        import capo_network_security_manager.types.firewall_sync_reason

        out[
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                key
            )
        ] = capo_network_security_manager.types.firewall_sync_reason.deserialize_json(
            value
        )
    return out
