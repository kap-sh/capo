"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StripePrivyTokenRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.stripe_privy_request_body_type
    import capo_bedrock_agentcore.types.stripe_privy_request_host_type
    import capo_bedrock_agentcore.types.stripe_privy_request_path_type


class StripePrivyTokenRequestInput(TypedDict, closed=True):
    request_host: NotRequired[
        "capo_bedrock_agentcore.types.stripe_privy_request_host_type.StripePrivyRequestHostType"
    ]
    """<p>The host for the Privy API request. Defaults to "api.privy.io".</p>"""
    request_path: "capo_bedrock_agentcore.types.stripe_privy_request_path_type.StripePrivyRequestPathType"
    """<p>The path of the Stripe Privy API request.</p>"""
    request_body: "capo_bedrock_agentcore.types.stripe_privy_request_body_type.StripePrivyRequestBodyType"
    """<p>Request body JSON for the Privy API call.</p>"""
    include_authorization_signature: "bool"
    """<p>Set to true to generate privy-authorization-signature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StripePrivyTokenRequestInput) -> dict:
    out: dict = {}
    if "request_host" in value:
        out["requestHost"] = value["request_host"]
    out["requestPath"] = value["request_path"]
    out["requestBody"] = value["request_body"]
    out["includeAuthorizationSignature"] = value.get(
        "include_authorization_signature", False
    )
    return out


def deserialize_json(data: dict) -> StripePrivyTokenRequestInput:
    out: StripePrivyTokenRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("requestHost") is not None:
        out["request_host"] = data["requestHost"]
    if data.get("requestPath") is not None:
        out["request_path"] = data["requestPath"]
    else:
        raise DeserializationError("StripePrivyTokenRequestInput.request_path required")
    if data.get("requestBody") is not None:
        out["request_body"] = data["requestBody"]
    else:
        raise DeserializationError("StripePrivyTokenRequestInput.request_body required")
    if data.get("includeAuthorizationSignature") is not None:
        out["include_authorization_signature"] = data["includeAuthorizationSignature"]
    else:
        out["include_authorization_signature"] = False
    return out
