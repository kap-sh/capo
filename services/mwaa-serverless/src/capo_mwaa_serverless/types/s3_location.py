"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#S3Location``."""

from typing_extensions import NotRequired, TypedDict


class S3Location(TypedDict, closed=True):
    bucket: "str"
    """<p>The name of the Amazon S3 bucket.</p>"""
    object_key: "str"
    """<p>The key of the code artifact within the Amazon S3 bucket.</p>"""
    version_id: NotRequired["str"]
    """<p>The version ID of the object in Amazon S3. If not specified, the latest version is used.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Location) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["ObjectKey"] = value["object_key"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("ObjectKey") is not None:
        out["object_key"] = data["ObjectKey"]
    else:
        out["object_key"] = ""
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    return out
