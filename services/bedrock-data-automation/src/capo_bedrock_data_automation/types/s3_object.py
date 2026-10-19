"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#S3Object``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.s3_object_version
    import capo_bedrock_data_automation.types.s3_uri


class S3Object(TypedDict, closed=True):
    s3_uri: "capo_bedrock_data_automation.types.s3_uri.S3Uri"
    """S3 uri."""
    version: NotRequired[
        "capo_bedrock_data_automation.types.s3_object_version.S3ObjectVersion"
    ]
    """S3 object version."""


# --- restJson1 ser/de ---
def serialize_json(value: S3Object) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "version" in value:
        out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> S3Object:
    out: S3Object = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    return out
