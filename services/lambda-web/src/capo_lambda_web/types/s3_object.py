"""Generated from Smithy shape ``com.amazonaws.lambdaweb#S3Object``."""

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError


class S3Object(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the Amazon S3 bucket. Must be between 3 and 63 characters.</p>"""
    key: "str"
    """<p>The Amazon S3 object key. Must be between 1 and 1024 characters.</p>"""
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
        raise DeserializationError("S3Object.bucket required")
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("S3Object.key required")
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    return out
