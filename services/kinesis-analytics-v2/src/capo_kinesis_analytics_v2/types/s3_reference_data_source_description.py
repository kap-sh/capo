"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ReferenceDataSourceDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.bucket_arn
    import capo_kinesis_analytics_v2.types.file_key
    import capo_kinesis_analytics_v2.types.role_arn


class S3ReferenceDataSourceDescription(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    file_key: "capo_kinesis_analytics_v2.types.file_key.FileKey"
    """<p>Amazon S3 object key name.</p>"""
    reference_role_arn: NotRequired["capo_kinesis_analytics_v2.types.role_arn.RoleARN"]
    """<p>The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table. </p> <note> <p>Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ReferenceDataSourceDescription) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    if "reference_role_arn" in value:
        out["ReferenceRoleARN"] = value["reference_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ReferenceDataSourceDescription:
    out: S3ReferenceDataSourceDescription = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("FileKey") is not None:
        out["file_key"] = data["FileKey"]
    else:
        out["file_key"] = ""
    if data.get("ReferenceRoleARN") is not None:
        out["reference_role_arn"] = data["ReferenceRoleARN"]
    return out
