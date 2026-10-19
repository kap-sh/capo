"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlockStart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.harness_tool_use_id
    import capo_bedrock_agentcore.types.harness_tool_use_status


class HarnessToolResultBlockStart(TypedDict, closed=True):
    tool_use_id: "capo_bedrock_agentcore.types.harness_tool_use_id.HarnessToolUseId"
    """<p>The tool use ID that this result corresponds to.</p>"""
    status: NotRequired[
        "capo_bedrock_agentcore.types.harness_tool_use_status.HarnessToolUseStatus"
    ]
    """<p>The status of the tool execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlockStart) -> dict:
    out: dict = {}
    out["toolUseId"] = value["tool_use_id"]
    if "status" in value:
        import capo_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            capo_bedrock_agentcore.types.harness_tool_use_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessToolResultBlockStart:
    out: HarnessToolResultBlockStart = {}  # type: ignore[typeddict-item]
    if data.get("toolUseId") is not None:
        out["tool_use_id"] = data["toolUseId"]
    else:
        out["tool_use_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.harness_tool_use_status

        out["status"] = (
            capo_bedrock_agentcore.types.harness_tool_use_status.deserialize_json(
                data["status"]
            )
        )
    return out
