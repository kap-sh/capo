"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetLambdaFunctionParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_target_invocation_type


class PipeTargetLambdaFunctionParameters(TypedDict, closed=True):
    invocation_type: NotRequired[
        "capo_pipes.types.pipe_target_invocation_type.PipeTargetInvocationType"
    ]
    """<p>Specify whether to invoke the function synchronously or asynchronously.</p> <ul> <li> <p> <code>REQUEST_RESPONSE</code> (default) - Invoke synchronously. This corresponds to the <code>RequestResponse</code> option in the <code>InvocationType</code> parameter for the Lambda <a href="https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax">Invoke</a> API.</p> </li> <li> <p> <code>FIRE_AND_FORGET</code> - Invoke asynchronously. This corresponds to the <code>Event</code> option in the <code>InvocationType</code> parameter for the Lambda <a href="https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax">Invoke</a> API.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes.html#pipes-invocation">Invocation types</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetLambdaFunctionParameters) -> dict:
    out: dict = {}
    if "invocation_type" in value:
        out["InvocationType"] = value["invocation_type"]
    return out


def deserialize_json(data: dict) -> PipeTargetLambdaFunctionParameters:
    out: PipeTargetLambdaFunctionParameters = {}  # type: ignore[typeddict-item]
    if data.get("InvocationType") is not None:
        out["invocation_type"] = data["InvocationType"]
    return out
