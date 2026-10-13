"""Generated from Smithy shape ``com.amazonaws.drs#StartSourceNetworkRecoveryRequestNetworkEntries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.start_source_network_recovery_request_network_entry

StartSourceNetworkRecoveryRequestNetworkEntries: TypeAlias = list[
    "capo_drs.types.start_source_network_recovery_request_network_entry.StartSourceNetworkRecoveryRequestNetworkEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: StartSourceNetworkRecoveryRequestNetworkEntries) -> list:
    import capo_drs.types.start_source_network_recovery_request_network_entry

    out: list = []
    for item in value:
        out.append(
            capo_drs.types.start_source_network_recovery_request_network_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StartSourceNetworkRecoveryRequestNetworkEntries:
    import capo_drs.types.start_source_network_recovery_request_network_entry

    out: StartSourceNetworkRecoveryRequestNetworkEntries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_drs.types.start_source_network_recovery_request_network_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: StartSourceNetworkRecoveryRequestNetworkEntries,
) -> list[Any]:
    import capo_drs.types.start_source_network_recovery_request_network_entry

    return [
        capo_drs.types.start_source_network_recovery_request_network_entry.redact_sensitive(
            item
        )
        for item in value
    ]
