"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualPalette``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_color_list
    import capo_quicksight.types.hex_color


class VisualPalette(TypedDict, closed=True):
    chart_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The chart color options for the visual palette.</p>"""
    color_map: NotRequired[
        "capo_quicksight.types.data_path_color_list.DataPathColorList"
    ]
    """<p>The color map options for the visual palette.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualPalette) -> dict:
    out: dict = {}
    if "chart_color" in value:
        out["ChartColor"] = value["chart_color"]
    if "color_map" in value:
        import capo_quicksight.types.data_path_color_list

        out["ColorMap"] = capo_quicksight.types.data_path_color_list.serialize_json(
            value["color_map"]
        )
    return out


def deserialize_json(data: dict) -> VisualPalette:
    out: VisualPalette = {}  # type: ignore[typeddict-item]
    if data.get("ChartColor") is not None:
        out["chart_color"] = data["ChartColor"]
    if data.get("ColorMap") is not None:
        import capo_quicksight.types.data_path_color_list

        out["color_map"] = capo_quicksight.types.data_path_color_list.deserialize_json(
            data["ColorMap"]
        )
    return out


def redact_sensitive(value: VisualPalette) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "color_map" in value:
        import capo_quicksight.types.data_path_color_list

        out["color_map"] = capo_quicksight.types.data_path_color_list.redact_sensitive(
            value["color_map"]
        )
    return out
