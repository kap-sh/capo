"""Generated from Smithy shape ``com.amazonaws.transfer#WorkflowDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.on_partial_upload_workflow_details
    import capo_transfer.types.on_upload_workflow_details


class WorkflowDetails(TypedDict, closed=True):
    on_upload: NotRequired[
        "capo_transfer.types.on_upload_workflow_details.OnUploadWorkflowDetails"
    ]
    """<p>A trigger that starts a workflow: the workflow begins to execute after a file is uploaded.</p> <p>To remove an associated workflow from a server, you can provide an empty <code>OnUpload</code> object, as in the following example.</p> <p> <code>aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'</code> </p> <note> <p> <code>OnUpload</code> can contain a maximum of one <code>WorkflowDetail</code> object.</p> </note>"""
    on_partial_upload: NotRequired[
        "capo_transfer.types.on_partial_upload_workflow_details.OnPartialUploadWorkflowDetails"
    ]
    """<p>A trigger that starts a workflow if a file is only partially uploaded. You can attach a workflow to a server that executes whenever there is a partial upload.</p> <p>A <i>partial upload</i> occurs when a file is open when the session disconnects.</p> <note> <p> <code>OnPartialUpload</code> can contain a maximum of one <code>WorkflowDetail</code> object.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkflowDetails) -> dict:
    out: dict = {}
    if "on_upload" in value:
        import capo_transfer.types.on_upload_workflow_details

        out["OnUpload"] = (
            capo_transfer.types.on_upload_workflow_details.serialize_aws_json_1_1(
                value["on_upload"]
            )
        )
    if "on_partial_upload" in value:
        import capo_transfer.types.on_partial_upload_workflow_details

        out["OnPartialUpload"] = (
            capo_transfer.types.on_partial_upload_workflow_details.serialize_aws_json_1_1(
                value["on_partial_upload"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkflowDetails:
    out: WorkflowDetails = {}  # type: ignore[typeddict-item]
    if data.get("OnUpload") is not None:
        import capo_transfer.types.on_upload_workflow_details

        out["on_upload"] = (
            capo_transfer.types.on_upload_workflow_details.deserialize_aws_json_1_1(
                data["OnUpload"]
            )
        )
    if data.get("OnPartialUpload") is not None:
        import capo_transfer.types.on_partial_upload_workflow_details

        out["on_partial_upload"] = (
            capo_transfer.types.on_partial_upload_workflow_details.deserialize_aws_json_1_1(
                data["OnPartialUpload"]
            )
        )
    return out
