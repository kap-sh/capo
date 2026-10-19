"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.definition_s3_location
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.is_latest_version
    import capo_mwaa_serverless.types.schedule_configuration
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_version


class WorkflowVersionSummary(TypedDict, closed=True):
    workflow_version: "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
    """<p>The version identifier of the workflow version.</p>"""
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow that contains this version.</p>"""
    is_latest_version: NotRequired[
        "capo_mwaa_serverless.types.is_latest_version.IsLatestVersion"
    ]
    """<p>Boolean flag that indicates whether this is the latest version of the workflow.</p>"""
    created_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow version was created, in ISO 8601 date-time format.</p>"""
    modified_at: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow version was last modified, in ISO 8601 date-time format.</p>"""
    definition_s3_location: NotRequired[
        "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    ]
    """<p>The Amazon S3 location of the workflow definition file for this version.</p>"""
    schedule_configuration: NotRequired[
        "capo_mwaa_serverless.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule configuration for this workflow version.</p>"""
    trigger_mode: NotRequired["capo_mwaa_serverless.types.generic_string.GenericString"]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowVersionSummary) -> dict:
    out: dict = {}
    out["WorkflowVersion"] = value["workflow_version"]
    out["WorkflowArn"] = value["workflow_arn"]
    if "is_latest_version" in value:
        out["IsLatestVersion"] = value["is_latest_version"]
    if "created_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["CreatedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "modified_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["ModifiedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "definition_s3_location" in value:
        import capo_mwaa_serverless.types.definition_s3_location

        out["DefinitionS3Location"] = (
            capo_mwaa_serverless.types.definition_s3_location.serialize_aws_json_1_0(
                value["definition_s3_location"]
            )
        )
    if "schedule_configuration" in value:
        import capo_mwaa_serverless.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_mwaa_serverless.types.schedule_configuration.serialize_aws_json_1_0(
                value["schedule_configuration"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowVersionSummary:
    out: WorkflowVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    else:
        out["workflow_version"] = ""
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("IsLatestVersion") is not None:
        out["is_latest_version"] = data["IsLatestVersion"]
    if data.get("CreatedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["created_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("ModifiedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["modified_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if data.get("DefinitionS3Location") is not None:
        import capo_mwaa_serverless.types.definition_s3_location

        out["definition_s3_location"] = (
            capo_mwaa_serverless.types.definition_s3_location.deserialize_aws_json_1_0(
                data["DefinitionS3Location"]
            )
        )
    if data.get("ScheduleConfiguration") is not None:
        import capo_mwaa_serverless.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_mwaa_serverless.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("TriggerMode") is not None:
        out["trigger_mode"] = data["TriggerMode"]
    return out
