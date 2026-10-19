"""Generated from Smithy shape ``com.amazonaws.mgn#S3BucketSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_key


class S3BucketSource(TypedDict, closed=True):
    s3_bucket: "capo_mgn.types.s3_bucket_name.S3BucketName"
    """<p>S3 bucket source s3 bucket.</p>"""
    s3_key: "capo_mgn.types.s3_key.S3Key"
    """<p>S3 bucket source s3 key.</p>"""
    s3_bucket_owner: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>S3 bucket source s3 bucket owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketSource) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3Key"] = value["s3_key"]
    if "s3_bucket_owner" in value:
        out["s3BucketOwner"] = value["s3_bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3BucketSource:
    out: S3BucketSource = {}  # type: ignore[typeddict-item]
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("s3Key") is not None:
        out["s3_key"] = data["s3Key"]
    else:
        out["s3_key"] = ""
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    return out
