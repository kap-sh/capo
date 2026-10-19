"""Generated from Smithy shape ``com.amazonaws.signin#AccessToken``."""

from typing_extensions import TypedDict


class AccessToken(TypedDict, closed=True):
    access_key_id: "str"
    """AWS access key ID for temporary credentials"""
    secret_access_key: "str"
    """AWS secret access key for temporary credentials"""
    session_token: "str"
    """AWS session token for temporary credentials"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessToken) -> dict:
    out: dict = {}
    out["accessKeyId"] = value["access_key_id"]
    out["secretAccessKey"] = value["secret_access_key"]
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_json(data: dict) -> AccessToken:
    out: AccessToken = {}  # type: ignore[typeddict-item]
    if data.get("accessKeyId") is not None:
        out["access_key_id"] = data["accessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("secretAccessKey") is not None:
        out["secret_access_key"] = data["secretAccessKey"]
    else:
        out["secret_access_key"] = ""
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    else:
        out["session_token"] = ""
    return out
