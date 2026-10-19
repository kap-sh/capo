"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdMappingJobOutputSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.kms_arn
    import capo_entityresolution.types.role_arn
    import capo_entityresolution.types.s3_path


class IdMappingJobOutputSource(TypedDict, closed=True):
    role_arn: "capo_entityresolution.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role. Entity Resolution assumes this role to access Amazon Web Services resources on your behalf as part of workflow execution.</p>"""
    output_s3_path: "capo_entityresolution.types.s3_path.S3Path"
    """<p>The S3 path to which Entity Resolution will write the output table.</p>"""
    kms_arn: NotRequired["capo_entityresolution.types.kms_arn.KMSArn"]
    """<p>Customer KMS ARN for encryption at rest. If not provided, system will use an Entity Resolution managed KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdMappingJobOutputSource) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["outputS3Path"] = value["output_s3_path"]
    if "kms_arn" in value:
        out["KMSArn"] = value["kms_arn"]
    return out


def deserialize_json(data: dict) -> IdMappingJobOutputSource:
    out: IdMappingJobOutputSource = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("outputS3Path") is not None:
        out["output_s3_path"] = data["outputS3Path"]
    else:
        out["output_s3_path"] = ""
    if data.get("KMSArn") is not None:
        out["kms_arn"] = data["KMSArn"]
    return out
