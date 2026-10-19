"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#OutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.s3_uri


class OutputConfiguration(TypedDict, closed=True):
    s3_uri: "capo_bedrock_data_automation_runtime.types.s3_uri.S3Uri"
    """S3 uri."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputConfiguration) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OutputConfiguration:
    out: OutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out
