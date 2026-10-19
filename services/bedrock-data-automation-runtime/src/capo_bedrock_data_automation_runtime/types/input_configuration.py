"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.asset_processing_configuration
    import capo_bedrock_data_automation_runtime.types.s3_uri


class InputConfiguration(TypedDict, closed=True):
    s3_uri: "capo_bedrock_data_automation_runtime.types.s3_uri.S3Uri"
    """S3 uri."""
    asset_processing_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.asset_processing_configuration.AssetProcessingConfiguration"
    ]
    """Asset processing configuration"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputConfiguration) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "asset_processing_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.asset_processing_configuration

        out["assetProcessingConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.asset_processing_configuration.serialize_aws_json_1_1(
                value["asset_processing_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("assetProcessingConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.asset_processing_configuration

        out["asset_processing_configuration"] = (
            capo_bedrock_data_automation_runtime.types.asset_processing_configuration.deserialize_aws_json_1_1(
                data["assetProcessingConfiguration"]
            )
        )
    return out
