"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#LabelsS3InputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.s3_bucket
    import capo_lookoutequipment.types.s3_prefix


class LabelsS3InputConfiguration(TypedDict, closed=True):
    bucket: "capo_lookoutequipment.types.s3_bucket.S3Bucket"
    """<p>The name of the S3 bucket holding the label data. </p>"""
    prefix: NotRequired["capo_lookoutequipment.types.s3_prefix.S3Prefix"]
    """<p> The prefix for the S3 bucket used for the label data. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LabelsS3InputConfiguration) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LabelsS3InputConfiguration:
    out: LabelsS3InputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    return out
