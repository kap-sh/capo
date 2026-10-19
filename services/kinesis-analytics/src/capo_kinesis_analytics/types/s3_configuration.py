"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#S3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.bucket_arn
    import capo_kinesis_analytics.types.file_key
    import capo_kinesis_analytics.types.role_arn


class S3Configuration(TypedDict, closed=True):
    role_arn: "capo_kinesis_analytics.types.role_arn.RoleARN"
    """<p>IAM ARN of the role used to access the data.</p>"""
    bucket_arn: "capo_kinesis_analytics.types.bucket_arn.BucketARN"
    """<p>ARN of the S3 bucket that contains the data.</p>"""
    file_key: "capo_kinesis_analytics.types.file_key.FileKey"
    """<p>The name of the object that contains the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Configuration) -> dict:
    out: dict = {}
    out["RoleARN"] = value["role_arn"]
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("RoleARN") is not None:
        out["role_arn"] = data["RoleARN"]
    else:
        out["role_arn"] = ""
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("FileKey") is not None:
        out["file_key"] = data["FileKey"]
    else:
        out["file_key"] = ""
    return out
