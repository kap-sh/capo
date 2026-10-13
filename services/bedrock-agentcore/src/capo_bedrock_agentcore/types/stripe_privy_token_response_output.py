"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#StripePrivyTokenResponseOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.stripe_privy_app_id_type
    import capo_bedrock_agentcore.types.stripe_privy_authorization_signature_type
    import capo_bedrock_agentcore.types.stripe_privy_basic_auth_token_type


class StripePrivyTokenResponseOutput(TypedDict, closed=True):
    authorization_signature: NotRequired[
        "capo_bedrock_agentcore.types.stripe_privy_authorization_signature_type.StripePrivyAuthorizationSignatureType"
    ]
    """<p>Base64-encoded ECDSA P-256 authorization signature (only present when includeAuthorizationSignature is true).</p>"""
    request_expiry: NotRequired["int"]
    """<p>Unix timestamp in milliseconds when the authorization signature expires.</p>"""
    app_id: "capo_bedrock_agentcore.types.stripe_privy_app_id_type.StripePrivyAppIdType"
    """<p>The Privy app ID for the privy-app-id header.</p>"""
    basic_auth_token: "capo_bedrock_agentcore.types.stripe_privy_basic_auth_token_type.StripePrivyBasicAuthTokenType"
    """<p>Base64-encoded Basic Auth token (appId:appSecret) for the Authorization header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StripePrivyTokenResponseOutput) -> dict:
    out: dict = {}
    if "authorization_signature" in value:
        out["authorizationSignature"] = value["authorization_signature"]
    if "request_expiry" in value:
        out["requestExpiry"] = value["request_expiry"]
    out["appId"] = value["app_id"]
    out["basicAuthToken"] = value["basic_auth_token"]
    return out


def deserialize_json(data: dict) -> StripePrivyTokenResponseOutput:
    out: StripePrivyTokenResponseOutput = {}  # type: ignore[typeddict-item]
    if data.get("authorizationSignature") is not None:
        out["authorization_signature"] = data["authorizationSignature"]
    if data.get("requestExpiry") is not None:
        out["request_expiry"] = data["requestExpiry"]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("StripePrivyTokenResponseOutput.app_id required")
    if data.get("basicAuthToken") is not None:
        out["basic_auth_token"] = data["basicAuthToken"]
    else:
        raise DeserializationError(
            "StripePrivyTokenResponseOutput.basic_auth_token required"
        )
    return out


def redact_sensitive(value: StripePrivyTokenResponseOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorization_signature" in value:
        out["authorization_signature"] = "*** Sensitive Data Redacted ***"
    if "basic_auth_token" in value:
        out["basic_auth_token"] = "*** Sensitive Data Redacted ***"
    return out
