"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWorkflow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.structured_log_destinations
    import capo_transfer.types.tags
    import capo_transfer.types.workflow_description
    import capo_transfer.types.workflow_id
    import capo_transfer.types.workflow_steps


class DescribedWorkflow(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>Specifies the unique Amazon Resource Name (ARN) for the workflow.</p>"""
    description: NotRequired[
        "capo_transfer.types.workflow_description.WorkflowDescription"
    ]
    """<p>Specifies the text description for the workflow.</p>"""
    steps: NotRequired["capo_transfer.types.workflow_steps.WorkflowSteps"]
    """<p>Specifies the details for the steps that are in the specified workflow.</p>"""
    on_exception_steps: NotRequired["capo_transfer.types.workflow_steps.WorkflowSteps"]
    """<p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p>"""
    workflow_id: NotRequired["capo_transfer.types.workflow_id.WorkflowId"]
    """<p>A unique identifier for the workflow.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>"""
    structured_log_destinations: NotRequired[
        "capo_transfer.types.structured_log_destinations.StructuredLogDestinations"
    ]
    """<p>Specifies the log groups to which your workflow logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWorkflow) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "steps" in value:
        import capo_transfer.types.workflow_steps

        out["Steps"] = capo_transfer.types.workflow_steps.serialize_aws_json_1_1(
            value["steps"]
        )
    if "on_exception_steps" in value:
        import capo_transfer.types.workflow_steps

        out["OnExceptionSteps"] = (
            capo_transfer.types.workflow_steps.serialize_aws_json_1_1(
                value["on_exception_steps"]
            )
        )
    if "workflow_id" in value:
        out["WorkflowId"] = value["workflow_id"]
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "structured_log_destinations" in value:
        import capo_transfer.types.structured_log_destinations

        out["StructuredLogDestinations"] = (
            capo_transfer.types.structured_log_destinations.serialize_aws_json_1_1(
                value["structured_log_destinations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedWorkflow:
    out: DescribedWorkflow = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedWorkflow.arn required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Steps") is not None:
        import capo_transfer.types.workflow_steps

        out["steps"] = capo_transfer.types.workflow_steps.deserialize_aws_json_1_1(
            data["Steps"]
        )
    if data.get("OnExceptionSteps") is not None:
        import capo_transfer.types.workflow_steps

        out["on_exception_steps"] = (
            capo_transfer.types.workflow_steps.deserialize_aws_json_1_1(
                data["OnExceptionSteps"]
            )
        )
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("StructuredLogDestinations") is not None:
        import capo_transfer.types.structured_log_destinations

        out["structured_log_destinations"] = (
            capo_transfer.types.structured_log_destinations.deserialize_aws_json_1_1(
                data["StructuredLogDestinations"]
            )
        )
    return out
