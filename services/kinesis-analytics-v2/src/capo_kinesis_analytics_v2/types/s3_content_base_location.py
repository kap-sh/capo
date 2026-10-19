"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3ContentBaseLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.base_path
    import capo_kinesis_analytics_v2.types.bucket_arn


class S3ContentBaseLocation(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    base_path: NotRequired["capo_kinesis_analytics_v2.types.base_path.BasePath"]
    """<p>The base path for the S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ContentBaseLocation) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    if "base_path" in value:
        out["BasePath"] = value["base_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ContentBaseLocation:
    out: S3ContentBaseLocation = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("BasePath") is not None:
        out["base_path"] = data["BasePath"]
    return out
