"""Generated from Smithy shape ``com.amazonaws.transfer#SendWorkflowStepStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.callback_token
    import capo_transfer.types.custom_step_status
    import capo_transfer.types.execution_id
    import capo_transfer.types.workflow_id


class SendWorkflowStepStateRequest(TypedDict, closed=True):
    workflow_id: "capo_transfer.types.workflow_id.WorkflowId"
    """<p>A unique identifier for the workflow.</p>"""
    execution_id: "capo_transfer.types.execution_id.ExecutionId"
    """<p>A unique identifier for the execution of a workflow.</p>"""
    token: "capo_transfer.types.callback_token.CallbackToken"
    """<p>Used to distinguish between multiple callbacks for multiple Lambda steps within the same execution.</p>"""
    status: "capo_transfer.types.custom_step_status.CustomStepStatus"
    """<p>Indicates whether the specified step succeeded or failed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendWorkflowStepStateRequest) -> dict:
    out: dict = {}
    out["WorkflowId"] = value["workflow_id"]
    out["ExecutionId"] = value["execution_id"]
    out["Token"] = value["token"]
    import capo_transfer.types.custom_step_status

    out["Status"] = capo_transfer.types.custom_step_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendWorkflowStepStateRequest:
    out: SendWorkflowStepStateRequest = {}  # type: ignore[typeddict-item]
    if data.get("WorkflowId") is not None:
        out["workflow_id"] = data["WorkflowId"]
    else:
        out["workflow_id"] = ""
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    else:
        out["execution_id"] = ""
    if data.get("Token") is not None:
        out["token"] = data["Token"]
    else:
        out["token"] = ""
    if data.get("Status") is not None:
        import capo_transfer.types.custom_step_status

        out["status"] = capo_transfer.types.custom_step_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_transfer.types.custom_step_status.CustomStepStatus", ""
        )
    return out
