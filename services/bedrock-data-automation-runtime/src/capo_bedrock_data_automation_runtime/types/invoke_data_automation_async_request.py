"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#InvokeDataAutomationAsyncRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.blueprint_list
    import capo_bedrock_data_automation_runtime.types.data_automation_configuration
    import capo_bedrock_data_automation_runtime.types.data_automation_profile_arn
    import capo_bedrock_data_automation_runtime.types.encryption_configuration
    import capo_bedrock_data_automation_runtime.types.idempotency_token
    import capo_bedrock_data_automation_runtime.types.input_configuration
    import capo_bedrock_data_automation_runtime.types.notification_configuration
    import capo_bedrock_data_automation_runtime.types.output_configuration
    import capo_bedrock_data_automation_runtime.types.tag_list


class InvokeDataAutomationAsyncRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_data_automation_runtime.types.idempotency_token.IdempotencyToken"
    ]
    """Idempotency token."""
    input_configuration: "capo_bedrock_data_automation_runtime.types.input_configuration.InputConfiguration"
    """Input configuration."""
    output_configuration: "capo_bedrock_data_automation_runtime.types.output_configuration.OutputConfiguration"
    """Output configuration."""
    data_automation_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.data_automation_configuration.DataAutomationConfiguration"
    ]
    """Data automation configuration."""
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.encryption_configuration.EncryptionConfiguration"
    ]
    """Encryption configuration."""
    notification_configuration: NotRequired[
        "capo_bedrock_data_automation_runtime.types.notification_configuration.NotificationConfiguration"
    ]
    """Notification configuration."""
    blueprints: NotRequired[
        "capo_bedrock_data_automation_runtime.types.blueprint_list.BlueprintList"
    ]
    """Blueprint list."""
    data_automation_profile_arn: "capo_bedrock_data_automation_runtime.types.data_automation_profile_arn.DataAutomationProfileArn"
    """Data automation profile ARN"""
    tags: NotRequired["capo_bedrock_data_automation_runtime.types.tag_list.TagList"]
    """List of tags."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvokeDataAutomationAsyncRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_data_automation_runtime.types.input_configuration

    out["inputConfiguration"] = (
        capo_bedrock_data_automation_runtime.types.input_configuration.serialize_aws_json_1_1(
            value["input_configuration"]
        )
    )
    import capo_bedrock_data_automation_runtime.types.output_configuration

    out["outputConfiguration"] = (
        capo_bedrock_data_automation_runtime.types.output_configuration.serialize_aws_json_1_1(
            value["output_configuration"]
        )
    )
    if "data_automation_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.data_automation_configuration

        out["dataAutomationConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.data_automation_configuration.serialize_aws_json_1_1(
                value["data_automation_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
            )
        )
    if "notification_configuration" in value:
        import capo_bedrock_data_automation_runtime.types.notification_configuration

        out["notificationConfiguration"] = (
            capo_bedrock_data_automation_runtime.types.notification_configuration.serialize_aws_json_1_1(
                value["notification_configuration"]
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
    if "tags" in value:
        import capo_bedrock_data_automation_runtime.types.tag_list

        out["tags"] = (
            capo_bedrock_data_automation_runtime.types.tag_list.serialize_aws_json_1_1(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvokeDataAutomationAsyncRequest:
    out: InvokeDataAutomationAsyncRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("inputConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.input_configuration

        out["input_configuration"] = (
            capo_bedrock_data_automation_runtime.types.input_configuration.deserialize_aws_json_1_1(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationAsyncRequest.input_configuration required"
        )
    if data.get("outputConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation_runtime.types.output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationAsyncRequest.output_configuration required"
        )
    if data.get("dataAutomationConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.data_automation_configuration

        out["data_automation_configuration"] = (
            capo_bedrock_data_automation_runtime.types.data_automation_configuration.deserialize_aws_json_1_1(
                data["dataAutomationConfiguration"]
            )
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_data_automation_runtime.types.encryption_configuration.deserialize_aws_json_1_1(
                data["encryptionConfiguration"]
            )
        )
    if data.get("notificationConfiguration") is not None:
        import capo_bedrock_data_automation_runtime.types.notification_configuration

        out["notification_configuration"] = (
            capo_bedrock_data_automation_runtime.types.notification_configuration.deserialize_aws_json_1_1(
                data["notificationConfiguration"]
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
    if data.get("tags") is not None:
        import capo_bedrock_data_automation_runtime.types.tag_list

        out["tags"] = (
            capo_bedrock_data_automation_runtime.types.tag_list.deserialize_aws_json_1_1(
                data["tags"]
            )
        )
    return out
