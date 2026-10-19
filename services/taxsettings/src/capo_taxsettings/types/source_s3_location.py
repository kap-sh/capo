"""Generated from Smithy shape ``com.amazonaws.taxsettings#SourceS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.s3_bucket_name
    import capo_taxsettings.types.s3_key


class SourceS3Location(TypedDict, closed=True):
    bucket: "capo_taxsettings.types.s3_bucket_name.S3BucketName"
    """<p>The name of your Amazon S3 bucket that your tax document is located.</p>"""
    key: "capo_taxsettings.types.s3_key.S3Key"
    """<p>The object key of your tax document object in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceS3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> SourceS3Location:
    out: SourceS3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    return out
