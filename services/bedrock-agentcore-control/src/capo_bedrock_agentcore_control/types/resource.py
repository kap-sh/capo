"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Resource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn


class ResourceArnMember(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"


Resource: TypeAlias = ResourceArnMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Resource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Resource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "arn" in value:
        return {"arn": value["arn"]}
    else:
        raise SerializationError("Resource: no variant present")


def deserialize_json(data: dict) -> Resource:
    if data.get("arn") is not None:
        return {"arn": data["arn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Resource: no recognized variant key")
