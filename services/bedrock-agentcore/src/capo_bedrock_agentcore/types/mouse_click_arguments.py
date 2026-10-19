"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseClickArguments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.mouse_button


class MouseClickArguments(TypedDict, closed=True):
    x: "int"
    """<p>The X coordinate on screen where the click occurs.</p>"""
    y: "int"
    """<p>The Y coordinate on screen where the click occurs.</p>"""
    button: NotRequired["capo_bedrock_agentcore.types.mouse_button.MouseButton"]
    """<p>The mouse button to use. Defaults to <code>LEFT</code>.</p>"""
    click_count: NotRequired["int"]
    """<p>The number of clicks to perform. Valid range: 1–10. Defaults to 1.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseClickArguments) -> dict:
    out: dict = {}
    out["x"] = value["x"]
    out["y"] = value["y"]
    if "button" in value:
        import capo_bedrock_agentcore.types.mouse_button

        out["button"] = capo_bedrock_agentcore.types.mouse_button.serialize_json(
            value["button"]
        )
    if "click_count" in value:
        out["clickCount"] = value["click_count"]
    return out


def deserialize_json(data: dict) -> MouseClickArguments:
    out: MouseClickArguments = {}  # type: ignore[typeddict-item]
    if data.get("x") is not None:
        out["x"] = data["x"]
    else:
        out["x"] = 0
    if data.get("y") is not None:
        out["y"] = data["y"]
    else:
        out["y"] = 0
    if data.get("button") is not None:
        import capo_bedrock_agentcore.types.mouse_button

        out["button"] = capo_bedrock_agentcore.types.mouse_button.deserialize_json(
            data["button"]
        )
    if data.get("clickCount") is not None:
        out["click_count"] = data["clickCount"]
    return out
