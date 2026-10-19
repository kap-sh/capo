"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OAuthClientCredential``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.sensitive_string


class OAuthClientCredential(TypedDict, closed=True):
    client_id: "str"
    """The OAuth 2.0 client identifier registered with the external system."""
    client_secret: "capo_cloudwatchomni.types.sensitive_string.SensitiveString"
    """The OAuth 2.0 client secret that pairs with the client identifier."""
    provider_id: NotRequired["str"]
    """The identifier of the OAuth provider that issued the client credentials."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OAuthClientCredential) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    if "provider_id" in value:
        out["providerId"] = value["provider_id"]
    return out


def deserialize_cbor(data: dict) -> OAuthClientCredential:
    out: OAuthClientCredential = {}  # type: ignore[typeddict-item]
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    else:
        out["client_id"] = ""
    if data.get("clientSecret") is not None:
        out["client_secret"] = data["clientSecret"]
    else:
        out["client_secret"] = ""
    if data.get("providerId") is not None:
        out["provider_id"] = data["providerId"]
    return out
