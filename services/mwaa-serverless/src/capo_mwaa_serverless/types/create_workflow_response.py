"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#CreateWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.is_latest_version
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.warning_messages
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_status
    import capo_mwaa_serverless.types.workflow_version


class CreateWorkflowResponse(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the newly created workflow. This ARN uniquely identifies the workflow resource.</p>"""
    created_at: NotRequired["capo_mwaa_serverless.types.timestamp_value.TimestampValue"]
    """<p>The timestamp when the workflow was created, in ISO 8601 date-time format.</p>"""
    revision_id: NotRequired["str"]
    """<p>A unique identifier for this revision of the workflow configuration. This ID changes when the workflow is updated and you can use it for optimistic concurrency control in update operations. The revision ID helps prevent conflicting updates and ensures that updates are applied to the expected version of the workflow configuration.</p>"""
    workflow_status: NotRequired[
        "capo_mwaa_serverless.types.workflow_status.WorkflowStatus"
    ]
    """<p>The current status of the workflow. Possible values are <code>READY</code> (workflow is ready to run) and <code>DELETING</code> (workflow is being deleted).</p>"""
    workflow_version: NotRequired[
        "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version identifier of the workflow. This is a service-generated alphanumeric string that uniquely identifies this version of the workflow. Amazon Managed Workflows for Apache Airflow Serverless uses a version-first approach where each workflow can have multiple immutable versions, which allows you to maintain different configurations and roll back to previous versions as needed. The version identifier is used in ARNs and API operations to reference specific workflow versions.</p>"""
    is_latest_version: NotRequired[
        "capo_mwaa_serverless.types.is_latest_version.IsLatestVersion"
    ]
    """<p>A Boolean flag that indicates whether this workflow version is the latest version of the workflow.</p>"""
    warnings: NotRequired["capo_mwaa_serverless.types.warning_messages.WarningMessages"]
    """<p>Warning messages generated during workflow creation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "created_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["CreatedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "workflow_status" in value:
        import capo_mwaa_serverless.types.workflow_status

        out["WorkflowStatus"] = (
            capo_mwaa_serverless.types.workflow_status.serialize_aws_json_1_0(
                value["workflow_status"]
            )
        )
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "is_latest_version" in value:
        out["IsLatestVersion"] = value["is_latest_version"]
    if "warnings" in value:
        import capo_mwaa_serverless.types.warning_messages

        out["Warnings"] = (
            capo_mwaa_serverless.types.warning_messages.serialize_aws_json_1_0(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkflowResponse:
    out: CreateWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("CreatedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["created_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    if data.get("WorkflowStatus") is not None:
        import capo_mwaa_serverless.types.workflow_status

        out["workflow_status"] = (
            capo_mwaa_serverless.types.workflow_status.deserialize_aws_json_1_0(
                data["WorkflowStatus"]
            )
        )
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    if data.get("IsLatestVersion") is not None:
        out["is_latest_version"] = data["IsLatestVersion"]
    if data.get("Warnings") is not None:
        import capo_mwaa_serverless.types.warning_messages

        out["warnings"] = (
            capo_mwaa_serverless.types.warning_messages.deserialize_aws_json_1_0(
                data["Warnings"]
            )
        )
    return out
