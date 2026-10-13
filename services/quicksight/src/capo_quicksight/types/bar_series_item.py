"""Generated from Smithy shape ``com.amazonaws.quicksight#BarSeriesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_field_bar_series_item
    import capo_quicksight.types.field_bar_series_item


class BarSeriesItem(TypedDict, closed=True):
    field_bar_series_item: NotRequired[
        "capo_quicksight.types.field_bar_series_item.FieldBarSeriesItem"
    ]
    """<p>The field series item configuration of a <code>BarChartVisual</code>.</p>"""
    data_field_bar_series_item: NotRequired[
        "capo_quicksight.types.data_field_bar_series_item.DataFieldBarSeriesItem"
    ]
    """<p>The data field series item configuration of a <code>BarChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarSeriesItem) -> dict:
    out: dict = {}
    if "field_bar_series_item" in value:
        import capo_quicksight.types.field_bar_series_item

        out["FieldBarSeriesItem"] = (
            capo_quicksight.types.field_bar_series_item.serialize_json(
                value["field_bar_series_item"]
            )
        )
    if "data_field_bar_series_item" in value:
        import capo_quicksight.types.data_field_bar_series_item

        out["DataFieldBarSeriesItem"] = (
            capo_quicksight.types.data_field_bar_series_item.serialize_json(
                value["data_field_bar_series_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarSeriesItem:
    out: BarSeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldBarSeriesItem") is not None:
        import capo_quicksight.types.field_bar_series_item

        out["field_bar_series_item"] = (
            capo_quicksight.types.field_bar_series_item.deserialize_json(
                data["FieldBarSeriesItem"]
            )
        )
    if data.get("DataFieldBarSeriesItem") is not None:
        import capo_quicksight.types.data_field_bar_series_item

        out["data_field_bar_series_item"] = (
            capo_quicksight.types.data_field_bar_series_item.deserialize_json(
                data["DataFieldBarSeriesItem"]
            )
        )
    return out


def redact_sensitive(value: BarSeriesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_field_bar_series_item" in value:
        import capo_quicksight.types.data_field_bar_series_item

        out["data_field_bar_series_item"] = (
            capo_quicksight.types.data_field_bar_series_item.redact_sensitive(
                value["data_field_bar_series_item"]
            )
        )
    return out
