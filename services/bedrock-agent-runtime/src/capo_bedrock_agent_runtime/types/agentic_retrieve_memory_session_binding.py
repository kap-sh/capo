"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveMemorySessionBinding``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_core_memory_actor_id
    import capo_bedrock_agent_runtime.types.agent_core_memory_session_id


class AgenticRetrieveMemorySessionBinding(TypedDict, closed=True):
    actor_id: "capo_bedrock_agent_runtime.types.agent_core_memory_actor_id.AgentCoreMemoryActorId"
    """<p>The identifier of the end user or agent that the session belongs to. This identifier scopes session history so that one actor's history is never returned for another. You are responsible for sending the correct actor value.</p>"""
    session_id: "capo_bedrock_agent_runtime.types.agent_core_memory_session_id.AgentCoreMemorySessionId"
    """<p>The identifier of the session to restore and continue. You are responsible for sending the correct session value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveMemorySessionBinding) -> dict:
    out: dict = {}
    out["actorId"] = value["actor_id"]
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveMemorySessionBinding:
    out: AgenticRetrieveMemorySessionBinding = {}  # type: ignore[typeddict-item]
    if data.get("actorId") is not None:
        out["actor_id"] = data["actorId"]
    else:
        out["actor_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
