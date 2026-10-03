"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_simspaceweaver.errors import DeserializationError

if TYPE_CHECKING:
    import capo_simspaceweaver.types.bucket_name
    import capo_simspaceweaver.types.object_key_prefix


class S3Destination(TypedDict, closed=True):
    bucket_name: "capo_simspaceweaver.types.bucket_name.BucketName"
    """<p>The name of an Amazon S3 bucket. For more information about buckets, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html">Creating, configuring, and working with Amazon S3 buckets</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""
    object_key_prefix: NotRequired[
        "capo_simspaceweaver.types.object_key_prefix.ObjectKeyPrefix"
    ]
    """<p>A string prefix for an Amazon S3 object key. It's usually a folder name. For more information about folders in Amazon S3, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html">Organizing objects in the Amazon S3 console using folders</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "object_key_prefix" in value:
        out["ObjectKeyPrefix"] = value["object_key_prefix"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        raise DeserializationError("S3Destination.bucket_name required")
    if data.get("ObjectKeyPrefix") is not None:
        out["object_key_prefix"] = data["ObjectKeyPrefix"]
    return out
