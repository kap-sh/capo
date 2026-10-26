"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PutInvocationStepRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.invocation_identifier
    import capo_bedrock_agent_runtime.types.invocation_step_payload
    import capo_bedrock_agent_runtime.types.session_identifier
    import capo_bedrock_agent_runtime.types.uuid


class PutInvocationStepRequest(TypedDict, closed=True):
    session_identifier: (
        "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier"
    )
    """<p>The unique identifier for the session to add the invocation step to. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>"""
    invocation_identifier: (
        "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier"
    )
    """<p>The unique identifier (in UUID format) of the invocation to add the invocation step to.</p>"""
    invocation_step_time: (
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp for when the invocation step occurred.</p>"""
    payload: (
        "capo_bedrock_agent_runtime.types.invocation_step_payload.InvocationStepPayload"
    )
    """<p>The payload for the invocation step, including text and images for the interaction.</p>"""
    invocation_step_id: NotRequired["capo_bedrock_agent_runtime.types.uuid.Uuid"]
    """<p>The unique identifier of the invocation step in UUID format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutInvocationStepRequest) -> dict:
    out: dict = {}
    out["invocationIdentifier"] = value["invocation_identifier"]
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
    if "invocation_step_id" in value:
        out["invocationStepId"] = value["invocation_step_id"]
    return out


def deserialize_json(data: dict) -> PutInvocationStepRequest:
    out: PutInvocationStepRequest = {}  # type: ignore[typeddict-item]
    if data.get("invocationIdentifier") is not None:
        out["invocation_identifier"] = data["invocationIdentifier"]
    else:
        out["invocation_identifier"] = ""
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
    if data.get("payload") is not None:
        import capo_bedrock_agent_runtime.types.invocation_step_payload

        out["payload"] = (
            capo_bedrock_agent_runtime.types.invocation_step_payload.deserialize_json(
                data["payload"]
            )
        )
    else:
        out["payload"] = {"$unknown": {"name": ""}}
    if data.get("invocationStepId") is not None:
        out["invocation_step_id"] = data["invocationStepId"]
    return out


def redact_sensitive(value: PutInvocationStepRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "payload" in value:
        import capo_bedrock_agent_runtime.types.invocation_step_payload

        out["payload"] = (
            capo_bedrock_agent_runtime.types.invocation_step_payload.redact_sensitive(
                value["payload"]
            )
        )
    return out
