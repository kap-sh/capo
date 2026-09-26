"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#FirewallSyncReason``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_network_security_manager.types.invalid_firewall_reasons


class _FirewallSyncReason_missingFirewall(TypedDict, closed=True):
    missingFirewall: "str"


class _FirewallSyncReason_invalidFirewall(TypedDict, closed=True):
    invalidFirewall: "capo_network_security_manager.types.invalid_firewall_reasons.InvalidFirewallReasons"


FirewallSyncReason: TypeAlias = (
    _FirewallSyncReason_missingFirewall | _FirewallSyncReason_invalidFirewall
)


# --- restJson1 ser/de ---
def serialize_json(value: FirewallSyncReason) -> dict:
    if "missingFirewall" in value:
        return {"missingFirewall": value["missingFirewall"]}
    elif "invalidFirewall" in value:
        import capo_network_security_manager.types.invalid_firewall_reasons

        return {
            "invalidFirewall": capo_network_security_manager.types.invalid_firewall_reasons.serialize_json(
                value["invalidFirewall"]
            )
        }
    else:
        raise SerializationError("FirewallSyncReason: no variant present")


def deserialize_json(data: dict) -> FirewallSyncReason:
    if data.get("missingFirewall") is not None:
        return {"missingFirewall": data["missingFirewall"]}
    elif data.get("invalidFirewall") is not None:
        import capo_network_security_manager.types.invalid_firewall_reasons

        return {
            "invalidFirewall": capo_network_security_manager.types.invalid_firewall_reasons.deserialize_json(
                data["invalidFirewall"]
            )
        }
    else:
        raise DeserializationError("FirewallSyncReason: no recognized variant key")
