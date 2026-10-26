"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#FirewallSyncReason``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_network_security_manager.errors import (
    DeserializationError,
    SerializationError,
)
from capo_network_security_manager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_network_security_manager.types.invalid_firewall_reasons


class _FirewallSyncReason_missingFirewall(TypedDict, closed=True):
    missingFirewall: "str"


class _FirewallSyncReason_invalidFirewall(TypedDict, closed=True):
    invalidFirewall: "capo_network_security_manager.types.invalid_firewall_reasons.InvalidFirewallReasons"


FirewallSyncReason: TypeAlias = (
    _FirewallSyncReason_missingFirewall
    | _FirewallSyncReason_invalidFirewall
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FirewallSyncReason) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FirewallSyncReason: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "missingFirewall" in value:
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
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FirewallSyncReason: no recognized variant key")
