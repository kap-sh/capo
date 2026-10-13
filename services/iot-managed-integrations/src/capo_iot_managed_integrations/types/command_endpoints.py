"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandEndpoints``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.command_endpoint

CommandEndpoints: TypeAlias = list[
    "capo_iot_managed_integrations.types.command_endpoint.CommandEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: CommandEndpoints) -> list:
    import capo_iot_managed_integrations.types.command_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.command_endpoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CommandEndpoints:
    import capo_iot_managed_integrations.types.command_endpoint

    out: CommandEndpoints = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.command_endpoint.deserialize_json(item)
        )
    return out


def redact_sensitive(value: CommandEndpoints) -> list[Any]:
    import capo_iot_managed_integrations.types.command_endpoint

    return [
        capo_iot_managed_integrations.types.command_endpoint.redact_sensitive(item)
        for item in value
    ]
