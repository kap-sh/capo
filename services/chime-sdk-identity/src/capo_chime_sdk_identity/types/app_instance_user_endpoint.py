"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.allow_messages
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_type
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.endpoint_attributes
    import capo_chime_sdk_identity.types.endpoint_state
    import capo_chime_sdk_identity.types.sensitive_string1600
    import capo_chime_sdk_identity.types.string64
    import capo_chime_sdk_identity.types.timestamp


class AppInstanceUserEndpoint(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    endpoint_id: NotRequired["capo_chime_sdk_identity.types.string64.String64"]
    """<p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>"""
    name: NotRequired[
        "capo_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
    ]
    """<p>The name of the <code>AppInstanceUserEndpoint</code>.</p>"""
    type: NotRequired[
        "capo_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType"
    ]
    """<p>The type of the <code>AppInstanceUserEndpoint</code>.</p>"""
    resource_arn: NotRequired["capo_chime_sdk_identity.types.chime_arn.ChimeArn"]
    """<p>The ARN of the resource to which the endpoint belongs.</p>"""
    endpoint_attributes: NotRequired[
        "capo_chime_sdk_identity.types.endpoint_attributes.EndpointAttributes"
    ]
    """<p>The attributes of an <code>Endpoint</code>.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_identity.types.timestamp.Timestamp"]
    """<p>The time at which an <code>AppInstanceUserEndpoint</code> was created.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which an <code>AppInstanceUserEndpoint</code> was last updated.</p>"""
    allow_messages: NotRequired[
        "capo_chime_sdk_identity.types.allow_messages.AllowMessages"
    ]
    """<p>Boolean that controls whether the <code>AppInstanceUserEndpoint</code> is opted in to receive messages. <code>ALL</code> indicates the endpoint will receive all messages. <code>NONE</code> indicates the endpoint will receive no messages.</p>"""
    endpoint_state: NotRequired[
        "capo_chime_sdk_identity.types.endpoint_state.EndpointState"
    ]
    """<p>A read-only field that represents the state of an <code>AppInstanceUserEndpoint</code>. Supported values:</p> <ul> <li> <p> <code>ACTIVE</code>: The <code>AppInstanceUserEndpoint</code> is active and able to receive messages. When <code>ACTIVE</code>, the <code>EndpointStatusReason</code> remains empty.</p> </li> <li> <p> <code>INACTIVE</code>: The <code>AppInstanceUserEndpoint</code> is inactive and can't receive message. When <code>INACTIVE</code>, the corresponding reason will be conveyed through <code>EndpointStatusReason</code>.</p> </li> <li> <p> <code>INVALID_DEVICE_TOKEN</code> indicates that an <code>AppInstanceUserEndpoint</code> is <code>INACTIVE</code> due to invalid device token</p> </li> <li> <p> <code>INVALID_PINPOINT_ARN</code> indicates that an <code>AppInstanceUserEndpoint</code> is <code>INACTIVE</code> due to an invalid pinpoint ARN that was input through the <code>ResourceArn</code> field.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserEndpoint) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "endpoint_id" in value:
        out["EndpointId"] = value["endpoint_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint_type

        out["Type"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint_type.serialize_json(
                value["type"]
            )
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "endpoint_attributes" in value:
        import capo_chime_sdk_identity.types.endpoint_attributes

        out["EndpointAttributes"] = (
            capo_chime_sdk_identity.types.endpoint_attributes.serialize_json(
                value["endpoint_attributes"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "allow_messages" in value:
        import capo_chime_sdk_identity.types.allow_messages

        out["AllowMessages"] = (
            capo_chime_sdk_identity.types.allow_messages.serialize_json(
                value["allow_messages"]
            )
        )
    if "endpoint_state" in value:
        import capo_chime_sdk_identity.types.endpoint_state

        out["EndpointState"] = (
            capo_chime_sdk_identity.types.endpoint_state.serialize_json(
                value["endpoint_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> AppInstanceUserEndpoint:
    out: AppInstanceUserEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceUserArn") is not None:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if data.get("EndpointId") is not None:
        out["endpoint_id"] = data["EndpointId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint_type

        out["type"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint_type.deserialize_json(
                data["Type"]
            )
        )
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("EndpointAttributes") is not None:
        import capo_chime_sdk_identity.types.endpoint_attributes

        out["endpoint_attributes"] = (
            capo_chime_sdk_identity.types.endpoint_attributes.deserialize_json(
                data["EndpointAttributes"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_identity.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_chime_sdk_identity.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("AllowMessages") is not None:
        import capo_chime_sdk_identity.types.allow_messages

        out["allow_messages"] = (
            capo_chime_sdk_identity.types.allow_messages.deserialize_json(
                data["AllowMessages"]
            )
        )
    if data.get("EndpointState") is not None:
        import capo_chime_sdk_identity.types.endpoint_state

        out["endpoint_state"] = (
            capo_chime_sdk_identity.types.endpoint_state.deserialize_json(
                data["EndpointState"]
            )
        )
    return out


def redact_sensitive(value: AppInstanceUserEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "endpoint_attributes" in value:
        import capo_chime_sdk_identity.types.endpoint_attributes

        out["endpoint_attributes"] = (
            capo_chime_sdk_identity.types.endpoint_attributes.redact_sensitive(
                value["endpoint_attributes"]
            )
        )
    return out
