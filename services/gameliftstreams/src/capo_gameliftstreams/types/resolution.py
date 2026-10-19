"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#Resolution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.resolution_height
    import capo_gameliftstreams.types.resolution_width


class Resolution(TypedDict, closed=True):
    width: "capo_gameliftstreams.types.resolution_width.ResolutionWidth"
    """<p>The width of the stream session's virtual monitor, in pixels. The value must be an even number.</p>"""
    height: "capo_gameliftstreams.types.resolution_height.ResolutionHeight"
    """<p>The height of the stream session's virtual monitor, in pixels. The value must be an even number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Resolution) -> dict:
    out: dict = {}
    out["Width"] = value["width"]
    out["Height"] = value["height"]
    return out


def deserialize_json(data: dict) -> Resolution:
    out: Resolution = {}  # type: ignore[typeddict-item]
    if data.get("Width") is not None:
        out["width"] = data["Width"]
    else:
        out["width"] = 0
    if data.get("Height") is not None:
        out["height"] = data["Height"]
    else:
        out["height"] = 0
    return out
