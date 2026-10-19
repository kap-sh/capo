"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#WorkflowSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.description_string
    import capo_mwaa_serverless.types.generic_string
    import capo_mwaa_serverless.types.name_string
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_status
    import capo_mwaa_serverless.types.workflow_version


class WorkflowSummary(TypedDict, closed=True):
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
    workflow_status: NotRequired[
        "capo_mwaa_serverless.types.workflow_status.WorkflowStatus"
    ]
    """<p>The current status of the workflow.</p>"""
    trigger_mode: NotRequired["capo_mwaa_serverless.types.generic_string.GenericString"]
    """<p>The trigger mode for the workflow execution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkflowSummary) -> dict:
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
    if "workflow_status" in value:
        import capo_mwaa_serverless.types.workflow_status

        out["WorkflowStatus"] = (
            capo_mwaa_serverless.types.workflow_status.serialize_aws_json_1_0(
                value["workflow_status"]
            )
        )
    if "trigger_mode" in value:
        out["TriggerMode"] = value["trigger_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> WorkflowSummary:
    out: WorkflowSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("WorkflowStatus") is not None:
        import capo_mwaa_serverless.types.workflow_status

        out["workflow_status"] = (
            capo_mwaa_serverless.types.workflow_status.deserialize_aws_json_1_0(
                data["WorkflowStatus"]
            )
        )
    if data.get("TriggerMode") is not None:
        out["trigger_mode"] = data["TriggerMode"]
    return out
