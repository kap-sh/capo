"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorDeviceIdList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.connector_device_id

ConnectorDeviceIdList: TypeAlias = list[
    "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorDeviceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConnectorDeviceIdList:
    return [item for item in data if item is not None]


def redact_sensitive(value: ConnectorDeviceIdList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
