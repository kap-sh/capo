"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#UpdateAppInstanceUserEndpointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.allow_messages
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.sensitive_string1600
    import capo_chime_sdk_identity.types.string64


class UpdateAppInstanceUserEndpointRequest(TypedDict, closed=True):
    app_instance_user_arn: "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    endpoint_id: "capo_chime_sdk_identity.types.string64.String64"
    """<p>The unique identifier of the <code>AppInstanceUserEndpoint</code>.</p>"""
    name: NotRequired[
        "capo_chime_sdk_identity.types.sensitive_string1600.SensitiveString1600"
    ]
    """<p>The name of the <code>AppInstanceUserEndpoint</code>.</p>"""
    allow_messages: NotRequired[
        "capo_chime_sdk_identity.types.allow_messages.AllowMessages"
    ]
    """<p>Boolean that controls whether the <code>AppInstanceUserEndpoint</code> is opted in to receive messages. <code>ALL</code> indicates the endpoint will receive all messages. <code>NONE</code> indicates the endpoint will receive no messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppInstanceUserEndpointRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "allow_messages" in value:
        import capo_chime_sdk_identity.types.allow_messages

        out["AllowMessages"] = (
            capo_chime_sdk_identity.types.allow_messages.serialize_json(
                value["allow_messages"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAppInstanceUserEndpointRequest:
    out: UpdateAppInstanceUserEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AllowMessages") is not None:
        import capo_chime_sdk_identity.types.allow_messages

        out["allow_messages"] = (
            capo_chime_sdk_identity.types.allow_messages.deserialize_json(
                data["AllowMessages"]
            )
        )
    return out


def redact_sensitive(value: UpdateAppInstanceUserEndpointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
