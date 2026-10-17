"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingSessionS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.customer_kms_key_arn
    import capo_sagemaker.types.output_s3_path


class TrainingSessionS3Location(TypedDict, closed=True):
    path: NotRequired["capo_sagemaker.types.output_s3_path.OutputS3Path"]
    """<p>The Amazon S3 path where training session outputs are stored.</p>"""
    kms_key_arn: NotRequired[
        "capo_sagemaker.types.customer_kms_key_arn.CustomerKmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt output data. If not specified, the default Amazon S3 encryption is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingSessionS3Location) -> dict:
    out: dict = {}
    if "path" in value:
        out["Path"] = value["path"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingSessionS3Location:
    out: TrainingSessionS3Location = {}  # type: ignore[typeddict-item]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
