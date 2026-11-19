"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AgentInvocationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.agent_core_runtime_invocation


class AgentInvocationConfigAgentCoreRuntimeMember(TypedDict, closed=True):
    agentCoreRuntime: "capo_bedrock_agentcore.types.agent_core_runtime_invocation.AgentCoreRuntimeInvocation"


AgentInvocationConfig: TypeAlias = (
    AgentInvocationConfigAgentCoreRuntimeMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AgentInvocationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AgentInvocationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentCoreRuntime" in value:
        import capo_bedrock_agentcore.types.agent_core_runtime_invocation

        return {
            "agentCoreRuntime": capo_bedrock_agentcore.types.agent_core_runtime_invocation.serialize_json(
                value["agentCoreRuntime"]
            )
        }
    else:
        raise SerializationError("AgentInvocationConfig: no variant present")


def deserialize_json(data: dict) -> AgentInvocationConfig:
    if data.get("agentCoreRuntime") is not None:
        import capo_bedrock_agentcore.types.agent_core_runtime_invocation

        return {
            "agentCoreRuntime": capo_bedrock_agentcore.types.agent_core_runtime_invocation.deserialize_json(
                data["agentCoreRuntime"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AgentInvocationConfig: no recognized variant key")
