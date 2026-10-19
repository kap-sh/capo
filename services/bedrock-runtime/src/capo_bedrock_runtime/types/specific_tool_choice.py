"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#SpecificToolChoice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.tool_name


class SpecificToolChoice(TypedDict, closed=True):
    name: "capo_bedrock_runtime.types.tool_name.ToolName"
    """<p>The name of the tool that the model must request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpecificToolChoice) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SpecificToolChoice:
    out: SpecificToolChoice = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
