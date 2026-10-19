"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ViewPort``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.view_port_height
    import capo_bedrock_agentcore.types.view_port_width


class ViewPort(TypedDict, closed=True):
    width: "capo_bedrock_agentcore.types.view_port_width.ViewPortWidth"
    """<p>The width of the viewport in pixels. This value determines the horizontal dimension of the visible area. Valid values range from 800 to 1920 pixels.</p>"""
    height: "capo_bedrock_agentcore.types.view_port_height.ViewPortHeight"
    """<p>The height of the viewport in pixels. This value determines the vertical dimension of the visible area. Valid values range from 600 to 1080 pixels.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewPort) -> dict:
    out: dict = {}
    out["width"] = value["width"]
    out["height"] = value["height"]
    return out


def deserialize_json(data: dict) -> ViewPort:
    out: ViewPort = {}  # type: ignore[typeddict-item]
    if data.get("width") is not None:
        out["width"] = data["width"]
    else:
        out["width"] = 0
    if data.get("height") is not None:
        out["height"] = data["height"]
    else:
        out["height"] = 0
    return out
