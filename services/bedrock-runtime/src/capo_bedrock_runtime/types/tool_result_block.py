"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolResultBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_result_content_blocks
    import capo_bedrock_runtime.types.tool_result_status
    import capo_bedrock_runtime.types.tool_use_id


class ToolResultBlock(TypedDict, closed=True):
    tool_use_id: "capo_bedrock_runtime.types.tool_use_id.ToolUseId"
    """<p>The ID of the tool request that this is the result for. </p>"""
    content: (
        "capo_bedrock_runtime.types.tool_result_content_blocks.ToolResultContentBlocks"
    )
    """<p>The content for tool result content block.</p>"""
    status: NotRequired[
        "capo_bedrock_runtime.types.tool_result_status.ToolResultStatus"
    ]
    """<p>The status for the tool result content block.</p> <note> <p>This field is only supported by Amazon Nova and Anthropic Claude 3 and 4 models.</p> </note>"""
    type: NotRequired["str"]
    """<p>The type for the tool result content block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolResultBlock) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    import capo_bedrock_runtime.types.tool_result_content_blocks

    out["content"] = (
        capo_bedrock_runtime.types.tool_result_content_blocks.serialize_json(
            value["content"]
        )
    )
    if "status" in value:
        import capo_bedrock_runtime.types.tool_result_status

        out["status"] = capo_bedrock_runtime.types.tool_result_status.serialize_json(
            value["status"]
        )
    if "type" in value:
        out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ToolResultBlock:
    out: ToolResultBlock = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        raise DeserializationError("ToolResultBlock.tool_use_id required")
    if data.get("content") is not None:
        import capo_bedrock_runtime.types.tool_result_content_blocks

        out["content"] = (
            capo_bedrock_runtime.types.tool_result_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("ToolResultBlock.content required")
    if data.get("status") is not None:
        import capo_bedrock_runtime.types.tool_result_status

        out["status"] = capo_bedrock_runtime.types.tool_result_status.deserialize_json(
            data["status"]
        )
    if data.get("type") is not None:
        out["type"] = data["type"]
    return out


def redact_sensitive(value: ToolResultBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_runtime.types.tool_result_content_blocks

        out["content"] = (
            capo_bedrock_runtime.types.tool_result_content_blocks.redact_sensitive(
                value["content"]
            )
        )
    return out
