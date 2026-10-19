"""Generated from Smithy shape ``com.amazonaws.kms#XksProxyAuthenticationCredentialType``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kms.types.xks_proxy_authentication_access_key_id_type
    import capo_kms.types.xks_proxy_authentication_raw_secret_access_key_type


class XksProxyAuthenticationCredentialType(TypedDict, closed=True):
    access_key_id: "capo_kms.types.xks_proxy_authentication_access_key_id_type.XksProxyAuthenticationAccessKeyIdType"
    """<p>A unique identifier for the raw secret access key.</p>"""
    raw_secret_access_key: "capo_kms.types.xks_proxy_authentication_raw_secret_access_key_type.XksProxyAuthenticationRawSecretAccessKeyType"
    """<p>A secret string of 43-64 characters. Valid characters are a-z, A-Z, 0-9, /, +, and =.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XksProxyAuthenticationCredentialType) -> dict:
    out: dict = {}
    out["AccessKeyId"] = value["access_key_id"]
    out["RawSecretAccessKey"] = value["raw_secret_access_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XksProxyAuthenticationCredentialType:
    out: XksProxyAuthenticationCredentialType = {}  # type: ignore[typeddict-item]
    if data.get("AccessKeyId") is not None:
        out["access_key_id"] = data["AccessKeyId"]
    else:
        out["access_key_id"] = ""
    if data.get("RawSecretAccessKey") is not None:
        out["raw_secret_access_key"] = data["RawSecretAccessKey"]
    else:
        out["raw_secret_access_key"] = ""
    return out


def redact_sensitive(value: XksProxyAuthenticationCredentialType) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_key_id" in value:
        out["access_key_id"] = "*** Sensitive Data Redacted ***"
    if "raw_secret_access_key" in value:
        out["raw_secret_access_key"] = "*** Sensitive Data Redacted ***"
    return out
