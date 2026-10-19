"""Generated from Smithy shape ``com.amazonaws.finspacedata#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.s3_bucket_name
    import capo_finspace_data.types.s3_key


class S3Location(TypedDict, closed=True):
    bucket: "capo_finspace_data.types.s3_bucket_name.S3BucketName"
    """<p> The name of the S3 bucket.</p>"""
    key: "capo_finspace_data.types.s3_key.S3Key"
    """<p> The path of the folder, within the S3 bucket that contains the Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    return out
