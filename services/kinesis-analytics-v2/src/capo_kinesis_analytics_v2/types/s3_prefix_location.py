"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#S3PrefixLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.bucket_arn
    import capo_kinesis_analytics_v2.types.key_prefix


class S3PrefixLocation(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The ARN of the Amazon S3 bucket.</p>"""
    key_prefix: "capo_kinesis_analytics_v2.types.key_prefix.KeyPrefix"
    """<p>The key prefix in the Amazon S3 bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3PrefixLocation) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["KeyPrefix"] = value["key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3PrefixLocation:
    out: S3PrefixLocation = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("KeyPrefix") is not None:
        out["key_prefix"] = data["KeyPrefix"]
    else:
        out["key_prefix"] = ""
    return out
