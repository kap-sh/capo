"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#S3DestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.s3_bucket_name
    import capo_mediapackagev2.types.s3_destination_path


class S3DestinationConfig(TypedDict, closed=True):
    bucket_name: "capo_mediapackagev2.types.s3_bucket_name.S3BucketName"
    """<p>The name of an S3 bucket within which harvested content will be exported.</p>"""
    destination_path: "capo_mediapackagev2.types.s3_destination_path.S3DestinationPath"
    """<p>The path within the specified S3 bucket where the harvested content will be placed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3DestinationConfig) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["DestinationPath"] = value["destination_path"]
    return out


def deserialize_json(data: dict) -> S3DestinationConfig:
    out: S3DestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("DestinationPath") is not None:
        out["destination_path"] = data["DestinationPath"]
    else:
        out["destination_path"] = ""
    return out
