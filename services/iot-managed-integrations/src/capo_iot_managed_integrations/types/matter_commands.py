"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCommands``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.matter_command_id
    import capo_iot_managed_integrations.types.matter_fields

MatterCommands: TypeAlias = dict[
    "capo_iot_managed_integrations.types.matter_command_id.MatterCommandId",
    "capo_iot_managed_integrations.types.matter_fields.MatterFields",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MatterCommands) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MatterCommands:
    out: MatterCommands = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


def redact_sensitive(value: MatterCommands) -> dict[str, Any]:
    return dict.fromkeys(value, "*** Sensitive Data Redacted ***")
