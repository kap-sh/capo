"""Generated from Smithy shape ``com.amazonaws.apigateway#MethodSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.boolean
    import capo_api_gateway.types.string


class MethodSnapshot(TypedDict, closed=True):
    authorization_type: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The method's authorization type. Valid values are <code>NONE</code> for open access, <code>AWS_IAM</code> for using Amazon Web Services IAM permissions, <code>CUSTOM</code> for using a custom authorizer, or <code>COGNITO_USER_POOLS</code> for using a Cognito user pool.</p>"""
    api_key_required: "capo_api_gateway.types.boolean.Boolean"
    """<p>Specifies whether the method requires a valid ApiKey.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MethodSnapshot) -> dict:
    out: dict = {}
    if "authorization_type" in value:
        out["authorizationType"] = value["authorization_type"]
    out["apiKeyRequired"] = value.get("api_key_required", False)
    return out


def deserialize_json(data: dict) -> MethodSnapshot:
    out: MethodSnapshot = {}  # type: ignore[typeddict-item]
    if data.get("authorizationType") is not None:
        out["authorization_type"] = data["authorizationType"]
    if data.get("apiKeyRequired") is not None:
        out["api_key_required"] = data["apiKeyRequired"]
    else:
        out["api_key_required"] = False
    return out
