"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateCloudConnectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.cloud_connector_description
    import capo_iot_managed_integrations.types.display_name
    import capo_iot_managed_integrations.types.endpoint_config
    import capo_iot_managed_integrations.types.endpoint_type


class CreateCloudConnectorRequest(TypedDict, closed=True):
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
    """<p>The type of endpoint used for the cloud connector, which defines how the connector communicates with external services.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCloudConnectorRequest) -> dict:
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateCloudConnectorRequest:
    out: CreateCloudConnectorRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError(
            "CreateCloudConnectorRequest.endpoint_config required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("EndpointType") is not None:
        import capo_iot_managed_integrations.types.endpoint_type

        out["endpoint_type"] = (
            capo_iot_managed_integrations.types.endpoint_type.deserialize_json(
                data["EndpointType"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
