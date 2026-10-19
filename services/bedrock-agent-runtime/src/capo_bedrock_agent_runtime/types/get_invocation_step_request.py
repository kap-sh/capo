"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#GetInvocationStepRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_identifier
    import capo_bedrock_agent_runtime.types.session_identifier
    import capo_bedrock_agent_runtime.types.uuid


class GetInvocationStepRequest(TypedDict, closed=True):
    invocation_identifier: (
        "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier"
    )
    """<p>The unique identifier for the invocation in UUID format.</p>"""
    invocation_step_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the specific invocation step to retrieve.</p>"""
    session_identifier: (
        "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the invocation step's associated session. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInvocationStepRequest) -> dict:
    out: dict = {}
    out["invocationIdentifier"] = value["invocation_identifier"]
    return out


def deserialize_json(data: dict) -> GetInvocationStepRequest:
    out: GetInvocationStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("invocationIdentifier") is not None:
        out["invocation_identifier"] = data["invocationIdentifier"]
    else:
        out["invocation_identifier"] = ""
    return out
