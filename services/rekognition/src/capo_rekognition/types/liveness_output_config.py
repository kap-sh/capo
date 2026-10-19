"""Generated from Smithy shape ``com.amazonaws.rekognition#LivenessOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.liveness_s3_key_prefix
    import capo_rekognition.types.s3_bucket


class LivenessOutputConfig(TypedDict, closed=True):
    s3_bucket: "capo_rekognition.types.s3_bucket.S3Bucket"
    """<p>The path to an AWS Amazon S3 bucket used to store Face Liveness session results.</p>"""
    s3_key_prefix: NotRequired[
        "capo_rekognition.types.liveness_s3_key_prefix.LivenessS3KeyPrefix"
    ]
    """<p>The prefix prepended to the output files for the Face Liveness session results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LivenessOutputConfig) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LivenessOutputConfig:
    out: LivenessOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
