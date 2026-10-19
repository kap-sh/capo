"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MouseScrollArguments``."""

from typing_extensions import NotRequired, TypedDict


class MouseScrollArguments(TypedDict, closed=True):
    x: "int"
    """<p>The X coordinate on screen where the scroll occurs.</p>"""
    y: "int"
    """<p>The Y coordinate on screen where the scroll occurs.</p>"""
    delta_x: NotRequired["int"]
    """<p>The horizontal scroll delta. Valid range: -1000 to 1000.</p>"""
    delta_y: NotRequired["int"]
    """<p>The vertical scroll delta. Valid range: -1000 to 1000. Negative values scroll down.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MouseScrollArguments) -> dict:
    out: dict = {}
    out["x"] = value["x"]
    out["y"] = value["y"]
    if "delta_x" in value:
        out["deltaX"] = value["delta_x"]
    if "delta_y" in value:
        out["deltaY"] = value["delta_y"]
    return out


def deserialize_json(data: dict) -> MouseScrollArguments:
    out: MouseScrollArguments = {}  # type: ignore[typeddict-item]
    if data.get("x") is not None:
        out["x"] = data["x"]
    else:
        out["x"] = 0
    if data.get("y") is not None:
        out["y"] = data["y"]
    else:
        out["y"] = 0
    if data.get("deltaX") is not None:
        out["delta_x"] = data["deltaX"]
    if data.get("deltaY") is not None:
        out["delta_y"] = data["deltaY"]
    return out
