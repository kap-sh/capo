"""Generated from Smithy shape ``com.amazonaws.databrew#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.bucket
    import capo_databrew.types.bucket_owner
    import capo_databrew.types.key


class S3Location(TypedDict, closed=True):
    bucket: "capo_databrew.types.bucket.Bucket"
    """<p>The Amazon S3 bucket name.</p>"""
    key: NotRequired["capo_databrew.types.key.Key"]
    """<p>The unique name of the object in the bucket.</p>"""
    bucket_owner: NotRequired["capo_databrew.types.bucket_owner.BucketOwner"]
    """<p>The Amazon Web Services account ID of the bucket owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "key" in value:
        out["Key"] = value["key"]
    if "bucket_owner" in value:
        out["BucketOwner"] = value["bucket_owner"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("BucketOwner") is not None:
        out["bucket_owner"] = data["BucketOwner"]
    return out
