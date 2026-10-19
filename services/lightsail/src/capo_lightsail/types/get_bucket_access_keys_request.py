"""Generated from Smithy shape ``com.amazonaws.lightsail#GetBucketAccessKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_name


class GetBucketAccessKeysRequest(TypedDict, closed=True):
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to return access keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBucketAccessKeysRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBucketAccessKeysRequest:
    out: GetBucketAccessKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        out["bucket_name"] = ""
    return out
