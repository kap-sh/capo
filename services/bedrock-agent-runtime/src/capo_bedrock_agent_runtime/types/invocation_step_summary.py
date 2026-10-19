"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStepSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.uuid


class InvocationStepSummary(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier for the session associated with the invocation step.</p>"""
    invocation_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>A unique identifier for the invocation in UUID format.</p>"""
    invocation_step_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the invocation step.</p>"""
    invocation_step_time: (
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp for when the invocation step was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStepSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["invocationId"] = value["invocation_id"]
    out["invocationStepId"] = value["invocation_step_id"]
    import capo_bedrock_agent_runtime.types.date_timestamp

    out["invocationStepTime"] = (
        capo_bedrock_agent_runtime.types.date_timestamp.serialize_json(
            value["invocation_step_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvocationStepSummary:
    out: InvocationStepSummary = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    else:
        out["invocation_id"] = ""
    if data.get("invocationStepId") is not None:
        out["invocation_step_id"] = data["invocationStepId"]
    else:
        out["invocation_step_id"] = ""
    if data.get("invocationStepTime") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["invocation_step_time"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["invocationStepTime"]
            )
        )
    else:
        import datetime

        out["invocation_step_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
