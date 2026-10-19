"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldSeriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.axis_binding
    import capo_quicksight.types.field_id
    import capo_quicksight.types.line_chart_series_settings


class FieldSeriesItem(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the field for which you are setting the axis binding.</p>"""
    axis_binding: "capo_quicksight.types.axis_binding.AxisBinding"
    """<p>The axis that you are binding the field to.</p>"""
    settings: NotRequired[
        "capo_quicksight.types.line_chart_series_settings.LineChartSeriesSettings"
    ]
    """<p>The options that determine the presentation of line series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import capo_quicksight.types.axis_binding

    out["AxisBinding"] = capo_quicksight.types.axis_binding.serialize_json(
        value["axis_binding"]
    )
    if "settings" in value:
        import capo_quicksight.types.line_chart_series_settings

        out["Settings"] = (
            capo_quicksight.types.line_chart_series_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldSeriesItem:
    out: FieldSeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("AxisBinding") is not None:
        import capo_quicksight.types.axis_binding

        out["axis_binding"] = capo_quicksight.types.axis_binding.deserialize_json(
            data["AxisBinding"]
        )
    else:
        import typing

        out["axis_binding"] = typing.cast(
            "capo_quicksight.types.axis_binding.AxisBinding", ""
        )
    if data.get("Settings") is not None:
        import capo_quicksight.types.line_chart_series_settings

        out["settings"] = (
            capo_quicksight.types.line_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out
