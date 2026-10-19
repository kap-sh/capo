"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateBucketAccessKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_name


class CreateBucketAccessKeyRequest(TypedDict, closed=True):
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket that the new access key will belong to, and grant access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBucketAccessKeyRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBucketAccessKeyRequest:
    out: CreateBucketAccessKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    return out
