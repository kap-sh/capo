"""Generated from Smithy shape ``com.amazonaws.dynamodb#S3BucketSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.s3_bucket
    import capo_dynamodb.types.s3_bucket_owner
    import capo_dynamodb.types.s3_prefix


class S3BucketSource(TypedDict, closed=True):
    s3_bucket_owner: NotRequired["capo_dynamodb.types.s3_bucket_owner.S3BucketOwner"]
    """<p> The account number of the S3 bucket that is being imported from. If the bucket is owned by the requester this is optional. </p>"""
    s3_bucket: "capo_dynamodb.types.s3_bucket.S3Bucket"
    """<p> The S3 bucket that is being imported from. </p>"""
    s3_key_prefix: NotRequired["capo_dynamodb.types.s3_prefix.S3Prefix"]
    """<p> The key prefix shared by all S3 Objects that are being imported. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3BucketSource) -> dict:
    out: dict = {}
    if "s3_bucket_owner" in value:
        out["S3BucketOwner"] = value["s3_bucket_owner"]
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3BucketSource:
    out: S3BucketSource = {}  # type: ignore[typeddict-item]
    if data.get("S3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["S3BucketOwner"]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
