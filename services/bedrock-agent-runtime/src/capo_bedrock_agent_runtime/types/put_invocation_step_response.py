"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PutInvocationStepResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.uuid


class PutInvocationStepResponse(TypedDict, closed=True):
    invocation_step_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier of the invocation step in UUID format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInvocationStepResponse) -> dict:
    out: dict = {}
    out["invocationStepId"] = value["invocation_step_id"]
    return out


def deserialize_json(data: dict) -> PutInvocationStepResponse:
    out: PutInvocationStepResponse = {}  # type: ignore[typeddict-item]
    if data.get("invocationStepId") is not None:
        out["invocation_step_id"] = data["invocationStepId"]
    else:
        out["invocation_step_id"] = ""
    return out
