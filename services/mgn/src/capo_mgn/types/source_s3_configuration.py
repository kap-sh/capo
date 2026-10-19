"""Generated from Smithy shape ``com.amazonaws.mgn#SourceS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_key_name


class SourceS3Configuration(TypedDict, closed=True):
    s3_bucket: "capo_mgn.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket containing source data.</p>"""
    s3_bucket_owner: "capo_mgn.types.account_id.AccountID"
    """<p>The AWS account ID of the S3 bucket owner.</p>"""
    s3_key: "capo_mgn.types.s3_key_name.S3KeyName"
    """<p>The S3 key (path) for the source data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceS3Configuration) -> dict:
    out: dict = {}
    out["s3Bucket"] = value["s3_bucket"]
    out["s3BucketOwner"] = value["s3_bucket_owner"]
    out["s3Key"] = value["s3_key"]
    return out


def deserialize_json(data: dict) -> SourceS3Configuration:
    out: SourceS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("s3BucketOwner") is not None:
        out["s3_bucket_owner"] = data["s3BucketOwner"]
    else:
        out["s3_bucket_owner"] = ""
    if data.get("s3Key") is not None:
        out["s3_key"] = data["s3Key"]
    else:
        out["s3_key"] = ""
    return out
