"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#IngestionS3InputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.key_pattern
    import capo_lookoutequipment.types.s3_bucket
    import capo_lookoutequipment.types.s3_prefix


class IngestionS3InputConfiguration(TypedDict, closed=True):
    bucket: "capo_lookoutequipment.types.s3_bucket.S3Bucket"
    """<p>The name of the S3 bucket used for the input data for the data ingestion. </p>"""
    prefix: NotRequired["capo_lookoutequipment.types.s3_prefix.S3Prefix"]
    """<p>The prefix for the S3 location being used for the input data for the data ingestion. </p>"""
    key_pattern: NotRequired["capo_lookoutequipment.types.key_pattern.KeyPattern"]
    """<p> The pattern for matching the Amazon S3 files that will be used for ingestion. If the schema was created previously without any KeyPattern, then the default KeyPattern {prefix}/{component_name}/* is used to download files from Amazon S3 according to the schema. This field is required when ingestion is being done for the first time.</p> <p>Valid Values: {prefix}/{component_name}_* | {prefix}/{component_name}/* | {prefix}/{component_name}[DELIMITER]* (Allowed delimiters : space, dot, underscore, hyphen)</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionS3InputConfiguration) -> dict:
    out: dict = {}
    out["Bucket"] = value["bucket"]
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "key_pattern" in value:
        out["KeyPattern"] = value["key_pattern"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionS3InputConfiguration:
    out: IngestionS3InputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Bucket") is not None:
        out["bucket"] = data["Bucket"]
    else:
        out["bucket"] = ""
    if data.get("Prefix") is not None:
        out["prefix"] = data["Prefix"]
    if data.get("KeyPattern") is not None:
        out["key_pattern"] = data["KeyPattern"]
    return out
