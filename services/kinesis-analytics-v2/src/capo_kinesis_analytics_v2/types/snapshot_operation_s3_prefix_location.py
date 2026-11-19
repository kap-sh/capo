"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationS3PrefixLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.bucket_arn
    import capo_kinesis_analytics_v2.types.key_prefix


class SnapshotOperationS3PrefixLocation(TypedDict, closed=True):
    bucket_arn: "capo_kinesis_analytics_v2.types.bucket_arn.BucketARN"
    """<p>The ARN of the Amazon S3 bucket.</p>"""
    key_prefix: "capo_kinesis_analytics_v2.types.key_prefix.KeyPrefix"
    """<p>The key prefix in the Amazon S3 bucket that you specified in the request.</p>"""
    exported_prefix: NotRequired["capo_kinesis_analytics_v2.types.key_prefix.KeyPrefix"]
    """<p>The full key prefix that the exported snapshot data was written to. This value includes the unique prefix that Managed Service for Apache Flink appends to <code>KeyPrefix</code>. This field is present only after an <code>ExportSnapshot</code> operation completes successfully.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationS3PrefixLocation) -> dict:
    out: dict = {}
    out["BucketARN"] = value["bucket_arn"]
    out["KeyPrefix"] = value["key_prefix"]
    if "exported_prefix" in value:
        out["ExportedPrefix"] = value["exported_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotOperationS3PrefixLocation:
    out: SnapshotOperationS3PrefixLocation = {}  # type: ignore[typeddict-item]
    if data.get("BucketARN") is not None:
        out["bucket_arn"] = data["BucketARN"]
    else:
        out["bucket_arn"] = ""
    if data.get("KeyPrefix") is not None:
        out["key_prefix"] = data["KeyPrefix"]
    else:
        out["key_prefix"] = ""
    if data.get("ExportedPrefix") is not None:
        out["exported_prefix"] = data["ExportedPrefix"]
    return out
