"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveredDeviceSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.auth_material_string
    import capo_iot_managed_integrations.types.brand
    import capo_iot_managed_integrations.types.connector_device_id
    import capo_iot_managed_integrations.types.connector_device_name
    import capo_iot_managed_integrations.types.device_type_list
    import capo_iot_managed_integrations.types.discovered_at
    import capo_iot_managed_integrations.types.discovery_modification
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.model


class DiscoveredDeviceSummary(TypedDict, closed=True):
    connector_device_id: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_id.ConnectorDeviceId"
    ]
    """<p>The third-party device identifier as defined by the connector. This identifier must not contain personal identifiable information (PII).</p>"""
    connector_device_name: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_name.ConnectorDeviceName"
    ]
    """<p>The name of the device as defined by the connector or third-party system.</p>"""
    device_types: NotRequired[
        "capo_iot_managed_integrations.types.device_type_list.DeviceTypeList"
    ]
    """<p>The list of device types or categories that the discovered device belongs to.</p>"""
    managed_thing_id: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The identifier of the managed thing created for this discovered device, if one exists.</p>"""
    modification: NotRequired[
        "capo_iot_managed_integrations.types.discovery_modification.DiscoveryModification"
    ]
    """<p>The status of the discovered device, indicating whether it has been added, removed, or modified since the last discovery.</p>"""
    discovered_at: NotRequired[
        "capo_iot_managed_integrations.types.discovered_at.DiscoveredAt"
    ]
    """<p>The timestamp indicating when the device was discovered.</p>"""
    brand: NotRequired["capo_iot_managed_integrations.types.brand.Brand"]
    """<p>The brand of the discovered device.</p>"""
    model: NotRequired["capo_iot_managed_integrations.types.model.Model"]
    """<p>The model of the discovered device.</p>"""
    authentication_material: NotRequired[
        "capo_iot_managed_integrations.types.auth_material_string.AuthMaterialString"
    ]
    """<p>The authentication material required for connecting to the discovered device, such as credentials or tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveredDeviceSummary) -> dict:
    out: dict = {}
    if "connector_device_id" in value:
        out["ConnectorDeviceId"] = value["connector_device_id"]
    if "connector_device_name" in value:
        out["ConnectorDeviceName"] = value["connector_device_name"]
    if "device_types" in value:
        import capo_iot_managed_integrations.types.device_type_list

        out["DeviceTypes"] = (
            capo_iot_managed_integrations.types.device_type_list.serialize_json(
                value["device_types"]
            )
        )
    if "managed_thing_id" in value:
        out["ManagedThingId"] = value["managed_thing_id"]
    if "modification" in value:
        import capo_iot_managed_integrations.types.discovery_modification

        out["Modification"] = (
            capo_iot_managed_integrations.types.discovery_modification.serialize_json(
                value["modification"]
            )
        )
    if "discovered_at" in value:
        import capo_iot_managed_integrations.types.discovered_at

        out["DiscoveredAt"] = (
            capo_iot_managed_integrations.types.discovered_at.serialize_json(
                value["discovered_at"]
            )
        )
    if "brand" in value:
        out["Brand"] = value["brand"]
    if "model" in value:
        out["Model"] = value["model"]
    if "authentication_material" in value:
        out["AuthenticationMaterial"] = value["authentication_material"]
    return out


def deserialize_json(data: dict) -> DiscoveredDeviceSummary:
    out: DiscoveredDeviceSummary = {}  # type: ignore[typeddict-item]
    if data.get("ConnectorDeviceId") is not None:
        out["connector_device_id"] = data["ConnectorDeviceId"]
    if data.get("ConnectorDeviceName") is not None:
        out["connector_device_name"] = data["ConnectorDeviceName"]
    if data.get("DeviceTypes") is not None:
        import capo_iot_managed_integrations.types.device_type_list

        out["device_types"] = (
            capo_iot_managed_integrations.types.device_type_list.deserialize_json(
                data["DeviceTypes"]
            )
        )
    if data.get("ManagedThingId") is not None:
        out["managed_thing_id"] = data["ManagedThingId"]
    if data.get("Modification") is not None:
        import capo_iot_managed_integrations.types.discovery_modification

        out["modification"] = (
            capo_iot_managed_integrations.types.discovery_modification.deserialize_json(
                data["Modification"]
            )
        )
    if data.get("DiscoveredAt") is not None:
        import capo_iot_managed_integrations.types.discovered_at

        out["discovered_at"] = (
            capo_iot_managed_integrations.types.discovered_at.deserialize_json(
                data["DiscoveredAt"]
            )
        )
    if data.get("Brand") is not None:
        out["brand"] = data["Brand"]
    if data.get("Model") is not None:
        out["model"] = data["Model"]
    if data.get("AuthenticationMaterial") is not None:
        out["authentication_material"] = data["AuthenticationMaterial"]
    return out


def redact_sensitive(value: DiscoveredDeviceSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connector_device_id" in value:
        out["connector_device_id"] = "*** Sensitive Data Redacted ***"
    if "brand" in value:
        out["brand"] = "*** Sensitive Data Redacted ***"
    if "model" in value:
        out["model"] = "*** Sensitive Data Redacted ***"
    if "authentication_material" in value:
        out["authentication_material"] = "*** Sensitive Data Redacted ***"
    return out
