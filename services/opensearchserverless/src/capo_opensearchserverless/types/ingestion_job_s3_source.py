"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionJobS3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.bucket_owner_account_id
    import capo_opensearchserverless.types.s3_bucket_name_or_arn


class IngestionJobS3Source(TypedDict, closed=True):
    bucket: NotRequired[
        "capo_opensearchserverless.types.s3_bucket_name_or_arn.S3BucketNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the Amazon S3 bucket to ingest data from.</p>"""
    bucket_owner_account_id: NotRequired[
        "capo_opensearchserverless.types.bucket_owner_account_id.BucketOwnerAccountId"
    ]
    """<p>The Amazon Web Services account ID that owns the Amazon S3 bucket.</p>"""
    key_prefix: NotRequired["str"]
    """<p>A key prefix that limits ingestion to objects in the Amazon S3 bucket whose keys begin with the prefix.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionJobS3Source) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "bucket_owner_account_id" in value:
        out["bucketOwnerAccountId"] = value["bucket_owner_account_id"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionJobS3Source:
    out: IngestionJobS3Source = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("bucketOwnerAccountId") is not None:
        out["bucket_owner_account_id"] = data["bucketOwnerAccountId"]
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    return out
