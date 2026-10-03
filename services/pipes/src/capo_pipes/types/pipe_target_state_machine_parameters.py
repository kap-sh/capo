"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetStateMachineParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_target_invocation_type


class PipeTargetStateMachineParameters(TypedDict, closed=True):
    invocation_type: NotRequired[
        "capo_pipes.types.pipe_target_invocation_type.PipeTargetInvocationType"
    ]
    """<p>Specify whether to invoke the Step Functions state machine synchronously or asynchronously.</p> <ul> <li> <p> <code>REQUEST_RESPONSE</code> (default) - Invoke synchronously. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartSyncExecution.html">StartSyncExecution</a> in the <i>Step Functions API Reference</i>.</p> <note> <p> <code>REQUEST_RESPONSE</code> is not supported for <code>STANDARD</code> state machine workflows.</p> </note> </li> <li> <p> <code>FIRE_AND_FORGET</code> - Invoke asynchronously. For more information, see <a href="https://docs.aws.amazon.com/step-functions/latest/apireference/API_StartExecution.html">StartExecution</a> in the <i>Step Functions API Reference</i>.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation">Invocation types</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetStateMachineParameters) -> dict:
    out: dict = {}
    if "invocation_type" in value:
        out["InvocationType"] = value["invocation_type"]
    return out


def deserialize_json(data: dict) -> PipeTargetStateMachineParameters:
    out: PipeTargetStateMachineParameters = {}  # type: ignore[typeddict-item]
    if data.get("InvocationType") is not None:
        out["invocation_type"] = data["InvocationType"]
    return out
