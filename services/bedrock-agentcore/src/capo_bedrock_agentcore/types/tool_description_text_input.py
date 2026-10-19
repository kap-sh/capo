"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionTextInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.tool_description_list


class ToolDescriptionTextInput(TypedDict, closed=True):
    tools: "capo_bedrock_agentcore.types.tool_description_list.ToolDescriptionList"
    """<p>The list of tool descriptions to optimize.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionTextInput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.tool_description_list

    out["tools"] = capo_bedrock_agentcore.types.tool_description_list.serialize_json(
        value["tools"]
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionTextInput:
    out: ToolDescriptionTextInput = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_bedrock_agentcore.types.tool_description_list

        out["tools"] = (
            capo_bedrock_agentcore.types.tool_description_list.deserialize_json(
                data["tools"]
            )
        )
    else:
        out["tools"] = []
    return out


def redact_sensitive(value: ToolDescriptionTextInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tools" in value:
        import capo_bedrock_agentcore.types.tool_description_list

        out["tools"] = (
            capo_bedrock_agentcore.types.tool_description_list.redact_sensitive(
                value["tools"]
            )
        )
    return out
