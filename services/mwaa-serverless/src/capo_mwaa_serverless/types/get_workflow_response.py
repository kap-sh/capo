"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#GetWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.code
    import capo_mwaa_serverless.types.definition_s3_location
    import capo_mwaa_serverless.types.description_string
    import capo_mwaa_serverless.types.encryption_configuration
    import capo_mwaa_serverless.types.engine_version
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.logging_configuration
    import capo_mwaa_serverless.types.name_string
    import capo_mwaa_serverless.types.network_configuration
    import capo_mwaa_serverless.types.role_arn
    import capo_mwaa_serverless.types.schedule_configuration
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_status
    import capo_mwaa_serverless.types.workflow_version


class GetWorkflowResponse(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the workflow.</p>"""
    workflow_version: NotRequired[
        "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version identifier of the workflow.</p>"""
    name: NotRequired["capo_mwaa_serverless.types.name_string.NameString"]
    """<p>The name of the workflow.</p>"""
    description: NotRequired[
        "capo_mwaa_serverless.types.description_string.DescriptionString"
    ]
    """<p>The description of the workflow.</p>"""
    created_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow was created, in ISO 8601 date-time format.</p>"""
    modified_at: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow was last modified, in ISO 8601 date-time format.</p>"""
    encryption_configuration: NotRequired[
        "capo_mwaa_serverless.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the workflow.</p>"""
    logging_configuration: NotRequired[
        "capo_mwaa_serverless.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The logging configuration for the workflow.</p>"""
    engine_version: NotRequired[
        "capo_mwaa_serverless.types.engine_version.EngineVersion"
    ]
    """<p>The version of the Amazon Managed Workflows for Apache Airflow Serverless engine that this workflow uses.</p>"""
    workflow_status: NotRequired[
        "capo_mwaa_serverless.types.workflow_status.WorkflowStatus"
    ]
    """<p>The current status of the workflow.</p>"""
    definition_s3_location: NotRequired[
        "capo_mwaa_serverless.types.definition_s3_location.DefinitionS3Location"
    ]
    """<p>The Amazon S3 location of the workflow definition file.</p>"""
    code: NotRequired["capo_mwaa_serverless.types.code.Code"]
    """<p>The Amazon S3 location of the code artifacts provided during workflow creation or update.</p>"""
    code_snapshotted_at: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The time at which the code artifacts were copied for this workflow, in ISO 8601 date-time format.</p>"""
    schedule_configuration: NotRequired[
        "capo_mwaa_serverless.types.schedule_configuration.ScheduleConfiguration"
    ]
    """<p>The schedule configuration for the workflow, including cron expressions for automated execution. Amazon Managed Workflows for Apache Airflow Serverless uses EventBridge Scheduler for cost-effective, timezone-aware scheduling. When a workflow includes schedule information in its YAML definition, the service automatically configures the appropriate triggers for automated execution. Only one version of a workflow can have an active schedule at any given time.</p>"""
    role_arn: NotRequired["capo_mwaa_serverless.types.role_arn.RoleARN"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used for workflow execution.</p>"""
    network_configuration: NotRequired[
        "capo_mwaa_serverless.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the workflow execution environment.</p>"""
    trigger_mode: NotRequired["capo_mwaa_serverless.types.generic_string.GenericString"]
    """<p>The trigger mode for the workflow execution.</p>"""
    workflow_definition: NotRequired[
        "capo_mwaa_serverless.types.generic_string.GenericString"
    ]
    """<p>The workflow definition content.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "encryption_configuration" in value:
        import capo_mwaa_serverless.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            capo_mwaa_serverless.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "logging_configuration" in value:
        import capo_mwaa_serverless.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_mwaa_serverless.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "engine_version" in value:
        import capo_mwaa_serverless.types.engine_version

        out["EngineVersion"] = (
            capo_mwaa_serverless.types.engine_version.serialize_aws_json_1_0(
                value["engine_version"]
            )
        )
    if "workflow_status" in value:
        import capo_mwaa_serverless.types.workflow_status

        out["WorkflowStatus"] = (
            capo_mwaa_serverless.types.workflow_status.serialize_aws_json_1_0(
                value["workflow_status"]
            )
        )
    if "definition_s3_location" in value:
        import capo_mwaa_serverless.types.definition_s3_location

        out["DefinitionS3Location"] = (
            capo_mwaa_serverless.types.definition_s3_location.serialize_aws_json_1_0(
                value["definition_s3_location"]
            )
        )
    if "code" in value:
        import capo_mwaa_serverless.types.code

        out["Code"] = capo_mwaa_serverless.types.code.serialize_aws_json_1_0(
            value["code"]
        )
    if "code_snapshotted_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["CodeSnapshottedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["code_snapshotted_at"]
            )
        )
    if "schedule_configuration" in value:
        import capo_mwaa_serverless.types.schedule_configuration

        out["ScheduleConfiguration"] = (
            capo_mwaa_serverless.types.schedule_configuration.serialize_aws_json_1_0(
                value["schedule_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "network_configuration" in value:
        import capo_mwaa_serverless.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_mwaa_serverless.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    if "workflow_definition" in value:
        out["WorkflowDefinition"] = value["workflow_definition"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetWorkflowResponse:
    out: GetWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("EncryptionConfiguration") is not None:
        import capo_mwaa_serverless.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_mwaa_serverless.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if data.get("LoggingConfiguration") is not None:
        import capo_mwaa_serverless.types.logging_configuration

        out["logging_configuration"] = (
            capo_mwaa_serverless.types.logging_configuration.deserialize_aws_json_1_0(
                data["LoggingConfiguration"]
            )
        )
    if data.get("EngineVersion") is not None:
        import capo_mwaa_serverless.types.engine_version

        out["engine_version"] = (
            capo_mwaa_serverless.types.engine_version.deserialize_aws_json_1_0(
                data["EngineVersion"]
            )
        )
    if data.get("WorkflowStatus") is not None:
        import capo_mwaa_serverless.types.workflow_status

        out["workflow_status"] = (
            capo_mwaa_serverless.types.workflow_status.deserialize_aws_json_1_0(
                data["WorkflowStatus"]
            )
        )
    if data.get("DefinitionS3Location") is not None:
        import capo_mwaa_serverless.types.definition_s3_location

        out["definition_s3_location"] = (
            capo_mwaa_serverless.types.definition_s3_location.deserialize_aws_json_1_0(
                data["DefinitionS3Location"]
            )
        )
    if data.get("Code") is not None:
        import capo_mwaa_serverless.types.code

        out["code"] = capo_mwaa_serverless.types.code.deserialize_aws_json_1_0(
            data["Code"]
        )
    if data.get("CodeSnapshottedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["code_snapshotted_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CodeSnapshottedAt"]
            )
        )
    if data.get("ScheduleConfiguration") is not None:
        import capo_mwaa_serverless.types.schedule_configuration

        out["schedule_configuration"] = (
            capo_mwaa_serverless.types.schedule_configuration.deserialize_aws_json_1_0(
                data["ScheduleConfiguration"]
            )
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("NetworkConfiguration") is not None:
        import capo_mwaa_serverless.types.network_configuration

        out["network_configuration"] = (
            capo_mwaa_serverless.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if data.get("TriggerMode") is not None:
        out["trigger_mode"] = data["TriggerMode"]
    if data.get("WorkflowDefinition") is not None:
        out["workflow_definition"] = data["WorkflowDefinition"]
    return out
