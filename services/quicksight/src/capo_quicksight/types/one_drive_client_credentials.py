"""Generated from Smithy shape ``com.amazonaws.quicksight#OneDriveClientCredentials``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_source_cert_thumbprint
    import capo_quicksight.types.data_source_kms_key_arn


class OneDriveClientCredentials(TypedDict, closed=True):
    kms_key_arn: "capo_quicksight.types.data_source_kms_key_arn.DataSourceKmsKeyArn"
    """<p>The Amazon Resource Name (ARN) of the AWS Key Management Service (AWS KMS) key used to encrypt the OneDrive certificate credentials. This field is required.</p>"""
    cert_thumbprint: (
        "capo_quicksight.types.data_source_cert_thumbprint.DataSourceCertThumbprint"
    )
    """<p>The thumbprint of the certificate used for two-legged OAuth (2LO) authentication to OneDrive. This field is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OneDriveClientCredentials) -> dict:
    out: dict = {}
    out["KmsKeyArn"] = value["kms_key_arn"]
    out["CertThumbprint"] = value["cert_thumbprint"]
    return out


def deserialize_json(data: dict) -> OneDriveClientCredentials:
    out: OneDriveClientCredentials = {}  # type: ignore[typeddict-item]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        out["kms_key_arn"] = ""
    if data.get("CertThumbprint") is not None:
        out["cert_thumbprint"] = data["CertThumbprint"]
    else:
        out["cert_thumbprint"] = ""
    return out


def redact_sensitive(value: OneDriveClientCredentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "kms_key_arn" in value:
        out["kms_key_arn"] = "*** Sensitive Data Redacted ***"
    if "cert_thumbprint" in value:
        out["cert_thumbprint"] = "*** Sensitive Data Redacted ***"
    return out
