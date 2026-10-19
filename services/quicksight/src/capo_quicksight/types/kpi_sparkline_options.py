"""Generated from Smithy shape ``com.amazonaws.quicksight#KPISparklineOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.kpi_sparkline_type
    import capo_quicksight.types.visibility


class KPISparklineOptions(TypedDict, closed=True):
    visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The visibility of the sparkline.</p>"""
    type: "capo_quicksight.types.kpi_sparkline_type.KPISparklineType"
    """<p>The type of the sparkline.</p>"""
    color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the sparkline.</p>"""
    tooltip_visibility: NotRequired["capo_quicksight.types.visibility.Visibility"]
    """<p>The tooltip visibility of the sparkline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPISparklineOptions) -> dict:
    out: dict = {}
    if "visibility" in value:
        import capo_quicksight.types.visibility

        out["Visibility"] = capo_quicksight.types.visibility.serialize_json(
            value["visibility"]
        )
    import capo_quicksight.types.kpi_sparkline_type

    out["Type"] = capo_quicksight.types.kpi_sparkline_type.serialize_json(value["type"])
    if "color" in value:
        out["Color"] = value["color"]
    if "tooltip_visibility" in value:
        import capo_quicksight.types.visibility

        out["TooltipVisibility"] = capo_quicksight.types.visibility.serialize_json(
            value["tooltip_visibility"]
        )
    return out


def deserialize_json(data: dict) -> KPISparklineOptions:
    out: KPISparklineOptions = {}  # type: ignore[typeddict-item]
    if data.get("Visibility") is not None:
        import capo_quicksight.types.visibility

        out["visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if data.get("Type") is not None:
        import capo_quicksight.types.kpi_sparkline_type

        out["type"] = capo_quicksight.types.kpi_sparkline_type.deserialize_json(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.kpi_sparkline_type.KPISparklineType", ""
        )
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    if data.get("TooltipVisibility") is not None:
        import capo_quicksight.types.visibility

        out["tooltip_visibility"] = capo_quicksight.types.visibility.deserialize_json(
            data["TooltipVisibility"]
        )
    return out
