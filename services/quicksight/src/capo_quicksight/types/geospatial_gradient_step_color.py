"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialGradientStepColor``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.hex_color_with_transparency


class GeospatialGradientStepColor(TypedDict, closed=True):
    color: "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    """<p>The color and opacity values for the gradient step color.</p>"""
    data_value: "capo_quicksight.types.double.Double"
    """<p>The data value for the gradient step color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialGradientStepColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    out["DataValue"] = (
        "NaN"
        if value.get("data_value", 0) != value.get("data_value", 0)
        else "Infinity"
        if value.get("data_value", 0) == float("inf")
        else "-Infinity"
        if value.get("data_value", 0) == float("-inf")
        else value.get("data_value", 0)
    )
    return out


def deserialize_json(data: dict) -> GeospatialGradientStepColor:
    out: GeospatialGradientStepColor = {}  # type: ignore[typeddict-item]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    else:
        out["color"] = ""
    if data.get("DataValue") is not None:
        out["data_value"] = float(data["DataValue"])
    else:
        out["data_value"] = 0
    return out
