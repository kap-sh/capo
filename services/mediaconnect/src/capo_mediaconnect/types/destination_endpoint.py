"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DestinationEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.destination_endpoint_arn
    import capo_mediaconnect.types.destination_endpoint_associated_resource_details
    import capo_mediaconnect.types.destination_endpoint_configuration
    import capo_mediaconnect.types.destination_endpoint_connection_details
    import capo_mediaconnect.types.destination_endpoint_connection_state
    import capo_mediaconnect.types.destination_endpoint_message_list
    import capo_mediaconnect.types.destination_endpoint_registration_state
    import capo_mediaconnect.types.destination_endpoint_type
    import capo_mediaconnect.types.endpoint_encryption_configuration
    import capo_mediaconnect.types.endpoint_encryption_type
    import capo_mediaconnect.types.endpoint_lifecycle
    import capo_mediaconnect.types.resource_share_details
    import capo_mediaconnect.types.resource_share_ownership
    import capo_mediaconnect.types.source_endpoint_arn


class DestinationEndpoint(TypedDict, closed=True):
    name: "str"
    """<p>The name of the destination endpoint.</p>"""
    arn: "capo_mediaconnect.types.destination_endpoint_arn.DestinationEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the destination endpoint.</p>"""
    id: "str"
    """<p>The unique identifier of the destination endpoint.</p>"""
    description: "str"
    """<p>The description of the destination endpoint.</p>"""
    region_name: "str"
    """<p>The name of the Amazon Web Services Region in which the destination endpoint is located.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone in which the destination endpoint is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The ID of the Availability Zone in which the destination endpoint is located.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the destination endpoint was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the destination endpoint was last updated.</p>"""
    lifecycle_management: "capo_mediaconnect.types.endpoint_lifecycle.EndpointLifecycle"
    """<p>The entity that manages the lifecycle of the destination endpoint.</p>"""
    messages: "capo_mediaconnect.types.destination_endpoint_message_list.DestinationEndpointMessageList"
    """<p>The status messages for the destination endpoint.</p>"""
    destination_type: (
        "capo_mediaconnect.types.destination_endpoint_type.DestinationEndpointType"
    )
    """<p>The type of the destination endpoint. Valid values include the following:</p> <ul> <li> <p> <code>STANDARD</code> – A destination endpoint that represents an external destination over a standard protocol, such as RTP, RIST, or SRT.</p> </li> <li> <p> <code>ROUTER_INPUT</code> – A destination endpoint that represents a router input.</p> </li> </ul>"""
    configuration: "capo_mediaconnect.types.destination_endpoint_configuration.DestinationEndpointConfiguration"
    """<p>The configuration settings for the destination endpoint.</p>"""
    resource_share_ownership: (
        "capo_mediaconnect.types.resource_share_ownership.ResourceShareOwnership"
    )
    """<p>Indicates whether this account owns the destination endpoint or consumes it from another account through RAM.</p>"""
    resource_share_details: (
        "capo_mediaconnect.types.resource_share_details.ResourceShareDetails"
    )
    registration_state: "capo_mediaconnect.types.destination_endpoint_registration_state.DestinationEndpointRegistrationState"
    """<p>The registration state of the destination endpoint. Valid values include the following:</p> <ul> <li> <p> <code>REGISTERED</code> – The destination endpoint is registered and ready to use.</p> </li> <li> <p> <code>REGISTERING</code> – MediaConnect is registering the destination endpoint.</p> </li> <li> <p> <code>DEREGISTERING</code> – MediaConnect is deregistering the destination endpoint.</p> </li> <li> <p> <code>REGISTRATION_FAILED</code> – MediaConnect couldn't register the destination endpoint.</p> </li> </ul>"""
    connection_details: NotRequired[
        "capo_mediaconnect.types.destination_endpoint_connection_details.DestinationEndpointConnectionDetails"
    ]
    """<p>The connection details for the destination endpoint.</p>"""
    connection_state: "capo_mediaconnect.types.destination_endpoint_connection_state.DestinationEndpointConnectionState"
    """<p>The connection state of the destination endpoint. Valid values include the following:</p> <ul> <li> <p> <code>CONNECTED</code> – The destination endpoint is connected to a source endpoint.</p> </li> <li> <p> <code>DISCONNECTED</code> – The destination endpoint isn't connected to a source endpoint.</p> </li> <li> <p> <code>CONNECTING</code> – The destination endpoint is connecting to a source endpoint.</p> </li> <li> <p> <code>DISCONNECTING</code> – The destination endpoint is disconnecting from a source endpoint.</p> </li> </ul>"""
    connected_source: NotRequired[
        "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source endpoint that is connected to the destination endpoint.</p>"""
    decryption_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_type.EndpointEncryptionType"
    ]
    """<p>The type of decryption used for the destination endpoint connection.</p>"""
    decryption_configuration: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_configuration.EndpointEncryptionConfiguration"
    ]
    associated_resource_details: "capo_mediaconnect.types.destination_endpoint_associated_resource_details.DestinationEndpointAssociatedResourceDetails"
    """<p>The details of the resource that is associated with the destination endpoint.</p>"""
    tags: "capo_mediaconnect.types.__map_of_string.__mapOfString"
    """<p>The tags associated with the destination endpoint. Each tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["description"] = value["description"]
    out["regionName"] = value["region_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    import capo_mediaconnect._protocol.serialize

    out["createdAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_mediaconnect._protocol.serialize

    out["updatedAt"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    import capo_mediaconnect.types.endpoint_lifecycle

    out["lifecycleManagement"] = (
        capo_mediaconnect.types.endpoint_lifecycle.serialize_json(
            value["lifecycle_management"]
        )
    )
    import capo_mediaconnect.types.destination_endpoint_message_list

    out["messages"] = (
        capo_mediaconnect.types.destination_endpoint_message_list.serialize_json(
            value["messages"]
        )
    )
    import capo_mediaconnect.types.destination_endpoint_type

    out["destinationType"] = (
        capo_mediaconnect.types.destination_endpoint_type.serialize_json(
            value["destination_type"]
        )
    )
    import capo_mediaconnect.types.destination_endpoint_configuration

    out["configuration"] = (
        capo_mediaconnect.types.destination_endpoint_configuration.serialize_json(
            value["configuration"]
        )
    )
    import capo_mediaconnect.types.resource_share_ownership

    out["resourceShareOwnership"] = (
        capo_mediaconnect.types.resource_share_ownership.serialize_json(
            value["resource_share_ownership"]
        )
    )
    import capo_mediaconnect.types.resource_share_details

    out["resourceShareDetails"] = (
        capo_mediaconnect.types.resource_share_details.serialize_json(
            value["resource_share_details"]
        )
    )
    import capo_mediaconnect.types.destination_endpoint_registration_state

    out["registrationState"] = (
        capo_mediaconnect.types.destination_endpoint_registration_state.serialize_json(
            value["registration_state"]
        )
    )
    if "connection_details" in value:
        import capo_mediaconnect.types.destination_endpoint_connection_details

        out["connectionDetails"] = (
            capo_mediaconnect.types.destination_endpoint_connection_details.serialize_json(
                value["connection_details"]
            )
        )
    import capo_mediaconnect.types.destination_endpoint_connection_state

    out["connectionState"] = (
        capo_mediaconnect.types.destination_endpoint_connection_state.serialize_json(
            value["connection_state"]
        )
    )
    if "connected_source" in value:
        out["connectedSource"] = value["connected_source"]
    if "decryption_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["decryptionType"] = (
            capo_mediaconnect.types.endpoint_encryption_type.serialize_json(
                value["decryption_type"]
            )
        )
    if "decryption_configuration" in value:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["decryptionConfiguration"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.serialize_json(
                value["decryption_configuration"]
            )
        )
    import capo_mediaconnect.types.destination_endpoint_associated_resource_details

    out["associatedResourceDetails"] = (
        capo_mediaconnect.types.destination_endpoint_associated_resource_details.serialize_json(
            value["associated_resource_details"]
        )
    )
    import capo_mediaconnect.types.__map_of_string

    out["tags"] = capo_mediaconnect.types.__map_of_string.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DestinationEndpoint:
    out: DestinationEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("regionName") is not None:
        out["region_name"] = data["regionName"]
    else:
        out["region_name"] = ""
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lifecycleManagement") is not None:
        import capo_mediaconnect.types.endpoint_lifecycle

        out["lifecycle_management"] = (
            capo_mediaconnect.types.endpoint_lifecycle.deserialize_json(
                data["lifecycleManagement"]
            )
        )
    else:
        import typing

        out["lifecycle_management"] = typing.cast(
            "capo_mediaconnect.types.endpoint_lifecycle.EndpointLifecycle", ""
        )
    if data.get("messages") is not None:
        import capo_mediaconnect.types.destination_endpoint_message_list

        out["messages"] = (
            capo_mediaconnect.types.destination_endpoint_message_list.deserialize_json(
                data["messages"]
            )
        )
    else:
        out["messages"] = []
    if data.get("destinationType") is not None:
        import capo_mediaconnect.types.destination_endpoint_type

        out["destination_type"] = (
            capo_mediaconnect.types.destination_endpoint_type.deserialize_json(
                data["destinationType"]
            )
        )
    else:
        import typing

        out["destination_type"] = typing.cast(
            "capo_mediaconnect.types.destination_endpoint_type.DestinationEndpointType",
            "",
        )
    if data.get("configuration") is not None:
        import capo_mediaconnect.types.destination_endpoint_configuration

        out["configuration"] = (
            capo_mediaconnect.types.destination_endpoint_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        out["configuration"] = {"$unknown": {"name": ""}}
    if data.get("resourceShareOwnership") is not None:
        import capo_mediaconnect.types.resource_share_ownership

        out["resource_share_ownership"] = (
            capo_mediaconnect.types.resource_share_ownership.deserialize_json(
                data["resourceShareOwnership"]
            )
        )
    else:
        import typing

        out["resource_share_ownership"] = typing.cast(
            "capo_mediaconnect.types.resource_share_ownership.ResourceShareOwnership",
            "",
        )
    if data.get("resourceShareDetails") is not None:
        import capo_mediaconnect.types.resource_share_details

        out["resource_share_details"] = (
            capo_mediaconnect.types.resource_share_details.deserialize_json(
                data["resourceShareDetails"]
            )
        )
    else:
        out["resource_share_details"] = {"$unknown": {"name": ""}}
    if data.get("registrationState") is not None:
        import capo_mediaconnect.types.destination_endpoint_registration_state

        out["registration_state"] = (
            capo_mediaconnect.types.destination_endpoint_registration_state.deserialize_json(
                data["registrationState"]
            )
        )
    else:
        import typing

        out["registration_state"] = typing.cast(
            "capo_mediaconnect.types.destination_endpoint_registration_state.DestinationEndpointRegistrationState",
            "",
        )
    if data.get("connectionDetails") is not None:
        import capo_mediaconnect.types.destination_endpoint_connection_details

        out["connection_details"] = (
            capo_mediaconnect.types.destination_endpoint_connection_details.deserialize_json(
                data["connectionDetails"]
            )
        )
    if data.get("connectionState") is not None:
        import capo_mediaconnect.types.destination_endpoint_connection_state

        out["connection_state"] = (
            capo_mediaconnect.types.destination_endpoint_connection_state.deserialize_json(
                data["connectionState"]
            )
        )
    else:
        import typing

        out["connection_state"] = typing.cast(
            "capo_mediaconnect.types.destination_endpoint_connection_state.DestinationEndpointConnectionState",
            "",
        )
    if data.get("connectedSource") is not None:
        out["connected_source"] = data["connectedSource"]
    if data.get("decryptionType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["decryption_type"] = (
            capo_mediaconnect.types.endpoint_encryption_type.deserialize_json(
                data["decryptionType"]
            )
        )
    if data.get("decryptionConfiguration") is not None:
        import capo_mediaconnect.types.endpoint_encryption_configuration

        out["decryption_configuration"] = (
            capo_mediaconnect.types.endpoint_encryption_configuration.deserialize_json(
                data["decryptionConfiguration"]
            )
        )
    if data.get("associatedResourceDetails") is not None:
        import capo_mediaconnect.types.destination_endpoint_associated_resource_details

        out["associated_resource_details"] = (
            capo_mediaconnect.types.destination_endpoint_associated_resource_details.deserialize_json(
                data["associatedResourceDetails"]
            )
        )
    else:
        out["associated_resource_details"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_mediaconnect.types.__map_of_string

        out["tags"] = capo_mediaconnect.types.__map_of_string.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out
