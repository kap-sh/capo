"""Generated from Smithy shape ``com.amazonaws.taxsettings#DestinationS3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.s3_bucket_name
    import capo_taxsettings.types.s3_prefix


class DestinationS3Location(TypedDict, closed=True):
    bucket: "capo_taxsettings.types.s3_bucket_name.S3BucketName"
    """<p>The name of your Amazon S3 bucket that you specify to download your tax documents to.</p>"""
    prefix: NotRequired["capo_taxsettings.types.s3_prefix.S3Prefix"]
    """<p>The Amazon S3 object prefix that you specify for your tax document file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationS3Location) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "prefix" in value:
        out["prefix"] = value["prefix"]
    return out


def deserialize_json(data: dict) -> DestinationS3Location:
    out: DestinationS3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("prefix") is not None:
        out["prefix"] = data["prefix"]
    return out
