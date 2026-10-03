"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SendWorkflowStepActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_build_version_arn
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.workflow_step_action_type
    import capo_imagebuilder.types.workflow_step_execution_id


class SendWorkflowStepActionRequest(TypedDict, closed=True):
    step_execution_id: (
        "capo_imagebuilder.types.workflow_step_execution_id.WorkflowStepExecutionId"
    )
    """<p>Uniquely identifies the waiting workflow step that you send the action to. To get this identifier, call <a>ListWaitingWorkflowSteps</a>.</p>"""
    image_build_version_arn: (
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the image build version associated with the workflow step execution. This value must match the image that owns the waiting step. If the ARN does not correspond to the image running the workflow, then the request fails with a validation error.</p>"""
    action: "capo_imagebuilder.types.workflow_step_action_type.WorkflowStepActionType"
    """<p>The action to perform on the paused workflow step. <code>RESUME</code> completes the waiting step, and the workflow continues. <code>STOP</code> fails the step, and the step's <code>onFailure</code> setting determines whether the workflow continues or aborts. The workflow step must be in a waiting state to accept an action. The request fails if the step has already timed out or been actioned.</p>"""
    reason: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The reason for the action. This value is stored with the step execution record and is accessible in subsequent workflow steps via step output references.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendWorkflowStepActionRequest) -> dict:
    out: dict = {}
    out["stepExecutionId"] = value["step_execution_id"]
    out["imageBuildVersionArn"] = value["image_build_version_arn"]
    import capo_imagebuilder.types.workflow_step_action_type

    out["action"] = capo_imagebuilder.types.workflow_step_action_type.serialize_json(
        value["action"]
    )
    if "reason" in value:
        out["reason"] = value["reason"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendWorkflowStepActionRequest:
    out: SendWorkflowStepActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("stepExecutionId") is not None:
        out["step_execution_id"] = data["stepExecutionId"]
    else:
        raise DeserializationError(
            "SendWorkflowStepActionRequest.step_execution_id required"
        )
    if data.get("imageBuildVersionArn") is not None:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    else:
        raise DeserializationError(
            "SendWorkflowStepActionRequest.image_build_version_arn required"
        )
    if data.get("action") is not None:
        import capo_imagebuilder.types.workflow_step_action_type

        out["action"] = (
            capo_imagebuilder.types.workflow_step_action_type.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("SendWorkflowStepActionRequest.action required")
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "SendWorkflowStepActionRequest.client_token required"
        )
    return out
