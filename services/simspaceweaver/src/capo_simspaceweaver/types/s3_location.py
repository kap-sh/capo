"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_simspaceweaver.types.bucket_name
    import capo_simspaceweaver.types.object_key


class S3Location(TypedDict, closed=True):
    bucket_name: "capo_simspaceweaver.types.bucket_name.BucketName"
    """<p>The name of an Amazon S3 bucket. For more information about buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html">Creating, configuring, and working with Amazon S3 buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""
    object_key: "capo_simspaceweaver.types.object_key.ObjectKey"
    """<p>The key name of an object in Amazon S3. For more information about Amazon S3 objects and object keys, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html">Uploading, downloading, and working with objects in Amazon S3</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Location) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    out["ObjectKey"] = value["object_key"]
    return out


def deserialize_json(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Location.bucket_name required")
    if data.get("ObjectKey") is not None:
        out["object_key"] = data["ObjectKey"]
    else:
        raise DeserializationError("S3Location.object_key required")
    return out
