"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.recommendation_tool_name
    import capo_bedrock_agentcore.types.tool_description_config


class ToolDescriptionInput(TypedDict, closed=True):
    tool_name: (
        "capo_bedrock_agentcore.types.recommendation_tool_name.RecommendationToolName"
    )
    """<p>The name of the tool.</p>"""
    tool_description: (
        "capo_bedrock_agentcore.types.tool_description_config.ToolDescriptionConfig"
    )
    """<p>The current description of the tool to optimize.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionInput) -> dict:
    out: dict = {}
    out["toolName"] = value["tool_name"]
    import capo_bedrock_agentcore.types.tool_description_config

    out["toolDescription"] = (
        capo_bedrock_agentcore.types.tool_description_config.serialize_json(
            value["tool_description"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionInput:
    out: ToolDescriptionInput = {}  # type: ignore[typeddict-item]
    if data.get("toolName") is not None:
        out["tool_name"] = data["toolName"]
    else:
        raise DeserializationError("ToolDescriptionInput.tool_name required")
    if data.get("toolDescription") is not None:
        import capo_bedrock_agentcore.types.tool_description_config

        out["tool_description"] = (
            capo_bedrock_agentcore.types.tool_description_config.deserialize_json(
                data["toolDescription"]
            )
        )
    else:
        raise DeserializationError("ToolDescriptionInput.tool_description required")
    return out


def redact_sensitive(value: ToolDescriptionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tool_description" in value:
        import capo_bedrock_agentcore.types.tool_description_config

        out["tool_description"] = (
            capo_bedrock_agentcore.types.tool_description_config.redact_sensitive(
                value["tool_description"]
            )
        )
    return out
