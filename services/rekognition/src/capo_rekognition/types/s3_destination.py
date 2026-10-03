"""Generated from Smithy shape ``com.amazonaws.rekognition#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.s3_bucket
    import capo_rekognition.types.s3_key_prefix


class S3Destination(TypedDict, closed=True):
    bucket: NotRequired["capo_rekognition.types.s3_bucket.S3Bucket"]
    """<p> The name of the Amazon S3 bucket you want to associate with the streaming video project. You must be the owner of the Amazon S3 bucket. </p>"""
    key_prefix: NotRequired["capo_rekognition.types.s3_key_prefix.S3KeyPrefix"]
    """<p> The prefix value of the location within the bucket that you want the information to be published to. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html">Using prefixes</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Destination) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["Bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["KeyPrefix"] = value["key_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    if data.get("KeyPrefix") is not None:
        out["key_prefix"] = data["KeyPrefix"]
    return out
