"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateBucketRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.bucket_name
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.tag_list


class CreateBucketRequest(TypedDict, closed=True):
    bucket_name: "capo_lightsail.types.bucket_name.BucketName"
    """<p>The name for the bucket.</p> <p>For more information about bucket names, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/bucket-naming-rules-in-amazon-lightsail">Bucket naming rules in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""
    bundle_id: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The ID of the bundle to use for the bucket.</p> <p>A bucket bundle specifies the monthly cost, storage space, and data transfer quota for a bucket.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetBucketBundles.html">GetBucketBundles</a> action to get a list of bundle IDs that you can specify.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_UpdateBucketBundle.html">UpdateBucketBundle</a> action to change the bundle after the bucket is created.</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the bucket during creation.</p> <p>Use the <a href="https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_TagResource.html">TagResource</a> action to tag the bucket after it's created.</p>"""
    enable_object_versioning: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value that indicates whether to enable versioning of objects in the bucket.</p> <p>For more information about versioning, see <a href="https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-managing-bucket-object-versioning">Enabling and suspending object versioning in a bucket in Amazon Lightsail</a> in the <i>Amazon Lightsail Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBucketRequest) -> dict:
    out: dict = {}
    out["bucketName"] = value["bucket_name"]
    out["bundleId"] = value["bundle_id"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "enable_object_versioning" in value:
        out["enableObjectVersioning"] = value["enable_object_versioning"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBucketRequest:
    out: CreateBucketRequest = {}  # type: ignore[typeddict-item]
    if data.get("bucketName") is not None:
        out["bucket_name"] = data["bucketName"]
    else:
        raise DeserializationError("CreateBucketRequest.bucket_name required")
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError("CreateBucketRequest.bundle_id required")
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("enableObjectVersioning") is not None:
        out["enable_object_versioning"] = data["enableObjectVersioning"]
    return out
