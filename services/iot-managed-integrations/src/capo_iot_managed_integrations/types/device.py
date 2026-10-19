"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#Device``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_schemas
    import capo_iot_managed_integrations.types.connector_device_id
    import capo_iot_managed_integrations.types.connector_device_name
    import capo_iot_managed_integrations.types.device_metadata
    import capo_iot_managed_integrations.types.matter_capability_report


class Device(TypedDict, closed=True):
    connector_device_id: (
        "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    )
    """<p>The device id as defined by the connector.</p> <note> <p>This parameter is used for cloud-to-cloud devices only.</p> </note>"""
    connector_device_name: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_name.ConnectorDeviceName"
    ]
    """<p>The name of the device as defined by the connector.</p>"""
    capability_report: "capo_iot_managed_integrations.types.matter_capability_report.MatterCapabilityReport"
    """<p>The capability report for the device.</p>"""
    capability_schemas: NotRequired[
        "capo_iot_managed_integrations.types.capability_schemas.CapabilitySchemas"
    ]
    """<p>Report of all capabilities supported by the device.</p>"""
    device_metadata: NotRequired[
        "capo_iot_managed_integrations.types.device_metadata.DeviceMetadata"
    ]
    """<p>The metadata attributes for a device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Device) -> dict:
    out: dict = {}
    out["ConnectorDeviceId"] = value["connector_device_id"]
    if "connector_device_name" in value:
        out["ConnectorDeviceName"] = value["connector_device_name"]
    import capo_iot_managed_integrations.types.matter_capability_report

    out["CapabilityReport"] = (
        capo_iot_managed_integrations.types.matter_capability_report.serialize_json(
            value["capability_report"]
        )
    )
    if "capability_schemas" in value:
        import capo_iot_managed_integrations.types.capability_schemas

        out["CapabilitySchemas"] = (
            capo_iot_managed_integrations.types.capability_schemas.serialize_json(
                value["capability_schemas"]
            )
        )
    if "device_metadata" in value:
        out["DeviceMetadata"] = value["device_metadata"]
    return out


def deserialize_json(data: dict) -> Device:
    out: Device = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorDeviceId") is not None:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    else:
        out["connector_device_id"] = ""
    if data.get("ConnectorDeviceName") is not None:
        out["connector_device_name"] = data["ConnectorDeviceName"]
    if data.get("CapabilityReport") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report

        out["capability_report"] = (
            capo_iot_managed_integrations.types.matter_capability_report.deserialize_json(
                data["CapabilityReport"]
            )
        )
    else:
        raise DeserializationError("Device.capability_report required")
    if data.get("CapabilitySchemas") is not None:
        import capo_iot_managed_integrations.types.capability_schemas

        out["capability_schemas"] = (
            capo_iot_managed_integrations.types.capability_schemas.deserialize_json(
                data["CapabilitySchemas"]
            )
        )
    if data.get("DeviceMetadata") is not None:
        out["device_metadata"] = data["DeviceMetadata"]
    return out


def redact_sensitive(value: Device) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_device_id" in value:
        out["connector_device_id"] = "*** Sensitive Data Redacted ***"
    return out
