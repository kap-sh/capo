"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#S3StorageConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.s3_bucket_name


class S3StorageConfiguration(TypedDict, closed=True):
    bucket_name: "capo_ivs_realtime.types.s3_bucket_name.S3BucketName"
    """<p>Location (S3 bucket name) where recorded videos will be stored. Note that the StorageConfiguration and S3 bucket must be in the same region as the Composition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3StorageConfiguration) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> S3StorageConfiguration:
    out: S3StorageConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    return out
