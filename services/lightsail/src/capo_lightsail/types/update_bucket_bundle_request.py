"""Generated from Smithy shape ``com.amazonaws.lightsail#UpdateBucketBundleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.non_empty_string


class UpdateBucketBundleRequest(TypedDict, closed=True):
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name of the bucket for which to update the bundle.</p>"""
    bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The ID of the new bundle to apply to the bucket.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html">GetBucketBundles</a> action to get a list of bundle IDs that you can specify.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBucketBundleRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["bundleId"] = value["bundle_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBucketBundleRequest:
    out: UpdateBucketBundleRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("UpdateBucketBundleRequest.bucket_name required")
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("UpdateBucketBundleRequest.bundle_id required")
    return out
