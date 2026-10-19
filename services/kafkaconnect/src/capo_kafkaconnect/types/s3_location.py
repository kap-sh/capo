"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__string


class S3Location(TypedDict, closed=True):
    bucket_arn: "capo_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of an S3 bucket.</p>"""
    file_key: "capo_kafkaconnect.types.__string.__string"
    """<p>The file key for an object in an S3 bucket.</p>"""
    object_version: NotRequired["capo_kafkaconnect.types.__string.__string"]
    """<p>The version of an object in an S3 bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["bucketArn"] = value["bucket_arn"]
    out["fileKey"] = value["file_key"]
    if "object_version" in value:
        out["objectVersion"] = value["object_version"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    else:
        out["bucket_arn"] = ""
    if data.get("fileKey") is not None:
        out["file_key"] = data["fileKey"]
    else:
        out["file_key"] = ""
    if data.get("objectVersion") is not None:
        out["object_version"] = data["objectVersion"]
    return out
