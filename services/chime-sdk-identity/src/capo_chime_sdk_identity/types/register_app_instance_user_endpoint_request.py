"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#RegisterAppInstanceUserEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.allow_messages
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_type
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.client_request_token
    import capo_chime_sdk_identity.types.endpoint_attributes
    import capo_chime_sdk_identity.types.sensitive_chime_arn
    import capo_chime_sdk_identity.types.sensitive_string1600


class RegisterAppInstanceUserEndpointRequest(TypedDict, closed=True):
    app_instance_user_arn: (
        "capo_chime_sdk_identity.types.sensitive_chime_arn.SensitiveChimeArn"
    )
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    name: NotRequired[
        "capo_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
    ]
    """<p>The name of the <code>AppInstanceUserEndpoint</code>.</p>"""
    type: "capo_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType"
    """<p>The type of the <code>AppInstanceUserEndpoint</code>. Supported types:</p> <ul> <li> <p> <code>APNS</code>: The mobile notification service for an Apple device.</p> </li> <li> <p> <code>APNS_SANDBOX</code>: The sandbox environment of the mobile notification service for an Apple device.</p> </li> <li> <p> <code>GCM</code>: The mobile notification service for an Android device.</p> </li> </ul> <p>Populate the <code>ResourceArn</code> value of each type as <code>PinpointAppArn</code>.</p>"""
    resource_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the resource to which the endpoint belongs.</p>"""
    endpoint_attributes: (
        "capo_chime_sdk_identity.types.endpoint_attributes.EndpointAttributes"
    )
    """<p>The attributes of an <code>Endpoint</code>.</p>"""
    client_request_token: (
        "capo_chime_sdk_identity.types.client_request_token.ClientRequestToken"
    )
    """<p>The unique ID assigned to the request. Use different tokens to register other endpoints.</p>"""
    allow_messages: NotRequired[
        "capo_chime_sdk_identity.types.allow_messages.AllowMessages"
    ]
    """<p>Boolean that controls whether the AppInstanceUserEndpoint is opted in to receive messages. <code>ALL</code> indicates the endpoint receives all messages. <code>NONE</code> indicates the endpoint receives no messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterAppInstanceUserEndpointRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import capo_chime_sdk_identity.types.app_instance_user_endpoint_type

    out["Type"] = (
        capo_chime_sdk_identity.types.app_instance_user_endpoint_type.serialize_json(
            value["type"]
        )
    )
    out["ResourceArn"] = value["resource_arn"]
    import capo_chime_sdk_identity.types.endpoint_attributes

    out["EndpointAttributes"] = (
        capo_chime_sdk_identity.types.endpoint_attributes.serialize_json(
            value["endpoint_attributes"]
        )
    )
    out["ClientRequestToken"] = value["client_request_token"]
    if "allow_messages" in value:
        import capo_chime_sdk_identity.types.allow_messages

        out["AllowMessages"] = (
            capo_chime_sdk_identity.types.allow_messages.serialize_json(
                value["allow_messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegisterAppInstanceUserEndpointRequest:
    out: RegisterAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_chime_sdk_identity.types.app_instance_user_endpoint_type

        out["type"] = (
            capo_chime_sdk_identity.types.app_instance_user_endpoint_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_chime_sdk_identity.types.app_instance_user_endpoint_type.AppInstanceUserEndpointType",
            "",
        )
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("EndpointAttributes") is not None:
        import capo_chime_sdk_identity.types.endpoint_attributes

        out["endpoint_attributes"] = (
            capo_chime_sdk_identity.types.endpoint_attributes.deserialize_json(
                data["EndpointAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "RegisterAppInstanceUserEndpointRequest.endpoint_attributes required"
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        out["client_request_token"] = ""
    if data.get("AllowMessages") is not None:
        import capo_chime_sdk_identity.types.allow_messages

        out["allow_messages"] = (
            capo_chime_sdk_identity.types.allow_messages.deserialize_json(
                data["AllowMessages"]
            )
        )
    return out


def redact_sensitive(value: RegisterAppInstanceUserEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "app_instance_user_arn" in value:
        out["app_instance_user_arn"] = "*** Sensitive Data Redacted ***"
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
