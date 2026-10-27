"""Generated from Smithy shape ``com.amazonaws.deadline#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.s3_bucket_name
    import capo_deadline.types.s3_key


class S3Location(TypedDict, closed=True):
    bucket_name: "capo_deadline.types.s3_bucket_name.S3BucketName"
    """The name of the Amazon S3 bucket."""
    key: "capo_deadline.types.s3_key.S3Key"
    """The Amazon S3 object key that uniquely identifies the Amazon S3 bucket."""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    return out
