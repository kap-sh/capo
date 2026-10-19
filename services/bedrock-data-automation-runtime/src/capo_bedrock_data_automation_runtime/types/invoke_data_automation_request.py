"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.blueprint_list
    import capo_bedrock_data_automation_runtime.types.data_automation_configuration
    import capo_bedrock_data_automation_runtime.types.data_automation_profile_arn
    import capo_bedrock_data_automation_runtime.types.encryption_configuration
    import capo_bedrock_data_automation_runtime.types.output_configuration
    import capo_bedrock_data_automation_runtime.types.sync_input_configuration


class InvokeDataAutomationRequest(TypedDict, closed=True):
    input_configuration: "capo_bedrock_data_automation_runtime.types.sync_input_configuration.SyncInputConfiguration"
    """Input configuration."""
    data_automation_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
    ]
    """Data automation configuration."""
    blueprints: NotRequired[
        "capo_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
    ]
    """Blueprint list."""
    data_automation_profile_arn: "capo_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn"
    """Data automation profile ARN"""
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
    ]
    """Encryption configuration."""
    output_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
    ]
    """Output configuration."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationRequest) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation_runtime.types.sync_input_configuration

    out["inputConfiguration"] = (
        capo_bedrock_data_automation_runtime.types.sync_input_configuration.serialize_aws_json_1_1(
            value["input_configuration"]
        )
    )
    if "data_automation_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.data_automation_configuration

        out["dataAutomationConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.data_automation_configuration.serialize_aws_json_1_1(
                value["data_automation_configuration"]
            )
        )
    if "blueprints" in value:
        import capo_bedrock_data_automation_runtime.types.blueprint_list

        out["blueprints"] = (
            capo_bedrock_data_automation_runtime.types.blueprint_list.serialize_aws_json_1_1(
                value["blueprints"]
            )
        )
    out["dataAutomationProfileArn"] = value["data_automation_profile_arn"]
    if "encryption_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "output_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["outputConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
                value["output_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationRequest:
    out: InvokeDataAutomationRequest = {}  # type: ignore[typeddict-item]
    if data.get("inputConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.sync_input_configuration

        out["input_configuration"] = (
            capo_bedrock_data_automation_runtime.types.sync_input_configuration.deserialize_aws_json_1_1(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationRequest.input_configuration required"
        )
    if data.get("dataAutomationConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.data_automation_configuration

        out["data_automation_configuration"] = (
            capo_bedrock_data_automation_runtime.types.data_automation_configuration.deserialize_aws_json_1_1(
                data["dataAutomationConfiguration"]
            )
        )
    if data.get("blueprints") is not None:
        import capo_bedrock_data_automation_runtime.types.blueprint_list

        out["blueprints"] = (
            capo_bedrock_data_automation_runtime.types.blueprint_list.deserialize_aws_json_1_1(
                data["blueprints"]
            )
        )
    if data.get("dataAutomationProfileArn") is not None:
        out["data_automation_profile_arn"] = data["dataAutomationProfileArn"]
    else:
        out["data_automation_profile_arn"] = ""
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_data_automation_runtime.types.encryption_configuration.deserialize_aws_json_1_1(
                data["encryptionConfiguration"]
            )
        )
    if data.get("outputConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    return out
