"""Generated from Smithy shape ``com.amazonaws.guardduty#NetworkInterfaces``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.network_interface

NetworkInterfaces: TypeAlias = list[
    "capo_guardduty.types.network_interface.NetworkInterface"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkInterfaces) -> list:
    import capo_guardduty.types.network_interface

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.network_interface.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkInterfaces:
    import capo_guardduty.types.network_interface

    out: NetworkInterfaces = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.network_interface.deserialize_json(item))
    return out


def redact_sensitive(value: NetworkInterfaces) -> list[Any]:
    import capo_guardduty.types.network_interface

    return [
        capo_guardduty.types.network_interface.redact_sensitive(item) for item in value
    ]
