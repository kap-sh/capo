"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandCapabilities``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.command_capability

CommandCapabilities: TypeAlias = list[
    "capo_iot_managed_integrations.types.command_capability.CommandCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandCapabilities) -> list:
    import capo_iot_managed_integrations.types.command_capability

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.command_capability.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommandCapabilities:
    import capo_iot_managed_integrations.types.command_capability

    out: CommandCapabilities = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.command_capability.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: CommandCapabilities) -> list[Any]:
    import capo_iot_managed_integrations.types.command_capability

    return [
        capo_iot_managed_integrations.types.command_capability.redact_sensitive(item)
        for item in value
    ]
