"""Generated from Smithy shape ``com.amazonaws.qconnect#DelegateAgentConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.agent_target
    import capo_qconnect.types.multi_agent_instruction


class DelegateAgentConfiguration(TypedDict, closed=True):
    agent_target: "capo_qconnect.types.agent_target.AgentTarget"
    """<p>The collaborator agent to delegate to.</p>"""
    instruction: NotRequired[
        "capo_qconnect.types.multi_agent_instruction.MultiAgentInstruction"
    ]
    """<p>The instruction that tells the Orchestration AI Agent when and how to delegate to this collaborator agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DelegateAgentConfiguration) -> dict:
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
    return out


def deserialize_json(data: dict) -> DelegateAgentConfiguration:
    out: DelegateAgentConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("agentTarget") is not None:
        import capo_qconnect.types.agent_target

        out["agent_target"] = capo_qconnect.types.agent_target.deserialize_json(
            data["agentTarget"]
        )
    else:
        raise DeserializationError("DelegateAgentConfiguration.agent_target required")
    if data.get("instruction") is not None:
        import capo_qconnect.types.multi_agent_instruction

        out["instruction"] = (
            capo_qconnect.types.multi_agent_instruction.deserialize_json(
                data["instruction"]
            )
        )
    return out


def redact_sensitive(value: DelegateAgentConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instruction" in value:
        out["instruction"] = "*** Sensitive Data Redacted ***"
    return out
