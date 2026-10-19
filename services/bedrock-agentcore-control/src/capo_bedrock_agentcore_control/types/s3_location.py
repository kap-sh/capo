"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#S3Location``."""

from typing_extensions import NotRequired, TypedDict


class S3Location(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the Amazon S3 bucket. This bucket contains the stored data.</p>"""
    prefix: "str"
    """<p>The prefix for objects in the Amazon S3 bucket. This prefix is added to the object keys to organize the data.</p>"""
    version_id: NotRequired["str"]
    """<p>The version ID of the Amazon Amazon S3 object. If not specified, the latest version of the object is used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["prefix"] = value["prefix"]
    if "version_id" in value:
        out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    else:
        out["prefix"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    return out
