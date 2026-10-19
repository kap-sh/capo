"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#S3Repository``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.name
    import capo_codeguru_reviewer.types.s3_bucket_name


class S3Repository(TypedDict, closed=True):
    name: "capo_codeguru_reviewer.types.name.Name"
    """<p>The name of the repository in the S3 bucket.</p>"""
    bucket_name: "capo_codeguru_reviewer.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket used for associating a new S3 repository. It must begin with <code>codeguru-reviewer-</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Repository) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["BucketName"] = value["bucket_name"]
    return out


def deserialize_json(data: dict) -> S3Repository:
    out: S3Repository = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    return out
