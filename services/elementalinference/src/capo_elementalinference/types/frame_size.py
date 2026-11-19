"""Generated from Smithy shape ``com.amazonaws.elementalinference#FrameSize``."""

from typing_extensions import TypedDict


class FrameSize(TypedDict, closed=True):
    width_pixels: "int"
    """<p>The width of each frame, in pixels. Valid range: 1 to 1280.</p>"""
    height_pixels: "int"
    """<p>The height of each frame, in pixels. Valid range: 1 to 720.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameSize) -> dict:
    out: dict = {}
    out["widthPixels"] = value["width_pixels"]
    out["heightPixels"] = value["height_pixels"]
    return out


def deserialize_json(data: dict) -> FrameSize:
    out: FrameSize = {}  # type: ignore[typeddict-item]
    if data.get("widthPixels") is not None:
        out["width_pixels"] = data["widthPixels"]
    else:
        out["width_pixels"] = 0
    if data.get("heightPixels") is not None:
        out["height_pixels"] = data["heightPixels"]
    else:
        out["height_pixels"] = 0
    return out
