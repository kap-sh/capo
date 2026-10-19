"""Generated from Smithy shape ``com.amazonaws.healthlake#DataTransformationS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.data_transformation_s3_uri
    import capo_healthlake.types.kms_key_id


class DataTransformationS3Configuration(TypedDict, closed=True):
    s3_uri: "capo_healthlake.types.data_transformation_s3_uri.DataTransformationS3Uri"
    """<p>The Amazon S3 URI where HealthLake writes the converted output files.</p>"""
    kms_key_id: "capo_healthlake.types.kms_key_id.KmsKeyId"
    """<p>The Amazon Web Services Key Management Service (Amazon Web Services KMS) key identifier used to encrypt the transformation job output written to Amazon S3.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DataTransformationS3Configuration) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    out["KmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DataTransformationS3Configuration:
    out: DataTransformationS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    else:
        out["kms_key_id"] = ""
    return out
