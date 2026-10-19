"""Generated from Smithy shape ``com.amazonaws.apprunner#EncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.kms_key_arn


class EncryptionConfiguration(TypedDict, closed=True):
    kms_key: "capo_apprunner.types.kms_key_arn.KmsKeyArn"
    """<p>The ARN of the KMS key that's used for encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionConfiguration) -> dict:
    out: dict = {}
    out["KmsKey"] = value["kms_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EncryptionConfiguration:
    out: EncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("KmsKey") is not None:
        out["kms_key"] = data["KmsKey"]
    else:
        out["kms_key"] = ""
    return out
