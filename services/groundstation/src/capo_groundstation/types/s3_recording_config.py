"""Generated from Smithy shape ``com.amazonaws.groundstation#S3RecordingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.bucket_arn
    import capo_groundstation.types.role_arn
    import capo_groundstation.types.s3_key_prefix


class S3RecordingConfig(TypedDict, closed=True):
    bucket_arn: "capo_groundstation.types.bucket_arn.BucketArn"
    """<p>ARN of the bucket to record to.</p>"""
    role_arn: "capo_groundstation.types.role_arn.RoleArn"
    """<p>ARN of the role Ground Station assumes to write data to the bucket.</p>"""
    prefix: NotRequired["capo_groundstation.types.s3_key_prefix.S3KeyPrefix"]
    """<p>S3 Key prefix to prefice data files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3RecordingConfig) -> dict:
    out: dict = {}
    out["bucketArn"] = value["bucket_arn"]
    out["roleArn"] = value["role_arn"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> S3RecordingConfig:
    out: S3RecordingConfig = {}  # type: ignore[typeddict-item]
    if data.get("bucketArn") is not None:
        out["bucket_arn"] = data["bucketArn"]
    else:
        out["bucket_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
