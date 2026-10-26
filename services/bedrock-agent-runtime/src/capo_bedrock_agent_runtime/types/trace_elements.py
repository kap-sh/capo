"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TraceElements``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_traces


class _TraceElements_agentTraces(TypedDict, closed=True):
    agentTraces: "capo_bedrock_agent_runtime.types.agent_traces.AgentTraces"


TraceElements: TypeAlias = _TraceElements_agentTraces | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TraceElements) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TraceElements: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentTraces" in value:
        import capo_bedrock_agent_runtime.types.agent_traces

        return {
            "agentTraces": capo_bedrock_agent_runtime.types.agent_traces.serialize_json(
                value["agentTraces"]
            )
        }
    else:
        raise SerializationError("TraceElements: no variant present")


def deserialize_json(data: dict) -> TraceElements:
    if data.get("agentTraces") is not None:
        import capo_bedrock_agent_runtime.types.agent_traces

        return {
            "agentTraces": capo_bedrock_agent_runtime.types.agent_traces.deserialize_json(
                data["agentTraces"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TraceElements: no recognized variant key")
