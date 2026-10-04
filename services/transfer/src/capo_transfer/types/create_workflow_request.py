"""Generated from Smithy shape ``com.amazonaws.transfer#CreateWorkflowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.structured_log_destinations
    import capo_transfer.types.tags
    import capo_transfer.types.workflow_description
    import capo_transfer.types.workflow_steps


class CreateWorkflowRequest(TypedDict, closed=True):
    description: NotRequired[
        "capo_transfer.types.workflow_description.WorkflowDescription"
    ]
    """<p>A textual description for the workflow.</p>"""
    steps: "capo_transfer.types.workflow_steps.WorkflowSteps"
    """<p>Specifies the details for the steps that are in the specified workflow.</p> <p> The <code>TYPE</code> specifies which of the following actions is being taken for this step. </p> <ul> <li> <p> <b> <code>COPY</code> </b> - Copy the file to another location.</p> </li> <li> <p> <b> <code>CUSTOM</code> </b> - Perform a custom step with an Lambda function target.</p> </li> <li> <p> <b> <code>DECRYPT</code> </b> - Decrypt a file that was encrypted before it was uploaded.</p> </li> <li> <p> <b> <code>DELETE</code> </b> - Delete the file.</p> </li> <li> <p> <b> <code>TAG</code> </b> - Add a tag to the file.</p> </li> </ul> <note> <p> Currently, copying and tagging are supported only on S3. </p> </note> <p> For file location, you specify either the Amazon S3 bucket and key, or the Amazon EFS file system ID and path. </p>"""
    on_exception_steps: NotRequired["capo_transfer.types.workflow_steps.WorkflowSteps"]
    """<p>Specifies the steps (actions) to take if errors are encountered during execution of the workflow.</p> <note> <p>For custom steps, the Lambda function needs to send <code>FAILURE</code> to the call back API to kick off the exception steps. Additionally, if the Lambda does not send <code>SUCCESS</code> before it times out, the exception steps are executed.</p> </note>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</p>"""
    structured_log_destinations: NotRequired[
        "capo_transfer.types.structured_log_destinations.StructuredLogDestinations"
    ]
    """<p>Specifies the log groups to which your workflow logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:partition:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkflowRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateWorkflowRequest:
    out: CreateWorkflowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Steps") is not None:
        import capo_transfer.types.workflow_steps

        out["steps"] = capo_transfer.types.workflow_steps.deserialize_aws_json_1_1(
            data["Steps"]
        )
    else:
        raise DeserializationError("CreateWorkflowRequest.steps required")
    if data.get("OnExceptionSteps") is not None:
        import capo_transfer.types.workflow_steps

        out["on_exception_steps"] = (
            capo_transfer.types.workflow_steps.deserialize_aws_json_1_1(
                data["OnExceptionSteps"]
            )
        )
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
