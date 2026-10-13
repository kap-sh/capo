"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserEndpointSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.allow_messages
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_type
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.endpoint_state
    import capo_chime_sdk_identity.types.sensitive_string1600
    import capo_chime_sdk_identity.types.string64


class AppInstanceUserEndpointSummary(TypedDict, closed=True):
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
    allow_messages: NotRequired[
        "capo_chime_sdk_identity.types.allow_messages.AllowMessages"
    ]
    """<p>BBoolean that controls whether the <code>AppInstanceUserEndpoint</code> is opted in to receive messages. <code>ALL</code> indicates the endpoint will receive all messages. <code>NONE</code> indicates the endpoint will receive no messages.</p>"""
    endpoint_state: NotRequired[
        "capo_chime_sdk_identity.types.endpoint_state.EndpointState"
    ]
    """<p>A read-only field that represent the state of an <code>AppInstanceUserEndpoint</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserEndpointSummary) -> dict:
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


def deserialize_json(data: dict) -> AppInstanceUserEndpointSummary:
    out: AppInstanceUserEndpointSummary = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: AppInstanceUserEndpointSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
