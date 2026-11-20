"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#EncryptionConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key_arn: NotRequired["str"]
    """<p>The ARN of a customer managed AWS KMS key that encrypts the space's data. The key must be an enabled symmetric encryption key in the space's Region, and you need permission to create grants on it (<code>kms:CreateGrant</code>). Otherwise, the request fails with <code>ValidationException</code> or <code>AccessDeniedException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
