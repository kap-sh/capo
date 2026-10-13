"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterEvents``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_event_id
    import capo_iot_managed_integrations.types.matter_fields

MatterEvents: TypeAlias = dict[
    "capo_iot_managed_integrations.types.matter_event_id.MatterEventId",
    "capo_iot_managed_integrations.types.matter_fields.MatterFields",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MatterEvents) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MatterEvents:
    out: MatterEvents = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: MatterEvents) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
