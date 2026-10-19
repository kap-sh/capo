"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialSolidColor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geospatial_color_state
    import capo_quicksight.types.hex_color_with_transparency


class GeospatialSolidColor(TypedDict, closed=True):
    color: "capo_quicksight.types.hex_color_with_transparency.HexColorWithTransparency"
    """<p>The color and opacity values for the color.</p>"""
    state: NotRequired[
        "capo_quicksight.types.geospatial_color_state.GeospatialColorState"
    ]
    """<p>Enables and disables the view state of the color.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialSolidColor) -> dict:
    out: dict = {}
    out["Color"] = value["color"]
    if "state" in value:
        import capo_quicksight.types.geospatial_color_state

        out["State"] = capo_quicksight.types.geospatial_color_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialSolidColor:
    out: GeospatialSolidColor = {}  # type: ignore[typeddict-item]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    else:
        out["color"] = ""
    if data.get("State") is not None:
        import capo_quicksight.types.geospatial_color_state

        out["state"] = capo_quicksight.types.geospatial_color_state.deserialize_json(
            data["State"]
        )
    return out
