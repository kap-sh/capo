"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#Devices``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.device

Devices: TypeAlias = list["capo_iot_managed_integrations.types.device.Device"]


# --- restJson1 ser/de ---
def serialize_json(value: Devices) -> list:
    import capo_iot_managed_integrations.types.device

    out: list = []
    for item in value:
        out.append(capo_iot_managed_integrations.types.device.serialize_json(item))
    return out


def deserialize_json(data: list) -> Devices:
    import capo_iot_managed_integrations.types.device

    out: Devices = []
    for item in data:
        if item is None:
            continue
        out.append(capo_iot_managed_integrations.types.device.deserialize_json(item))
    return out


def redact_sensitive(value: Devices) -> list[Any]:
    import capo_iot_managed_integrations.types.device

    return [
        capo_iot_managed_integrations.types.device.redact_sensitive(item)
        for item in value
    ]
