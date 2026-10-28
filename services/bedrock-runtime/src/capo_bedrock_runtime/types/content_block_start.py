"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ContentBlockStart``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.image_block_start
    import capo_bedrock_runtime.types.tool_result_block_start
    import capo_bedrock_runtime.types.tool_use_block_start


class ContentBlockStartToolUseMember(TypedDict, closed=True):
    toolUse: "capo_bedrock_runtime.types.tool_use_block_start.ToolUseBlockStart"


class ContentBlockStartToolResultMember(TypedDict, closed=True):
    toolResult: (
        "capo_bedrock_runtime.types.tool_result_block_start.ToolResultBlockStart"
    )


class ContentBlockStartImageMember(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.image_block_start.ImageBlockStart"


ContentBlockStart: TypeAlias = (
    ContentBlockStartToolUseMember
    | ContentBlockStartToolResultMember
    | ContentBlockStartImageMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlockStart) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContentBlockStart: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "toolUse" in value:
        import capo_bedrock_runtime.types.tool_use_block_start

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_start.serialize_json(
                value["toolUse"]
            )
        }
    elif "toolResult" in value:
        import capo_bedrock_runtime.types.tool_result_block_start

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_block_start.serialize_json(
                value["toolResult"]
            )
        }
    elif "image" in value:
        import capo_bedrock_runtime.types.image_block_start

        return {
            "image": capo_bedrock_runtime.types.image_block_start.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("ContentBlockStart: no variant present")


def deserialize_json(data: dict) -> ContentBlockStart:
    if data.get("toolUse") is not None:
        import capo_bedrock_runtime.types.tool_use_block_start

        return {
            "toolUse": capo_bedrock_runtime.types.tool_use_block_start.deserialize_json(
                data["toolUse"]
            )
        }
    elif data.get("toolResult") is not None:
        import capo_bedrock_runtime.types.tool_result_block_start

        return {
            "toolResult": capo_bedrock_runtime.types.tool_result_block_start.deserialize_json(
                data["toolResult"]
            )
        }
    elif data.get("image") is not None:
        import capo_bedrock_runtime.types.image_block_start

        return {
            "image": capo_bedrock_runtime.types.image_block_start.deserialize_json(
                data["image"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContentBlockStart: no recognized variant key")
