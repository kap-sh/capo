"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#UpdateWorkflowResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.timestamp_value
    import capo_mwaa_serverless.types.warning_messages
    import capo_mwaa_serverless.types.workflow_arn
    import capo_mwaa_serverless.types.workflow_version


class UpdateWorkflowResponse(TypedDict, closed=True):
    workflow_arn: "capo_mwaa_serverless.types.workflow_arn.WorkflowArn"
    """<p>The Amazon Resource Name (ARN) of the updated workflow.</p>"""
    modified_at: NotRequired[
        "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    ]
    """<p>The timestamp when the workflow was last modified, in ISO 8601 date-time format.</p>"""
    workflow_version: NotRequired[
        "capo_mwaa_serverless.types.workflow_version.WorkflowVersion"
    ]
    """<p>The version identifier of the updated workflow.</p>"""
    warnings: NotRequired["capo_mwaa_serverless.types.warning_messages.WarningMessages"]
    """<p>Warning messages generated during workflow update.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWorkflowResponse) -> dict:
    out: dict = {}
    out["WorkflowArn"] = value["workflow_arn"]
    if "modified_at" in value:
        import capo_mwaa_serverless.types.timestamp_value

        out["ModifiedAt"] = (
            capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "workflow_version" in value:
        out["WorkflowVersion"] = value["workflow_version"]
    if "warnings" in value:
        import capo_mwaa_serverless.types.warning_messages

        out["Warnings"] = (
            capo_mwaa_serverless.types.warning_messages.serialize_aws_json_1_0(
                value["warnings"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWorkflowResponse:
    out: UpdateWorkflowResponse = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowArn") is not None:
        out["workflow_arn"] = data["WorkflowArn"]
    else:
        out["workflow_arn"] = ""
    if data.get("ModifiedAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["modified_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if data.get("WorkflowVersion") is not None:
        out["workflow_version"] = data["WorkflowVersion"]
    if data.get("Warnings") is not None:
        import capo_mwaa_serverless.types.warning_messages

        out["warnings"] = (
            capo_mwaa_serverless.types.warning_messages.deserialize_aws_json_1_0(
                data["Warnings"]
            )
        )
    return out
