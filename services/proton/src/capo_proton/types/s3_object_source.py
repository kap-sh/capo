"""Generated from Smithy shape ``com.amazonaws.proton#S3ObjectSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_proton.types.s3_bucket
    import capo_proton.types.s3_key


class S3ObjectSource(TypedDict, closed=True):
    bucket: "capo_proton.types.s3_bucket.S3Bucket"
    """<p>The name of the S3 bucket that contains a template bundle.</p>"""
    key: "capo_proton.types.s3_key.S3Key"
    """<p>The path to the S3 bucket that contains a template bundle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ObjectSource) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ObjectSource:
    out: S3ObjectSource = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    return out
