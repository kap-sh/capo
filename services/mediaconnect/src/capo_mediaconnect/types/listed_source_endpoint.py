"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListedSourceEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.endpoint_encryption_type
    import capo_mediaconnect.types.endpoint_lifecycle
    import capo_mediaconnect.types.resource_share_ownership
    import capo_mediaconnect.types.resource_share_state
    import capo_mediaconnect.types.source_endpoint_arn
    import capo_mediaconnect.types.source_endpoint_connection_state
    import capo_mediaconnect.types.source_endpoint_registration_state
    import capo_mediaconnect.types.source_endpoint_type


class ListedSourceEndpoint(TypedDict, closed=True):
    name: "str"
    """<p>The name of the source endpoint.</p>"""
    arn: "capo_mediaconnect.types.source_endpoint_arn.SourceEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the source endpoint.</p>"""
    id: "str"
    """<p>The unique identifier of the source endpoint.</p>"""
    source_type: "capo_mediaconnect.types.source_endpoint_type.SourceEndpointType"
    """<p>The type of the source endpoint. Valid values include the following:</p> <ul> <li> <p> <code>STANDARD</code> – A source endpoint that represents an external source over a standard protocol, such as RTP, RIST, or SRT.</p> </li> <li> <p> <code>ROUTER_OUTPUT</code> – A source endpoint that represents a router output.</p> </li> </ul>"""
    region_name: "str"
    """<p>The name of the Amazon Web Services Region in which the source endpoint is located.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Availability Zone in which the source endpoint is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The ID of the Availability Zone in which the source endpoint is located.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the source endpoint was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the source endpoint was last updated.</p>"""
    lifecycle_management: "capo_mediaconnect.types.endpoint_lifecycle.EndpointLifecycle"
    """<p>The entity that manages the lifecycle of the source endpoint.</p>"""
    message_count: "int"
    """<p>The number of status messages for the source endpoint.</p>"""
    resource_share_ownership: (
        "capo_mediaconnect.types.resource_share_ownership.ResourceShareOwnership"
    )
    """<p>Indicates whether this account owns the source endpoint or consumes it from another account through RAM.</p>"""
    resource_share_state: (
        "capo_mediaconnect.types.resource_share_state.ResourceShareState"
    )
    """<p>The sharing state of the source endpoint.</p>"""
    registration_state: "capo_mediaconnect.types.source_endpoint_registration_state.SourceEndpointRegistrationState"
    """<p>The registration state of the source endpoint. Valid values include the following:</p> <ul> <li> <p> <code>REGISTERED</code> – The source endpoint is registered and ready to use.</p> </li> <li> <p> <code>REGISTERING</code> – MediaConnect is registering the source endpoint.</p> </li> <li> <p> <code>DEREGISTERING</code> – MediaConnect is deregistering the source endpoint.</p> </li> <li> <p> <code>REGISTRATION_FAILED</code> – MediaConnect couldn't register the source endpoint.</p> </li> </ul>"""
    connection_state: "capo_mediaconnect.types.source_endpoint_connection_state.SourceEndpointConnectionState"
    """<p>The connection state of the source endpoint. Valid values include the following:</p> <ul> <li> <p> <code>CONNECTED</code> – The source endpoint is connected to a destination endpoint.</p> </li> <li> <p> <code>DISCONNECTED</code> – The source endpoint isn't connected to a destination endpoint.</p> </li> <li> <p> <code>CONNECTING</code> – The source endpoint is connecting to a destination endpoint.</p> </li> <li> <p> <code>DISCONNECTING</code> – The source endpoint is disconnecting from a destination endpoint.</p> </li> </ul>"""
    encryption_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_type.EndpointEncryptionType"
    ]
    """<p>The type of encryption used for the source endpoint connection.</p>"""
    connected_destination_count: "int"
    """<p>The number of destination endpoints that are connected to the source endpoint.</p>"""
    associated_resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the resource that is associated with the source endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListedSourceEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_mediaconnect.types.source_endpoint_type

    out["sourceType"] = capo_mediaconnect.types.source_endpoint_type.serialize_json(
        value["source_type"]
    )
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
    out["messageCount"] = value["message_count"]
    import capo_mediaconnect.types.resource_share_ownership

    out["resourceShareOwnership"] = (
        capo_mediaconnect.types.resource_share_ownership.serialize_json(
            value["resource_share_ownership"]
        )
    )
    import capo_mediaconnect.types.resource_share_state

    out["resourceShareState"] = (
        capo_mediaconnect.types.resource_share_state.serialize_json(
            value["resource_share_state"]
        )
    )
    import capo_mediaconnect.types.source_endpoint_registration_state

    out["registrationState"] = (
        capo_mediaconnect.types.source_endpoint_registration_state.serialize_json(
            value["registration_state"]
        )
    )
    import capo_mediaconnect.types.source_endpoint_connection_state

    out["connectionState"] = (
        capo_mediaconnect.types.source_endpoint_connection_state.serialize_json(
            value["connection_state"]
        )
    )
    if "encryption_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["encryptionType"] = (
            capo_mediaconnect.types.endpoint_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    out["connectedDestinationCount"] = value["connected_destination_count"]
    if "associated_resource_arn" in value:
        out["associatedResourceArn"] = value["associated_resource_arn"]
    return out


def deserialize_json(data: dict) -> ListedSourceEndpoint:
    out: ListedSourceEndpoint = {}  # type: ignore[typeddict-item]
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
    if data.get("sourceType") is not None:
        import capo_mediaconnect.types.source_endpoint_type

        out["source_type"] = (
            capo_mediaconnect.types.source_endpoint_type.deserialize_json(
                data["sourceType"]
            )
        )
    else:
        import typing

        out["source_type"] = typing.cast(
            "capo_mediaconnect.types.source_endpoint_type.SourceEndpointType", ""
        )
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
    if data.get("messageCount") is not None:
        out["message_count"] = data["messageCount"]
    else:
        out["message_count"] = 0
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
    if data.get("resourceShareState") is not None:
        import capo_mediaconnect.types.resource_share_state

        out["resource_share_state"] = (
            capo_mediaconnect.types.resource_share_state.deserialize_json(
                data["resourceShareState"]
            )
        )
    else:
        import typing

        out["resource_share_state"] = typing.cast(
            "capo_mediaconnect.types.resource_share_state.ResourceShareState", ""
        )
    if data.get("registrationState") is not None:
        import capo_mediaconnect.types.source_endpoint_registration_state

        out["registration_state"] = (
            capo_mediaconnect.types.source_endpoint_registration_state.deserialize_json(
                data["registrationState"]
            )
        )
    else:
        import typing

        out["registration_state"] = typing.cast(
            "capo_mediaconnect.types.source_endpoint_registration_state.SourceEndpointRegistrationState",
            "",
        )
    if data.get("connectionState") is not None:
        import capo_mediaconnect.types.source_endpoint_connection_state

        out["connection_state"] = (
            capo_mediaconnect.types.source_endpoint_connection_state.deserialize_json(
                data["connectionState"]
            )
        )
    else:
        import typing

        out["connection_state"] = typing.cast(
            "capo_mediaconnect.types.source_endpoint_connection_state.SourceEndpointConnectionState",
            "",
        )
    if data.get("encryptionType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_type

        out["encryption_type"] = (
            capo_mediaconnect.types.endpoint_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if data.get("connectedDestinationCount") is not None:
        out["connected_destination_count"] = data["connectedDestinationCount"]
    else:
        out["connected_destination_count"] = 0
    if data.get("associatedResourceArn") is not None:
        out["associated_resource_arn"] = data["associatedResourceArn"]
    return out
