"""Generated from Smithy shape ``com.amazonaws.forecast#EncryptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.kms_key_arn


class EncryptionConfig(TypedDict, closed=True):
    role_arn: "capo_forecast.types.arn.Arn"
    """<p>The ARN of the IAM role that Amazon Forecast can assume to access the KMS key.</p> <p>Passing a role across Amazon Web Services accounts is not allowed. If you pass a role that isn't in your account, you get an <code>InvalidInputException</code> error.</p>"""
    kms_key_arn: "capo_forecast.types.kms_key_arn.KMSKeyArn"
    """<p>The Amazon Resource Name (ARN) of the KMS key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncryptionConfig) -> dict:
    out: dict = {}
    out["RoleArn"] = value["role_arn"]
    out["KMSKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EncryptionConfig:
    out: EncryptionConfig = {}  # type: ignore[typeddict-item]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        out["role_arn"] = ""
    if data.get("KMSKeyArn") is not None:
        out["kms_key_arn"] = data["KMSKeyArn"]
    else:
        out["kms_key_arn"] = ""
    return out
