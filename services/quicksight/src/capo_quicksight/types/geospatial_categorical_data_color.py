"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialCategoricalDataColor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color_with_transparency
    import capo_quicksight.types.string


class GeospatialCategoricalDataColor(TypedDict, closed=True):
    color: "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    """<p>The color and opacity values for the category data color.</p>"""
    data_value: "capo_quicksight.types.string.String"
    """<p>The data value for the category data color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialCategoricalDataColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    out["DataValue"] = value["data_value"]
    return out


def deserialize_json(data: dict) -> GeospatialCategoricalDataColor:
    out: GeospatialCategoricalDataColor = {}  # type: ignore[typeddict-item]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    else:
        out["color"] = ""
    if data.get("DataValue") is not None:
        out["data_value"] = data["DataValue"]
    else:
        out["data_value"] = ""
    return out
