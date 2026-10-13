"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InvokeDataAutomationLibraryIngestionJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.entity_type
    import capo_bedrock_data_automation.types.input_configuration
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type
    import capo_bedrock_data_automation.types.notification_configuration
    import capo_bedrock_data_automation.types.output_configuration
    import capo_bedrock_data_automation.types.tag_list


class InvokeDataAutomationLibraryIngestionJobRequest(TypedDict, closed=True):
    library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]
    """Idempotency token"""
    input_configuration: (
        "capo_bedrock_data_automation.types.input_configuration.InputConfiguration"
    )
    """Input configuration of DataAutomationLibraryIngestionJob request"""
    entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType"
    """The entity type for which DataAutomationLibraryIngestionJob is being run"""
    operation_type: "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType"
    """The operation to be performed by DataAutomationLibraryIngestionJob"""
    output_configuration: (
        "capo_bedrock_data_automation.types.output_configuration.OutputConfiguration"
    )
    """Output configuration of DataAutomationLibraryIngestionJob"""
    notification_configuration: NotRequired[
        "capo_bedrock_data_automation.types.notification_configuration.NotificationConfiguration"
    ]
    """Notification configuration."""
    tags: NotRequired["capo_bedrock_data_automation.types.tag_list.TagList"]
    """List of tags"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeDataAutomationLibraryIngestionJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_bedrock_data_automation.types.input_configuration

    out["inputConfiguration"] = (
        capo_bedrock_data_automation.types.input_configuration.serialize_json(
            value["input_configuration"]
        )
    )
    import capo_bedrock_data_automation.types.entity_type

    out["entityType"] = capo_bedrock_data_automation.types.entity_type.serialize_json(
        value["entity_type"]
    )
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type

    out["operationType"] = (
        capo_bedrock_data_automation.types.library_ingestion_job_operation_type.serialize_json(
            value["operation_type"]
        )
    )
    import capo_bedrock_data_automation.types.output_configuration

    out["outputConfiguration"] = (
        capo_bedrock_data_automation.types.output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    if "notification_configuration" in value:
        import capo_bedrock_data_automation.types.notification_configuration

        out["notificationConfiguration"] = (
            capo_bedrock_data_automation.types.notification_configuration.serialize_json(
                value["notification_configuration"]
            )
        )
    if "tags" in value:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> InvokeDataAutomationLibraryIngestionJobRequest:
    out: InvokeDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("inputConfiguration") is not None:
        import capo_bedrock_data_automation.types.input_configuration

        out["input_configuration"] = (
            capo_bedrock_data_automation.types.input_configuration.deserialize_json(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.input_configuration required"
        )
    if data.get("entityType") is not None:
        import capo_bedrock_data_automation.types.entity_type

        out["entity_type"] = (
            capo_bedrock_data_automation.types.entity_type.deserialize_json(
                data["entityType"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.entity_type required"
        )
    if data.get("operationType") is not None:
        import capo_bedrock_data_automation.types.library_ingestion_job_operation_type

        out["operation_type"] = (
            capo_bedrock_data_automation.types.library_ingestion_job_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.operation_type required"
        )
    if data.get("outputConfiguration") is not None:
        import capo_bedrock_data_automation.types.output_configuration

        out["output_configuration"] = (
            capo_bedrock_data_automation.types.output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "InvokeDataAutomationLibraryIngestionJobRequest.output_configuration required"
        )
    if data.get("notificationConfiguration") is not None:
        import capo_bedrock_data_automation.types.notification_configuration

        out["notification_configuration"] = (
            capo_bedrock_data_automation.types.notification_configuration.deserialize_json(
                data["notificationConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(
    value: InvokeDataAutomationLibraryIngestionJobRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_configuration" in value:
        import capo_bedrock_data_automation.types.input_configuration

        out["input_configuration"] = (
            capo_bedrock_data_automation.types.input_configuration.redact_sensitive(
                value["input_configuration"]
            )
        )
    return out
