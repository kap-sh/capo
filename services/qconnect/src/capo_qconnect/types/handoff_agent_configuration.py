"""Generated from Smithy shape ``com.amazonaws.qconnect#HandoffAgentConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.agent_target
    import capo_qconnect.types.multi_agent_instruction


class HandoffAgentConfiguration(TypedDict, closed=True):
    agent_target: "capo_qconnect.types.agent_target.AgentTarget"
    """<p>The collaborator agent to hand off to.</p>"""
    instruction: NotRequired[
        "capo_qconnect.types.multi_agent_instruction.MultiAgentInstruction"
    ]
    """<p>The instruction that tells the Orchestration AI Agent when and how to hand off to this collaborator agent.</p>"""
    audio_streaming_enabled: NotRequired["bool"]
    """<p>Specifies whether the caller's audio is streamed directly to the collaborator agent and the collaborator's audio response is played back during the handoff. This applies only to voice handoffs.</p>"""
    immediate_handoff: NotRequired["bool"]
    """<p>Specifies whether the conversation is handed off to this collaborator agent immediately on the first turn, without any orchestration reasoning. At most one handoff in an AI Agent's configuration can set this to <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HandoffAgentConfiguration) -> dict:
    out: dict = {}
    import capo_qconnect.types.agent_target

    out["agentTarget"] = capo_qconnect.types.agent_target.serialize_json(
        value["agent_target"]
    )
    if "instruction" in value:
        import capo_qconnect.types.multi_agent_instruction

        out["instruction"] = capo_qconnect.types.multi_agent_instruction.serialize_json(
            value["instruction"]
        )
    if "audio_streaming_enabled" in value:
        out["audioStreamingEnabled"] = value["audio_streaming_enabled"]
    if "immediate_handoff" in value:
        out["immediateHandoff"] = value["immediate_handoff"]
    return out


def deserialize_json(data: dict) -> HandoffAgentConfiguration:
    out: HandoffAgentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("agentTarget") is not None:
        import capo_qconnect.types.agent_target

        out["agent_target"] = capo_qconnect.types.agent_target.deserialize_json(
            data["agentTarget"]
        )
    else:
        out["agent_target"] = {"$unknown": {"name": ""}}
    if data.get("instruction") is not None:
        import capo_qconnect.types.multi_agent_instruction

        out["instruction"] = (
            capo_qconnect.types.multi_agent_instruction.deserialize_json(
                data["instruction"]
            )
        )
    if data.get("audioStreamingEnabled") is not None:
        out["audio_streaming_enabled"] = data["audioStreamingEnabled"]
    if data.get("immediateHandoff") is not None:
        out["immediate_handoff"] = data["immediateHandoff"]
    return out


def redact_sensitive(value: HandoffAgentConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    return out
