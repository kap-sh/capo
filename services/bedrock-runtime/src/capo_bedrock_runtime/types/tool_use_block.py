"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolUseBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_name
    import capo_bedrock_runtime.types.tool_use_id
    import capo_bedrock_runtime.types.tool_use_type


class ToolUseBlock(TypedDict, closed=True):
    tool_use_id: "capo_bedrock_runtime.types.tool_use_id.ToolUseId"
    """<p>The ID for the tool request.</p>"""
    name: "capo_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the tool that the model wants to use.</p>"""
    input: "object"
    """<p>The input to pass to the tool. </p>"""
    type: NotRequired["capo_bedrock_runtime.types.tool_use_type.ToolUseType"]
    """<p>The type for the tool request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolUseBlock) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    out["name"] = value["name"]
    out["input"] = value["input"]
    if "type" in value:
        import capo_bedrock_runtime.types.tool_use_type

        out["type"] = capo_bedrock_runtime.types.tool_use_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> ToolUseBlock:
    out: ToolUseBlock = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        out["tool_use_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("input") is not None:
        out["input"] = data["input"]
    else:
        out["input"] = None
    if data.get("type") is not None:
        import capo_bedrock_runtime.types.tool_use_type

        out["type"] = capo_bedrock_runtime.types.tool_use_type.deserialize_json(
            data["type"]
        )
    return out
