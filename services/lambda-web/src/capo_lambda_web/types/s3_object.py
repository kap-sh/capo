"""Generated from Smithy shape ``com.amazonaws.lambdaweb#S3Object``."""

from typing_extensions import NotRequired, TypedDict


class S3Object(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the Amazon S3 bucket.</p>"""
    key: "str"
    """<p>The Amazon S3 object key.</p>"""
    version_id: NotRequired["str"]
    """<p>The version ID of the Amazon S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    return out
