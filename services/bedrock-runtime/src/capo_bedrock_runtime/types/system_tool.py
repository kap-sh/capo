"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SystemTool``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_name


class SystemTool(TypedDict, closed=True):
    name: "capo_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the system-defined tool that you want to call. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemTool) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SystemTool:
    out: SystemTool = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
