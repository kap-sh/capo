"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#StreamBucketConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.bucket_owner_account_id
    import capo_opensearchserverless.types.initial_scan
    import capo_opensearchserverless.types.s3_bucket_name_or_arn


class StreamBucketConfig(TypedDict, closed=True):
    bucket: "capo_opensearchserverless.types.s3_bucket_name_or_arn.S3BucketNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the Amazon S3 bucket to ingest data from.</p>"""
    bucket_owner_account_id: NotRequired[
        "capo_opensearchserverless.types.bucket_owner_account_id.BucketOwnerAccountId"
    ]
    """The AWS account ID that owns the S3 bucket. Optional. If omitted, the control plane derives it from the account segment of sqsArn."""
    initial_scan: NotRequired[
        "capo_opensearchserverless.types.initial_scan.InitialScan"
    ]
    """<p>Specifies whether to perform a one-time scan of the objects that already exist in the bucket before the stream begins processing Amazon S3 event notifications. If <code>DISABLED</code>, only new objects are ingested.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StreamBucketConfig) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "bucket_owner_account_id" in value:
        out["bucketOwnerAccountId"] = value["bucket_owner_account_id"]
    if "initial_scan" in value:
        out["initialScan"] = value["initial_scan"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StreamBucketConfig:
    out: StreamBucketConfig = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("bucketOwnerAccountId") is not None:
        out["bucket_owner_account_id"] = data["bucketOwnerAccountId"]
    if data.get("initialScan") is not None:
        out["initial_scan"] = data["initialScan"]
    return out
