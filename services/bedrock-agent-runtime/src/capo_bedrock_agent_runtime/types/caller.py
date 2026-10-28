"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Caller``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_arn


class CallerAgentAliasArnMember(TypedDict, closed=True):
    agentAliasArn: "capo_bedrock_agent_runtime.types.agent_alias_arn.AgentAliasArn"


Caller: TypeAlias = CallerAgentAliasArnMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Caller) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Caller: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "agentAliasArn" in value:
        return {"agentAliasArn": value["agentAliasArn"]}
    else:
        raise SerializationError("Caller: no variant present")


def deserialize_json(data: dict) -> Caller:
    if data.get("agentAliasArn") is not None:
        return {"agentAliasArn": data["agentAliasArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Caller: no recognized variant key")
