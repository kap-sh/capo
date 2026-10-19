"""Generated from Smithy shape ``com.amazonaws.quicksight#DataFieldBarSeriesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.bar_chart_series_settings
    import capo_quicksight.types.field_id
    import capo_quicksight.types.sensitive_string


class DataFieldBarSeriesItem(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>Field ID of the field that you are setting the series configuration for.</p>"""
    field_value: NotRequired["capo_quicksight.types.sensitive_string.SensitiveString"]
    """<p>Field value of the field that you are setting the series configuration for.</p>"""
    settings: NotRequired[
        "capo_quicksight.types.bar_chart_series_settings.BarChartSeriesSettings"
    ]
    """<p>Options that determine the presentation of bar series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataFieldBarSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    if "settings" in value:
        import capo_quicksight.types.bar_chart_series_settings

        out["Settings"] = (
            capo_quicksight.types.bar_chart_series_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataFieldBarSeriesItem:
    out: DataFieldBarSeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("FieldValue") is not None:
        out["field_value"] = data["FieldValue"]
    if data.get("Settings") is not None:
        import capo_quicksight.types.bar_chart_series_settings

        out["settings"] = (
            capo_quicksight.types.bar_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out


def redact_sensitive(value: DataFieldBarSeriesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_value" in value:
        out["field_value"] = "*** Sensitive Data Redacted ***"
    return out
