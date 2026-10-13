"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveredDeviceListDefinition``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.discovered_device_summary

DiscoveredDeviceListDefinition: TypeAlias = list[
    "capo_iot_managed_integrations.types.discovered_device_summary.DiscoveredDeviceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredDeviceListDefinition) -> list:
    import capo_iot_managed_integrations.types.discovered_device_summary

    out: list = []
    for item in value:
        out.append(
            capo_iot_managed_integrations.types.discovered_device_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DiscoveredDeviceListDefinition:
    import capo_iot_managed_integrations.types.discovered_device_summary

    out: DiscoveredDeviceListDefinition = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_managed_integrations.types.discovered_device_summary.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: DiscoveredDeviceListDefinition) -> list[Any]:
    import capo_iot_managed_integrations.types.discovered_device_summary

    return [
        capo_iot_managed_integrations.types.discovered_device_summary.redact_sensitive(
            item
        )
        for item in value
    ]
