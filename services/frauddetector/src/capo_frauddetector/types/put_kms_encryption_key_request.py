"""Generated from Smithy shape ``com.amazonaws.frauddetector#PutKMSEncryptionKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.kms_encryption_key_arn


class PutKMSEncryptionKeyRequest(TypedDict, closed=True):
    kms_encryption_key_arn: (
        "capo_frauddetector.types.kms_encryption_key_arn.KmsEncryptionKeyArn"
    )
    """<p>The KMS encryption key ARN.</p> <p>The KMS key must be single-Region key. Amazon Fraud Detector does not support multi-Region KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutKMSEncryptionKeyRequest) -> dict:
    out: dict = {}
    out["kmsEncryptionKeyArn"] = value["kms_encryption_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutKMSEncryptionKeyRequest:
    out: PutKMSEncryptionKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("kmsEncryptionKeyArn") is not None:
        out["kms_encryption_key_arn"] = data["kmsEncryptionKeyArn"]
    else:
        out["kms_encryption_key_arn"] = ""
    return out
