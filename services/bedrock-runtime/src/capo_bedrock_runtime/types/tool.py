"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#Tool``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.cache_point_block
    import capo_bedrock_runtime.types.system_tool
    import capo_bedrock_runtime.types.tool_specification


class ToolToolSpecMember(TypedDict, closed=True):
    toolSpec: "capo_bedrock_runtime.types.tool_specification.ToolSpecification"


class ToolSystemToolMember(TypedDict, closed=True):
    systemTool: "capo_bedrock_runtime.types.system_tool.SystemTool"


class ToolCachePointMember(TypedDict, closed=True):
    cachePoint: "capo_bedrock_runtime.types.cache_point_block.CachePointBlock"


Tool: TypeAlias = (
    ToolToolSpecMember
    | ToolSystemToolMember
    | ToolCachePointMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Tool) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Tool: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "toolSpec" in value:
        import capo_bedrock_runtime.types.tool_specification

        return {
            "toolSpec": capo_bedrock_runtime.types.tool_specification.serialize_json(
                value["toolSpec"]
            )
        }
    elif "systemTool" in value:
        import capo_bedrock_runtime.types.system_tool

        return {
            "systemTool": capo_bedrock_runtime.types.system_tool.serialize_json(
                value["systemTool"]
            )
        }
    elif "cachePoint" in value:
        import capo_bedrock_runtime.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_runtime.types.cache_point_block.serialize_json(
                value["cachePoint"]
            )
        }
    else:
        raise SerializationError("Tool: no variant present")


def deserialize_json(data: dict) -> Tool:
    if data.get("toolSpec") is not None:
        import capo_bedrock_runtime.types.tool_specification

        return {
            "toolSpec": capo_bedrock_runtime.types.tool_specification.deserialize_json(
                data["toolSpec"]
            )
        }
    elif data.get("systemTool") is not None:
        import capo_bedrock_runtime.types.system_tool

        return {
            "systemTool": capo_bedrock_runtime.types.system_tool.deserialize_json(
                data["systemTool"]
            )
        }
    elif data.get("cachePoint") is not None:
        import capo_bedrock_runtime.types.cache_point_block

        return {
            "cachePoint": capo_bedrock_runtime.types.cache_point_block.deserialize_json(
                data["cachePoint"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Tool: no recognized variant key")
