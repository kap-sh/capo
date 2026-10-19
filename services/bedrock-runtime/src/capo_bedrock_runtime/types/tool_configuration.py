"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_choice
    import capo_bedrock_runtime.types.tools


class ToolConfiguration(TypedDict, closed=True):
    tools: "capo_bedrock_runtime.types.tools.Tools"
    """<p>An array of tools that you want to pass to a model. </p>"""
    tool_choice: NotRequired["capo_bedrock_runtime.types.tool_choice.ToolChoice"]
    """<p>If supported by model, forces the model to request a tool. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.tools

    out["tools"] = capo_bedrock_runtime.types.tools.serialize_json(value["tools"])
    if "tool_choice" in value:
        import capo_bedrock_runtime.types.tool_choice

        out["toolChoice"] = capo_bedrock_runtime.types.tool_choice.serialize_json(
            value["tool_choice"]
        )
    return out


def deserialize_json(data: dict) -> ToolConfiguration:
    out: ToolConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("tools") is not None:
        import capo_bedrock_runtime.types.tools

        out["tools"] = capo_bedrock_runtime.types.tools.deserialize_json(data["tools"])
    else:
        out["tools"] = []
    if data.get("toolChoice") is not None:
        import capo_bedrock_runtime.types.tool_choice

        out["tool_choice"] = capo_bedrock_runtime.types.tool_choice.deserialize_json(
            data["toolChoice"]
        )
    return out
