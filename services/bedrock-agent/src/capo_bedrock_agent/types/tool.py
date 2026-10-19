"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Tool``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError, SerializationError
from capo_bedrock_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agent.types.cache_point_block
    import capo_bedrock_agent.types.tool_specification


class _Tool_toolSpec(TypedDict, closed=True):
    toolSpec: "capo_bedrock_agent.types.tool_specification.ToolSpecification"


class _Tool_cachePoint(TypedDict, closed=True):
    cachePoint: "capo_bedrock_agent.types.cache_point_block.CachePointBlock"


Tool: TypeAlias = _Tool_toolSpec | _Tool_cachePoint | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Tool) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Tool: cannot serialize unknown variant {value.name!r}"
        )
    elif "toolSpec" in value:
        import capo_bedrock_agent.types.tool_specification

        return {
            "toolSpec": capo_bedrock_agent.types.tool_specification.serialize_json(
                value["toolSpec"]
            )
        }
    elif "cachePoint" in value:
        import capo_bedrock_agent.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_agent.types.cache_point_block.serialize_json(
                value["cachePoint"]
            )
        }
    else:
        raise SerializationError("Tool: no variant present")


def deserialize_json(data: dict) -> Tool:
    if data.get("toolSpec") is not None:
        import capo_bedrock_agent.types.tool_specification

        return {
            "toolSpec": capo_bedrock_agent.types.tool_specification.deserialize_json(
                data["toolSpec"]
            )
        }
    elif data.get("cachePoint") is not None:
        import capo_bedrock_agent.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_agent.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Tool: no recognized variant key")
