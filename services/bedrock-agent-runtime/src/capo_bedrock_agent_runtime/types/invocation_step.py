"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationStep``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.invocation_step_payload
    import capo_bedrock_agent_runtime.types.uuid


class InvocationStep(TypedDict, closed=True):
    session_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier of the session containing the invocation step.</p>"""
    invocation_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the invocation that includes the invocation step.</p>"""
    invocation_step_id: "capo_bedrock_agent_runtime.types.uuid.Uuid"
    """<p>The unique identifier (in UUID format) for the invocation step.</p>"""
    invocation_step_time: (
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp for when the invocation step was created.</p>"""
    payload: (
        "capo_bedrock_agent_runtime.types.invocation_step_payload.InvocationStepPayload"
    )
    """<p>Payload content, such as text and images, for the invocation step.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationStep) -> dict:
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
    import capo_bedrock_agent_runtime.types.invocation_step_payload

    out["payload"] = (
        capo_bedrock_agent_runtime.types.invocation_step_payload.serialize_json(
            value["payload"]
        )
    )
    return out


def deserialize_json(data: dict) -> InvocationStep:
    out: InvocationStep = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("InvocationStep.session_id required")
    if data.get("invocationId") is not None:
        out["invocation_id"] = data["invocationId"]
    else:
        raise DeserializationError("InvocationStep.invocation_id required")
    if data.get("invocationStepId") is not None:
        out["invocation_step_id"] = data["invocationStepId"]
    else:
        raise DeserializationError("InvocationStep.invocation_step_id required")
    if data.get("invocationStepTime") is not None:
        import capo_bedrock_agent_runtime.types.date_timestamp

        out["invocation_step_time"] = (
            capo_bedrock_agent_runtime.types.date_timestamp.deserialize_json(
                data["invocationStepTime"]
            )
        )
    else:
        raise DeserializationError("InvocationStep.invocation_step_time required")
    if data.get("payload") is not None:
        import capo_bedrock_agent_runtime.types.invocation_step_payload

        out["payload"] = (
            capo_bedrock_agent_runtime.types.invocation_step_payload.deserialize_json(
                data["payload"]
            )
        )
    else:
        raise DeserializationError("InvocationStep.payload required")
    return out


def redact_sensitive(value: InvocationStep) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_bedrock_agent_runtime.types.invocation_step_payload

        out["payload"] = (
            capo_bedrock_agent_runtime.types.invocation_step_payload.redact_sensitive(
                value["payload"]
            )
        )
    return out
