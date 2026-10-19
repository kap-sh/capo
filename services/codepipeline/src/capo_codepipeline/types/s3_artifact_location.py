"""Generated from Smithy shape ``com.amazonaws.codepipeline#S3ArtifactLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.s3_bucket_name
    import capo_codepipeline.types.s3_object_key


class S3ArtifactLocation(TypedDict, closed=True):
    bucket_name: "capo_codepipeline.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket.</p>"""
    object_key: "capo_codepipeline.types.s3_object_key.S3ObjectKey"
    """<p>The key of the object in the S3 bucket, which uniquely identifies the object in the bucket.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ArtifactLocation) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["objectKey"] = value["object_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3ArtifactLocation:
    out: S3ArtifactLocation = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("objectKey") is not None:
        out["object_key"] = data["objectKey"]
    else:
        out["object_key"] = ""
    return out
