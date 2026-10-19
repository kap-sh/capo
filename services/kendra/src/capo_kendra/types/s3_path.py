"""Generated from Smithy shape ``com.amazonaws.kendra#S3Path``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.s3_bucket_name
    import capo_kendra.types.s3_object_key


class S3Path(TypedDict, closed=True):
    bucket: "capo_kendra.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket that contains the file.</p>"""
    key: "capo_kendra.types.s3_object_key.S3ObjectKey"
    """<p>The name of the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Path) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Path:
    out: S3Path = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    return out
