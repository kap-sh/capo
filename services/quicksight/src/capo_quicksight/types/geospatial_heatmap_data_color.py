"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialHeatmapDataColor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color


class GeospatialHeatmapDataColor(TypedDict, closed=True):
    color: "capo_quicksight.types.hex_color.HexColor"
    """<p>The hex color to be used in the heatmap point style.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialHeatmapDataColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    return out


def deserialize_json(data: dict) -> GeospatialHeatmapDataColor:
    out: GeospatialHeatmapDataColor = {}  # type: ignore[typeddict-item]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    else:
        out["color"] = ""
    return out
