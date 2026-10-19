"""Generated from Smithy shape ``com.amazonaws.elementalinference#AspectRatio``."""

from typing_extensions import TypedDict


class AspectRatio(TypedDict, closed=True):
    width: "int"
    """<p>The width component of the aspect ratio (for example, 16 in a 16:9 ratio).</p>"""
    height: "int"
    """<p>The height component of the aspect ratio (for example, 9 in a 16:9 ratio).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AspectRatio) -> dict:
    out: dict = {}
    out["width"] = value["width"]
    out["height"] = value["height"]
    return out


def deserialize_json(data: dict) -> AspectRatio:
    out: AspectRatio = {}  # type: ignore[typeddict-item]
    if data.get("width") is not None:
        out["width"] = data["width"]
    else:
        out["width"] = 0
    if data.get("height") is not None:
        out["height"] = data["height"]
    else:
        out["height"] = 0
    return out
