"""Generated from Smithy shape ``com.amazonaws.quicksight#SparklinesOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.field_id
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.line_chart_marker_style_settings
    import capo_quicksight.types.line_interpolation
    import capo_quicksight.types.sparkline_axis_behavior
    import capo_quicksight.types.sparkline_visual_type


class SparklinesOptions(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the value column that the sparkline is applied to.</p>"""
    x_axis_field: "capo_quicksight.types.dimension_field.DimensionField"
    y_axis_behavior: NotRequired[
        "capo_quicksight.types.sparkline_axis_behavior.SparklineAxisBehavior"
    ]
    """<p>Determines whether the Y axis is shared across all sparklines or independent for each sparkline.</p>"""
    visual_type: NotRequired[
        "capo_quicksight.types.sparkline_visual_type.SparklineVisualType"
    ]
    """<p>The type of the sparkline. Valid values are <code>LINE</code> and <code>AREA_LINE</code>.</p>"""
    line_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the sparkline line.</p>"""
    line_interpolation: NotRequired[
        "capo_quicksight.types.line_interpolation.LineInterpolation"
    ]
    """<p>The interpolation style for the sparkline line.</p>"""
    all_points_marker: NotRequired[
        "capo_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    max_value_marker: NotRequired[
        "capo_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]
    min_value_marker: NotRequired[
        "capo_quicksight.types.line_chart_marker_style_settings.LineChartMarkerStyleSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SparklinesOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.dimension_field

    out["XAxisField"] = capo_quicksight.types.dimension_field.serialize_json(
        value["x_axis_field"]
    )
    if "y_axis_behavior" in value:
        import capo_quicksight.types.sparkline_axis_behavior

        out["YAxisBehavior"] = (
            capo_quicksight.types.sparkline_axis_behavior.serialize_json(
                value["y_axis_behavior"]
            )
        )
    if "visual_type" in value:
        import capo_quicksight.types.sparkline_visual_type

        out["VisualType"] = capo_quicksight.types.sparkline_visual_type.serialize_json(
            value["visual_type"]
        )
    if "line_color" in value:
        out["LineColor"] = value["line_color"]
    if "line_interpolation" in value:
        import capo_quicksight.types.line_interpolation

        out["LineInterpolation"] = (
            capo_quicksight.types.line_interpolation.serialize_json(
                value["line_interpolation"]
            )
        )
    if "all_points_marker" in value:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["AllPointsMarker"] = (
            capo_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["all_points_marker"]
            )
        )
    if "max_value_marker" in value:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["MaxValueMarker"] = (
            capo_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["max_value_marker"]
            )
        )
    if "min_value_marker" in value:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["MinValueMarker"] = (
            capo_quicksight.types.line_chart_marker_style_settings.serialize_json(
                value["min_value_marker"]
            )
        )
    return out


def deserialize_json(data: dict) -> SparklinesOptions:
    out: SparklinesOptions = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("SparklinesOptions.field_id required")
    if data.get("XAxisField") is not None:
        import capo_quicksight.types.dimension_field

        out["x_axis_field"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["XAxisField"]
        )
    else:
        raise DeserializationError("SparklinesOptions.x_axis_field required")
    if data.get("YAxisBehavior") is not None:
        import capo_quicksight.types.sparkline_axis_behavior

        out["y_axis_behavior"] = (
            capo_quicksight.types.sparkline_axis_behavior.deserialize_json(
                data["YAxisBehavior"]
            )
        )
    if data.get("VisualType") is not None:
        import capo_quicksight.types.sparkline_visual_type

        out["visual_type"] = (
            capo_quicksight.types.sparkline_visual_type.deserialize_json(
                data["VisualType"]
            )
        )
    if data.get("LineColor") is not None:
        out["line_color"] = data["LineColor"]
    if data.get("LineInterpolation") is not None:
        import capo_quicksight.types.line_interpolation

        out["line_interpolation"] = (
            capo_quicksight.types.line_interpolation.deserialize_json(
                data["LineInterpolation"]
            )
        )
    if data.get("AllPointsMarker") is not None:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["all_points_marker"] = (
            capo_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["AllPointsMarker"]
            )
        )
    if data.get("MaxValueMarker") is not None:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["max_value_marker"] = (
            capo_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["MaxValueMarker"]
            )
        )
    if data.get("MinValueMarker") is not None:
        import capo_quicksight.types.line_chart_marker_style_settings

        out["min_value_marker"] = (
            capo_quicksight.types.line_chart_marker_style_settings.deserialize_json(
                data["MinValueMarker"]
            )
        )
    return out


def redact_sensitive(value: SparklinesOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "x_axis_field" in value:
        import capo_quicksight.types.dimension_field

        out["x_axis_field"] = capo_quicksight.types.dimension_field.redact_sensitive(
            value["x_axis_field"]
        )
    return out
