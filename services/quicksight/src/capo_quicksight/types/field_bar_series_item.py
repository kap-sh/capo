"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldBarSeriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.bar_chart_series_settings
    import capo_quicksight.types.field_id


class FieldBarSeriesItem(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>Field ID of the field for which you are setting the series configuration.</p>"""
    settings: NotRequired[
        "capo_quicksight.types.bar_chart_series_settings.BarChartSeriesSettings"
    ]
    """<p>Options that determine the presentation of bar series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldBarSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "settings" in value:
        import capo_quicksight.types.bar_chart_series_settings

        out["Settings"] = (
            capo_quicksight.types.bar_chart_series_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldBarSeriesItem:
    out: FieldBarSeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("Settings") is not None:
        import capo_quicksight.types.bar_chart_series_settings

        out["settings"] = (
            capo_quicksight.types.bar_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out
