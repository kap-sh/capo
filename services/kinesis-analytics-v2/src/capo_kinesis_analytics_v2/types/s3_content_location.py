"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ContentLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.bucket_arn
    import capo_kinesis_analytics_v2.types.file_key
    import capo_kinesis_analytics_v2.types.object_version


class S3ContentLocation(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The Amazon Resource Name (ARN) for the S3 bucket containing the application code.</p>"""
    file_key: "capo_kinesis_analytics_v2.types.file_key.FileKey"
    """<p>The file key for the object containing the application code.</p>"""
    object_version: NotRequired[
        "capo_kinesis_analytics_v2.types.object_version.ObjectVersion"
    ]
    """<p>The version of the object containing the application code.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ContentLocation) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    if "object_version" in value:
        out["ObjectVersion"] = value["object_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ContentLocation:
    out: S3ContentLocation = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("FileKey") is not None:
        out["file_key"] = data["FileKey"]
    else:
        out["file_key"] = ""
    if data.get("ObjectVersion") is not None:
        out["object_version"] = data["ObjectVersion"]
    return out
