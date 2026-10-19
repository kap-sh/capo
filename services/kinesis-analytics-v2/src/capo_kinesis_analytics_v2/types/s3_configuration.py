"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.bucket_arn
    import capo_kinesis_analytics_v2.types.file_key


class S3Configuration(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The ARN of the S3 bucket that contains the data.</p>"""
    file_key: "capo_kinesis_analytics_v2.types.file_key.FileKey"
    """<p>The name of the object that contains the data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Configuration) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["FileKey"] = value["file_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Configuration:
    out: S3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("FileKey") is not None:
        out["file_key"] = data["FileKey"]
    else:
        out["file_key"] = ""
    return out
