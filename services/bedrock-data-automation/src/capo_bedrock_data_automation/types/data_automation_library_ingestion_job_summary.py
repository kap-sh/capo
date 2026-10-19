"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryIngestionJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn
    import capo_bedrock_data_automation.types.date_timestamp
    import capo_bedrock_data_automation.types.entity_type
    import capo_bedrock_data_automation.types.library_ingestion_job_operation_type
    import capo_bedrock_data_automation.types.library_ingestion_job_status


class DataAutomationLibraryIngestionJobSummary(TypedDict, closed=True):
    job_arn: "capo_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn"
    job_status: "capo_bedrock_data_automation.types.library_ingestion_job_status.LibraryIngestionJobStatus"
    entity_type: "capo_bedrock_data_automation.types.entity_type.EntityType"
    operation_type: "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType"
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    completion_time: NotRequired[
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryIngestionJobSummary) -> dict:
    out: dict = {}
    out["jobArn"] = value["job_arn"]
    import capo_bedrock_data_automation.types.library_ingestion_job_status

    out["jobStatus"] = (
        capo_bedrock_data_automation.types.library_ingestion_job_status.serialize_json(
            value["job_status"]
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
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    if "completion_time" in value:
        import capo_bedrock_data_automation.types.date_timestamp

        out["completionTime"] = (
            capo_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["completion_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationLibraryIngestionJobSummary:
    out: DataAutomationLibraryIngestionJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("jobArn") is not None:
        out["job_arn"] = data["jobArn"]
    else:
        out["job_arn"] = ""
    if data.get("jobStatus") is not None:
        import capo_bedrock_data_automation.types.library_ingestion_job_status

        out["job_status"] = (
            capo_bedrock_data_automation.types.library_ingestion_job_status.deserialize_json(
                data["jobStatus"]
            )
        )
    else:
        import typing

        out["job_status"] = typing.cast(
            "capo_bedrock_data_automation.types.library_ingestion_job_status.LibraryIngestionJobStatus",
            "",
        )
    if data.get("entityType") is not None:
        import capo_bedrock_data_automation.types.entity_type

        out["entity_type"] = (
            capo_bedrock_data_automation.types.entity_type.deserialize_json(
                data["entityType"]
            )
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_bedrock_data_automation.types.entity_type.EntityType", ""
        )
    if data.get("operationType") is not None:
        import capo_bedrock_data_automation.types.library_ingestion_job_operation_type

        out["operation_type"] = (
            capo_bedrock_data_automation.types.library_ingestion_job_operation_type.deserialize_json(
                data["operationType"]
            )
        )
    else:
        import typing

        out["operation_type"] = typing.cast(
            "capo_bedrock_data_automation.types.library_ingestion_job_operation_type.LibraryIngestionJobOperationType",
            "",
        )
    if data.get("creationTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("completionTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["completion_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    return out
