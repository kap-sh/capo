"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ConnectorItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.cloud_connector_description
    import capo_iot_managed_integrations.types.cloud_connector_id
    import capo_iot_managed_integrations.types.cloud_connector_type
    import capo_iot_managed_integrations.types.display_name
    import capo_iot_managed_integrations.types.endpoint_config
    import capo_iot_managed_integrations.types.endpoint_type


class ConnectorItem(TypedDict, closed=True):
    name: "capo_iot_managed_integrations.types.display_name.DisplayName"
    """<p>The display name of the C2C connector.</p>"""
    endpoint_config: (
        "capo_iot_managed_integrations.types.endpoint_config.EndpointConfig"
    )
    """<p>The configuration details for the cloud connector endpoint, including connection parameters and authentication requirements.</p>"""
    description: NotRequired[
        "capo_iot_managed_integrations.types.cloud_connector_description.CloudConnectorDescription"
    ]
    """<p>A description of the C2C connector.</p>"""
    endpoint_type: NotRequired[
        "capo_iot_managed_integrations.types.endpoint_type.EndpointType"
    ]
    """<p>The type of endpoint used for the C2C connector.</p>"""
    id: NotRequired[
        "capo_iot_managed_integrations.types.cloud_connector_id.CloudConnectorId"
    ]
    """<p>The identifier of the C2C connector.</p>"""
    type: NotRequired[
        "capo_iot_managed_integrations.types.cloud_connector_type.CloudConnectorType"
    ]
    """<p>The type of cloud connector created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorItem) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_iot_managed_integrations.types.endpoint_config

    out["EndpointConfig"] = (
        capo_iot_managed_integrations.types.endpoint_config.serialize_json(
            value["endpoint_config"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "endpoint_type" in value:
        import capo_iot_managed_integrations.types.endpoint_type

        out["EndpointType"] = (
            capo_iot_managed_integrations.types.endpoint_type.serialize_json(
                value["endpoint_type"]
            )
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_iot_managed_integrations.types.cloud_connector_type

        out["Type"] = (
            capo_iot_managed_integrations.types.cloud_connector_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConnectorItem:
    out: ConnectorItem = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("EndpointConfig") is not None:
        import capo_iot_managed_integrations.types.endpoint_config

        out["endpoint_config"] = (
            capo_iot_managed_integrations.types.endpoint_config.deserialize_json(
                data["EndpointConfig"]
            )
        )
    else:
        raise DeserializationError("ConnectorItem.endpoint_config required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EndpointType") is not None:
        import capo_iot_managed_integrations.types.endpoint_type

        out["endpoint_type"] = (
            capo_iot_managed_integrations.types.endpoint_type.deserialize_json(
                data["EndpointType"]
            )
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_iot_managed_integrations.types.cloud_connector_type

        out["type"] = (
            capo_iot_managed_integrations.types.cloud_connector_type.deserialize_json(
                data["Type"]
            )
        )
    return out
