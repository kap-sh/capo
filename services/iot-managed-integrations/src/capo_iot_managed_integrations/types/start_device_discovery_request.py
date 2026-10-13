"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#StartDeviceDiscoveryRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.account_association_id
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.connector_association_id
    import capo_iot_managed_integrations.types.connector_device_id_list
    import capo_iot_managed_integrations.types.custom_protocol_detail
    import capo_iot_managed_integrations.types.discovery_auth_material_string
    import capo_iot_managed_integrations.types.discovery_auth_material_type
    import capo_iot_managed_integrations.types.discovery_type
    import capo_iot_managed_integrations.types.managed_thing_id
    import capo_iot_managed_integrations.types.protocol_type
    import capo_iot_managed_integrations.types.tags_map


class StartDeviceDiscoveryRequest(TypedDict, closed=True):
    discovery_type: "capo_iot_managed_integrations.types.discovery_type.DiscoveryType"
    """<p>The discovery type supporting the type of device to be discovered in the device discovery task request.</p>"""
    custom_protocol_detail: NotRequired[
        "capo_iot_managed_integrations.types.custom_protocol_detail.CustomProtocolDetail"
    ]
    """<p>Additional protocol-specific details required for device discovery, which vary based on the discovery type.</p> <note> <p>For a <code>DiscoveryType</code> of <code>CUSTOM</code>, the string-to-string map must have a key value of <code>Name</code> set to a non-empty-string.</p> </note>"""
    controller_identifier: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The id of the end-user's IoT hub.</p>"""
    connector_association_identifier: NotRequired[
        "capo_iot_managed_integrations.types.connector_association_id.ConnectorAssociationId"
    ]
    """<p>The id of the connector association.</p>"""
    account_association_id: NotRequired[
        "capo_iot_managed_integrations.types.account_association_id.AccountAssociationId"
    ]
    """<p>The identifier of the cloud-to-cloud account association to use for discovery of third-party devices.</p>"""
    authentication_material: NotRequired[
        "capo_iot_managed_integrations.types.discovery_auth_material_string.DiscoveryAuthMaterialString"
    ]
    """<p>The authentication material required to start the local device discovery job request.</p>"""
    authentication_material_type: NotRequired[
        "capo_iot_managed_integrations.types.discovery_auth_material_type.DiscoveryAuthMaterialType"
    ]
    """<p>The type of authentication material used for device discovery jobs.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the device discovery request.</p>"""
    connector_device_id_list: NotRequired[
        "capo_iot_managed_integrations.types.connector_device_id_list.ConnectorDeviceIdList"
    ]
    """<p>Used as a filter for PLA discoveries.</p>"""
    protocol: NotRequired[
        "capo_iot_managed_integrations.types.protocol_type.ProtocolType"
    ]
    """<p>The protocol type for capability rediscovery (ZWAVE, ZIGBEE, or CUSTOM).</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>"""
    end_device_identifier: NotRequired[
        "capo_iot_managed_integrations.types.managed_thing_id.ManagedThingId"
    ]
    """<p>The unique id of the end device for capability rediscovery.</p> <note> <p>This parameter is only available when the discovery type is CONTROLLER_CAPABILITY_REDISCOVERY.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartDeviceDiscoveryRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.discovery_type

    out["DiscoveryType"] = (
        capo_iot_managed_integrations.types.discovery_type.serialize_json(
            value["discovery_type"]
        )
    )
    if "custom_protocol_detail" in value:
        import capo_iot_managed_integrations.types.custom_protocol_detail

        out["CustomProtocolDetail"] = (
            capo_iot_managed_integrations.types.custom_protocol_detail.serialize_json(
                value["custom_protocol_detail"]
            )
        )
    if "controller_identifier" in value:
        out["ControllerIdentifier"] = value["controller_identifier"]
    if "connector_association_identifier" in value:
        out["ConnectorAssociationIdentifier"] = value[
            "connector_association_identifier"
        ]
    if "account_association_id" in value:
        out["AccountAssociationId"] = value["account_association_id"]
    if "authentication_material" in value:
        out["AuthenticationMaterial"] = value["authentication_material"]
    if "authentication_material_type" in value:
        import capo_iot_managed_integrations.types.discovery_auth_material_type

        out["AuthenticationMaterialType"] = (
            capo_iot_managed_integrations.types.discovery_auth_material_type.serialize_json(
                value["authentication_material_type"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    if "connector_device_id_list" in value:
        import capo_iot_managed_integrations.types.connector_device_id_list

        out["ConnectorDeviceIdList"] = (
            capo_iot_managed_integrations.types.connector_device_id_list.serialize_json(
                value["connector_device_id_list"]
            )
        )
    if "protocol" in value:
        import capo_iot_managed_integrations.types.protocol_type

        out["Protocol"] = (
            capo_iot_managed_integrations.types.protocol_type.serialize_json(
                value["protocol"]
            )
        )
    if "end_device_identifier" in value:
        out["EndDeviceIdentifier"] = value["end_device_identifier"]
    return out


def deserialize_json(data: dict) -> StartDeviceDiscoveryRequest:
    out: StartDeviceDiscoveryRequest = {}  # type: ignore[typeddict-item]
    if data.get("DiscoveryType") is not None:
        import capo_iot_managed_integrations.types.discovery_type

        out["discovery_type"] = (
            capo_iot_managed_integrations.types.discovery_type.deserialize_json(
                data["DiscoveryType"]
            )
        )
    else:
        raise DeserializationError(
            "StartDeviceDiscoveryRequest.discovery_type required"
        )
    if data.get("CustomProtocolDetail") is not None:
        import capo_iot_managed_integrations.types.custom_protocol_detail

        out["custom_protocol_detail"] = (
            capo_iot_managed_integrations.types.custom_protocol_detail.deserialize_json(
                data["CustomProtocolDetail"]
            )
        )
    if data.get("ControllerIdentifier") is not None:
        out["controller_identifier"] = data["ControllerIdentifier"]
    if data.get("ConnectorAssociationIdentifier") is not None:
        out["connector_association_identifier"] = data["ConnectorAssociationIdentifier"]
    if data.get("AccountAssociationId") is not None:
        out["account_association_id"] = data["AccountAssociationId"]
    if data.get("AuthenticationMaterial") is not None:
        out["authentication_material"] = data["AuthenticationMaterial"]
    if data.get("AuthenticationMaterialType") is not None:
        import capo_iot_managed_integrations.types.discovery_auth_material_type

        out["authentication_material_type"] = (
            capo_iot_managed_integrations.types.discovery_auth_material_type.deserialize_json(
                data["AuthenticationMaterialType"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    if data.get("ConnectorDeviceIdList") is not None:
        import capo_iot_managed_integrations.types.connector_device_id_list

        out["connector_device_id_list"] = (
            capo_iot_managed_integrations.types.connector_device_id_list.deserialize_json(
                data["ConnectorDeviceIdList"]
            )
        )
    if data.get("Protocol") is not None:
        import capo_iot_managed_integrations.types.protocol_type

        out["protocol"] = (
            capo_iot_managed_integrations.types.protocol_type.deserialize_json(
                data["Protocol"]
            )
        )
    if data.get("EndDeviceIdentifier") is not None:
        out["end_device_identifier"] = data["EndDeviceIdentifier"]
    return out


def redact_sensitive(value: StartDeviceDiscoveryRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_material" in value:
        out["authentication_material"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    if "connector_device_id_list" in value:
        import capo_iot_managed_integrations.types.connector_device_id_list

        out["connector_device_id_list"] = (
            capo_iot_managed_integrations.types.connector_device_id_list.redact_sensitive(
                value["connector_device_id_list"]
            )
        )
    return out
