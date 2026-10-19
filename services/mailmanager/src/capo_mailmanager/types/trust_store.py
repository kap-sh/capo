"""Generated from Smithy shape ``com.amazonaws.mailmanager#TrustStore``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ca_content
    import capo_mailmanager.types.crl_content
    import capo_mailmanager.types.kms_key_arn


class TrustStore(TypedDict, closed=True):
    ca_content: "capo_mailmanager.types.ca_content.CAContent"
    """<p>The PEM-encoded certificate authority (CA) certificates bundle for the trust store.</p>"""
    crl_content: NotRequired["capo_mailmanager.types.crl_content.CrlContent"]
    """<p>The PEM-encoded certificate revocation lists (CRLs) for the trust store. There can be one CRL per certificate authority (CA) in the trust store.</p>"""
    kms_key_arn: NotRequired["capo_mailmanager.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the trust store contents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TrustStore) -> dict:
    out: dict = {}
    out["CAContent"] = value["ca_content"]
    if "crl_content" in value:
        out["CrlContent"] = value["crl_content"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TrustStore:
    out: TrustStore = {}  # type: ignore[typeddict-item]
    if data.get("CAContent") is not None:
        out["ca_content"] = data["CAContent"]
    else:
        out["ca_content"] = ""
    if data.get("CrlContent") is not None:
        out["crl_content"] = data["CrlContent"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out


def redact_sensitive(value: TrustStore) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ca_content" in value:
        out["ca_content"] = "*** Sensitive Data Redacted ***"
    if "crl_content" in value:
        out["crl_content"] = "*** Sensitive Data Redacted ***"
    return out
