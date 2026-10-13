"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ToolConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.tool_choice
    import capo_bedrock_agent.types.tools


class ToolConfiguration(TypedDict, closed=True):
    tools: "capo_bedrock_agent.types.tools.Tools"
    """<p>An array of tools to pass to a model.</p>"""
    tool_choice: NotRequired["capo_bedrock_agent.types.tool_choice.ToolChoice"]
    """<p>Defines which tools the model should request when invoked.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.tools

    out["tools"] = capo_bedrock_agent.types.tools.serialize_json(value["tools"])
    if "tool_choice" in value:
        import capo_bedrock_agent.types.tool_choice

        out["toolChoice"] = capo_bedrock_agent.types.tool_choice.serialize_json(
            value["tool_choice"]
        )
    return out


def deserialize_json(data: dict) -> ToolConfiguration:
    out: ToolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_bedrock_agent.types.tools

        out["tools"] = capo_bedrock_agent.types.tools.deserialize_json(data["tools"])
    else:
        raise DeserializationError("ToolConfiguration.tools required")
    if data.get("toolChoice") is not None:
        import capo_bedrock_agent.types.tool_choice

        out["tool_choice"] = capo_bedrock_agent.types.tool_choice.deserialize_json(
            data["toolChoice"]
        )
    return out


def redact_sensitive(value: ToolConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tools" in value:
        out["tools"] = "*** Sensitive Data Redacted ***"
    if "tool_choice" in value:
        out["tool_choice"] = "*** Sensitive Data Redacted ***"
    return out
