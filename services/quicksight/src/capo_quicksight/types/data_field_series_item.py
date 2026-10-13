"""Generated from Smithy shape ``com.amazonaws.quicksight#DataFieldSeriesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.axis_binding
    import capo_quicksight.types.field_id
    import capo_quicksight.types.line_chart_series_settings
    import capo_quicksight.types.sensitive_string


class DataFieldSeriesItem(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID of the field that you are setting the axis binding to.</p>"""
    field_value: NotRequired["capo_quicksight.types.sensitive_string.SensitiveString"]
    """<p>The field value of the field that you are setting the axis binding to.</p>"""
    axis_binding: "capo_quicksight.types.axis_binding.AxisBinding"
    """<p>The axis that you are binding the field to.</p>"""
    settings: NotRequired[
        "capo_quicksight.types.line_chart_series_settings.LineChartSeriesSettings"
    ]
    """<p>The options that determine the presentation of line series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataFieldSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
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


def deserialize_json(data: dict) -> DataFieldSeriesItem:
    out: DataFieldSeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("DataFieldSeriesItem.field_id required")
    if data.get("FieldValue") is not None:
        out["field_value"] = data["FieldValue"]
    if data.get("AxisBinding") is not None:
        import capo_quicksight.types.axis_binding

        out["axis_binding"] = capo_quicksight.types.axis_binding.deserialize_json(
            data["AxisBinding"]
        )
    else:
        raise DeserializationError("DataFieldSeriesItem.axis_binding required")
    if data.get("Settings") is not None:
        import capo_quicksight.types.line_chart_series_settings

        out["settings"] = (
            capo_quicksight.types.line_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out


def redact_sensitive(value: DataFieldSeriesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_value" in value:
        out["field_value"] = "*** Sensitive Data Redacted ***"
    return out
