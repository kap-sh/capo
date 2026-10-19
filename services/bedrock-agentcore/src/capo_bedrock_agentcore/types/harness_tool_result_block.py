"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlock``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_result_content_blocks
    import capo_bedrock_agentcore.types.harness_tool_use_id
    import capo_bedrock_agentcore.types.harness_tool_use_status
    import capo_bedrock_agentcore.types.harness_tool_use_type


class HarnessToolResultBlock(TypedDict, closed=True):
    tool_use_id: "capo_bedrock_agentcore.types.harness_tool_use_id.HarnessToolUseId"
    """<p>The tool use ID that this result corresponds to.</p>"""
    content: "capo_bedrock_agentcore.types.harness_tool_result_content_blocks.HarnessToolResultContentBlocks"
    """<p>The content of the tool result.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.harness_tool_use_status.HarnessToolUseStatus"
    ]
    """<p>The status of the tool execution.</p>"""
    type: NotRequired[
        "capo_bedrock_agentcore.types.harness_tool_use_type.HarnessToolUseType"
    ]
    """<p>The type of tool use that produced this result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlock) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    import capo_bedrock_agentcore.types.harness_tool_result_content_blocks

    out["content"] = (
        capo_bedrock_agentcore.types.harness_tool_result_content_blocks.serialize_json(
            value["content"]
        )
    )
    if "status" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            capo_bedrock_agentcore.types.harness_tool_use_status.serialize_json(
                value["status"]
            )
        )
    if "type" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = capo_bedrock_agentcore.types.harness_tool_use_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> HarnessToolResultBlock:
    out: HarnessToolResultBlock = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        out["tool_use_id"] = ""
    if data.get("content") is not None:
        import capo_bedrock_agentcore.types.harness_tool_result_content_blocks

        out["content"] = (
            capo_bedrock_agentcore.types.harness_tool_result_content_blocks.deserialize_json(
                data["content"]
            )
        )
    else:
        out["content"] = []
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            capo_bedrock_agentcore.types.harness_tool_use_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("type") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_type

        out["type"] = (
            capo_bedrock_agentcore.types.harness_tool_use_type.deserialize_json(
                data["type"]
            )
        )
    return out


def redact_sensitive(value: HarnessToolResultBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        import capo_bedrock_agentcore.types.harness_tool_result_content_blocks

        out["content"] = (
            capo_bedrock_agentcore.types.harness_tool_result_content_blocks.redact_sensitive(
                value["content"]
            )
        )
    return out
