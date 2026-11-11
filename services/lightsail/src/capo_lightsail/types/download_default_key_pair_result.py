"""Generated from Smithy shape ``com.amazonaws.lightsail#DownloadDefaultKeyPairResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.base64
    import capo_lightsail.types.iso_date
    import capo_lightsail.types.sensitive_base64


class DownloadDefaultKeyPairResult(TypedDict, closed=True):
    public_key_base64: NotRequired["capo_lightsail.types.base64.Base64"]
    """<p>A base64-encoded public key of the <code>ssh-rsa</code> type.</p>"""
    private_key_base64: NotRequired[
        "capo_lightsail.types.sensitive_base64.SensitiveBase64"
    ]
    """<p>A base64-encoded RSA private key.</p>"""
    created_at: NotRequired["capo_lightsail.types.iso_date.IsoDate"]
    """<p>The timestamp when the default key pair was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DownloadDefaultKeyPairResult) -> dict:
    out: dict = {}
    if "public_key_base64" in value:
        out["publicKeyBase64"] = value["public_key_base64"]
    if "private_key_base64" in value:
        out["privateKeyBase64"] = value["private_key_base64"]
    if "created_at" in value:
        import capo_lightsail.types.iso_date

        out["createdAt"] = capo_lightsail.types.iso_date.serialize_aws_json_1_1(
            value["created_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DownloadDefaultKeyPairResult:
    out: DownloadDefaultKeyPairResult = {}  # type: ignore[typeddict-item]
    if data.get("publicKeyBase64") is not None:
        out["public_key_base64"] = data["publicKeyBase64"]
    if data.get("privateKeyBase64") is not None:
        out["private_key_base64"] = data["privateKeyBase64"]
    if data.get("createdAt") is not None:
        import capo_lightsail.types.iso_date

        out["created_at"] = capo_lightsail.types.iso_date.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    return out


def redact_sensitive(value: DownloadDefaultKeyPairResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_key_base64" in value:
        out["private_key_base64"] = "*** Sensitive Data Redacted ***"
    return out
