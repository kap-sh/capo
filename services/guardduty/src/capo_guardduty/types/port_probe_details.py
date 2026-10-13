"""Generated from Smithy shape ``com.amazonaws.guardduty#PortProbeDetails``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.port_probe_detail

PortProbeDetails: TypeAlias = list[
    "capo_guardduty.types.port_probe_detail.PortProbeDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: PortProbeDetails) -> list:
    import capo_guardduty.types.port_probe_detail

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.port_probe_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortProbeDetails:
    import capo_guardduty.types.port_probe_detail

    out: PortProbeDetails = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.port_probe_detail.deserialize_json(item))
    return out


def redact_sensitive(value: PortProbeDetails) -> list[Any]:
    import capo_guardduty.types.port_probe_detail

    return [
        capo_guardduty.types.port_probe_detail.redact_sensitive(item) for item in value
    ]
