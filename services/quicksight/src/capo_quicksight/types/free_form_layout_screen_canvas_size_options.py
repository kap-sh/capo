"""Generated from Smithy shape ``com.amazonaws.quicksight#FreeFormLayoutScreenCanvasSizeOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.pixel_length


class FreeFormLayoutScreenCanvasSizeOptions(TypedDict, closed=True):
    optimized_view_port_width: "capo_quicksight.types.pixel_length.PixelLength"
    """<p>The width that the view port will be optimized for when the layout renders.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FreeFormLayoutScreenCanvasSizeOptions) -> dict:
    out: dict = {}
    out["OptimizedViewPortWidth"] = value["optimized_view_port_width"]
    return out


def deserialize_json(data: dict) -> FreeFormLayoutScreenCanvasSizeOptions:
    out: FreeFormLayoutScreenCanvasSizeOptions = {}  # type: ignore[typeddict-item]
    if data.get("OptimizedViewPortWidth") is not None:
        out["optimized_view_port_width"] = data["OptimizedViewPortWidth"]
    else:
        out["optimized_view_port_width"] = ""
    return out
