"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisOutputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.media_analysis_s3_key_prefix
    import capo_rekognition.types.s3_bucket


class MediaAnalysisOutputConfig(TypedDict, closed=True):
    s3_bucket: "capo_rekognition.types.s3_bucket.S3Bucket"
    """<p>Specifies the Amazon S3 bucket to contain the output of the media analysis job.</p>"""
    s3_key_prefix: NotRequired[
        "capo_rekognition.types.media_analysis_s3_key_prefix.MediaAnalysisS3KeyPrefix"
    ]
    """<p>Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for storage.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisOutputConfig) -> dict:
    out: dict = {}
    out["S3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["S3KeyPrefix"] = value["s3_key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisOutputConfig:
    out: MediaAnalysisOutputConfig = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    else:
        out["s3_bucket"] = ""
    if data.get("S3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["S3KeyPrefix"]
    return out
