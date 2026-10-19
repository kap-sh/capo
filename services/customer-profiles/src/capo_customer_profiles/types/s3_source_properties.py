"""Generated from Smithy shape ``com.amazonaws.customerprofiles#S3SourceProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.bucket_name
    import capo_customer_profiles.types.bucket_prefix


class S3SourceProperties(TypedDict, closed=True):
    bucket_name: "capo_customer_profiles.types.bucket_name.BucketName"
    """<p>The Amazon S3 bucket name where the source files are stored.</p>"""
    bucket_prefix: NotRequired[
        "capo_customer_profiles.types.bucket_prefix.BucketPrefix"
    ]
    """<p>The object key for the Amazon S3 bucket in which the source files are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3SourceProperties) -> dict:
    out: dict = {}
    out["BucketName"] = value["bucket_name"]
    if "bucket_prefix" in value:
        out["BucketPrefix"] = value["bucket_prefix"]
    return out


def deserialize_json(data: dict) -> S3SourceProperties:
    out: S3SourceProperties = {}  # type: ignore[typeddict-item]
    if data.get("BucketName") is not None:
        out["bucket_name"] = data["BucketName"]
    else:
        out["bucket_name"] = ""
    if data.get("BucketPrefix") is not None:
        out["bucket_prefix"] = data["BucketPrefix"]
    return out
