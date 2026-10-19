"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.s3_bucket
    import capo_lookoutequipment.types.s3_key


class S3Object(TypedDict, closed=True):
    bucket: "capo_lookoutequipment.types.s3_bucket.S3Bucket"
    """<p>The name of the specific S3 bucket. </p>"""
    key: "capo_lookoutequipment.types.s3_key.S3Key"
    """<p>The Amazon Web Services Key Management Service (KMS key) key being used to encrypt the S3 object. Without this key, data in the bucket is not accessible. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3Object) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    out["Key"] = value["key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    return out
