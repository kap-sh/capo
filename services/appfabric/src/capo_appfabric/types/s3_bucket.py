"""Generated from Smithy shape ``com.amazonaws.appfabric#S3Bucket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.string63
    import capo_appfabric.types.string120


class S3Bucket(TypedDict, closed=True):
    bucket_name: "capo_appfabric.types.string63.String63"
    """<p>The name of the Amazon S3 bucket.</p>"""
    prefix: NotRequired["capo_appfabric.types.string120.String120"]
    """<p>The object key to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Bucket) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3Bucket:
    out: S3Bucket = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
