"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InvokeBlueprintOptimizationAsyncRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_optimization_object
    import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration
    import capo_bedrock_data_automation.types.blueprint_optimization_samples
    import capo_bedrock_data_automation.types.data_automation_profile_arn
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.tag_list


class InvokeBlueprintOptimizationAsyncRequest(TypedDict, closed=True):
    blueprint: "capo_bedrock_data_automation.types.blueprint_optimization_object.BlueprintOptimizationObject"
    """Blueprint to be optimized"""
    samples: "capo_bedrock_data_automation.types.blueprint_optimization_samples.BlueprintOptimizationSamples"
    """List of Blueprint Optimization Samples"""
    output_configuration: "capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.BlueprintOptimizationOutputConfiguration"
    """Output configuration where the results should be placed"""
    data_automation_profile_arn: "capo_bedrock_data_automation.types.data_automation_profile_arn.DataAutomationProfileArn"
    """Data automation profile ARN"""
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]
    """Encryption configuration."""
    tags: NotRequired["capo_bedrock_data_automation.types.tag_list.TagList"]
    """List of tags."""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeBlueprintOptimizationAsyncRequest) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.blueprint_optimization_object

    out["blueprint"] = (
        capo_bedrock_data_automation.types.blueprint_optimization_object.serialize_json(
            value["blueprint"]
        )
    )
    import capo_bedrock_data_automation.types.blueprint_optimization_samples

    out["samples"] = (
        capo_bedrock_data_automation.types.blueprint_optimization_samples.serialize_json(
            value["samples"]
        )
    )
    import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration

    out["outputConfiguration"] = (
        capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    out["dataAutomationProfileArn"] = value["data_automation_profile_arn"]
    if "encryption_configuration" in value:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> InvokeBlueprintOptimizationAsyncRequest:
    out: InvokeBlueprintOptimizationAsyncRequest = {}  # type: ignore[typeddict-item]
    if data.get("blueprint") is not None:
        import capo_bedrock_data_automation.types.blueprint_optimization_object

        out["blueprint"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_object.deserialize_json(
                data["blueprint"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeBlueprintOptimizationAsyncRequest.blueprint required"
        )
    if data.get("samples") is not None:
        import capo_bedrock_data_automation.types.blueprint_optimization_samples

        out["samples"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_samples.deserialize_json(
                data["samples"]
            )
        )
    else:
        out["samples"] = []
    if data.get("outputConfiguration") is not None:
        import capo_bedrock_data_automation.types.blueprint_optimization_output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation.types.blueprint_optimization_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeBlueprintOptimizationAsyncRequest.output_configuration required"
        )
    if data.get("dataAutomationProfileArn") is not None:
        out["data_automation_profile_arn"] = data["dataAutomationProfileArn"]
    else:
        out["data_automation_profile_arn"] = ""
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
