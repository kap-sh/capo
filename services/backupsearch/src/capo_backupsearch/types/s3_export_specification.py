"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ExportSpecification``."""

from typing_extensions import NotRequired, TypedDict


class S3ExportSpecification(TypedDict, closed=True):
    destination_bucket: "str"
    """<p>This specifies the destination Amazon S3 bucket for the export job.</p>"""
    destination_prefix: NotRequired["str"]
    """<p>This specifies the prefix for the destination Amazon S3 bucket for the export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ExportSpecification) -> dict:
    out: dict = {}
    out["DestinationBucket"] = value["destination_bucket"]
    if "destination_prefix" in value:
        out["DestinationPrefix"] = value["destination_prefix"]
    return out


def deserialize_json(data: dict) -> S3ExportSpecification:
    out: S3ExportSpecification = {}  # type: ignore[typeddict-item]
    if data.get("DestinationBucket") is not None:
        out["destination_bucket"] = data["DestinationBucket"]
    else:
        out["destination_bucket"] = ""
    if data.get("DestinationPrefix") is not None:
        out["destination_prefix"] = data["DestinationPrefix"]
    return out
