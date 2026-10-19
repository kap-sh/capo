"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OAuthCodeCredential``."""

from typing_extensions import TypedDict


class OAuthCodeCredential(TypedDict, closed=True):
    auth_code: "str"
    """The OAuth 2.0 authorization code returned by the external system's authorization endpoint."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: OAuthCodeCredential) -> dict:
    out: dict = {}
    out["authCode"] = value["auth_code"]
    return out


def deserialize_cbor(data: dict) -> OAuthCodeCredential:
    out: OAuthCodeCredential = {}  # type: ignore[typeddict-item]
    if data.get("authCode") is not None:
        out["auth_code"] = data["authCode"]
    else:
        out["auth_code"] = ""
    return out
