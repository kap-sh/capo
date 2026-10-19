"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptGenAiResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.prompt_agent_resource


class _PromptGenAiResource_agent(TypedDict, closed=True):
    agent: "capo_bedrock_agent.types.prompt_agent_resource.PromptAgentResource"


PromptGenAiResource: TypeAlias = _PromptGenAiResource_agent | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: PromptGenAiResource) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PromptGenAiResource: cannot serialize unknown variant {value.name!r}"
        )
    elif "agent" in value:
        import capo_bedrock_agent.types.prompt_agent_resource

        return {
            "agent": capo_bedrock_agent.types.prompt_agent_resource.serialize_json(
                value["agent"]
            )
        }
    else:
        raise SerializationError("PromptGenAiResource: no variant present")


def deserialize_json(data: dict) -> PromptGenAiResource:
    if data.get("agent") is not None:
        import capo_bedrock_agent.types.prompt_agent_resource

        return {
            "agent": capo_bedrock_agent.types.prompt_agent_resource.deserialize_json(
                data["agent"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PromptGenAiResource: no recognized variant key")
