"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.output_configuration
    import capo_bedrock_data_automation_runtime.types.output_segment_list
    import capo_bedrock_data_automation_runtime.types.semantic_modality


class InvokeDataAutomationResponse(TypedDict, closed=True):
    output_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
    ]
    """Output configuration"""
    semantic_modality: (
        "capo_bedrock_data_automation_runtime.types.semantic_modality.SemanticModality"
    )
    """Detected semantic modality"""
    output_segments: "capo_bedrock_data_automation_runtime.types.output_segment_list.OutputSegmentList"
    """List of outputs for each logical sub-doc"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationResponse) -> dict:
    out: dict = {}
    if "output_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["outputConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    import capo_bedrock_data_automation_runtime.types.semantic_modality

    out["semanticModality"] = (
        capo_bedrock_data_automation_runtime.types.semantic_modality.serialize_aws_json_1_1(
            value["semantic_modality"]
        )
    )
    import capo_bedrock_data_automation_runtime.types.output_segment_list

    out["outputSegments"] = (
        capo_bedrock_data_automation_runtime.types.output_segment_list.serialize_aws_json_1_1(
            value.get("output_segments", [])
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationResponse:
    out: InvokeDataAutomationResponse = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    if data.get("semanticModality") is not None:
        import capo_bedrock_data_automation_runtime.types.semantic_modality

        out["semantic_modality"] = (
            capo_bedrock_data_automation_runtime.types.semantic_modality.deserialize_aws_json_1_1(
                data["semanticModality"]
            )
        )
    else:
        import typing

        out["semantic_modality"] = typing.cast(
            "capo_bedrock_data_automation_runtime.types.semantic_modality.SemanticModality",
            "",
        )
    if data.get("outputSegments") is not None:
        import capo_bedrock_data_automation_runtime.types.output_segment_list

        out["output_segments"] = (
            capo_bedrock_data_automation_runtime.types.output_segment_list.deserialize_aws_json_1_1(
                data["outputSegments"]
            )
        )
    else:
        out["output_segments"] = []
    return out
