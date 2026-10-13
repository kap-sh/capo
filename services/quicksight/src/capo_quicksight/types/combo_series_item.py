"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboSeriesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_field_combo_series_item
    import capo_quicksight.types.field_combo_series_item


class ComboSeriesItem(TypedDict, closed=True):
    field_combo_series_item: NotRequired[
        "capo_quicksight.types.field_combo_series_item.FieldComboSeriesItem"
    ]
    """<p>The field series item configuration of a <code>ComboChartVisual</code>.</p>"""
    data_field_combo_series_item: NotRequired[
        "capo_quicksight.types.data_field_combo_series_item.DataFieldComboSeriesItem"
    ]
    """<p>The data field series item configuration of a <code>ComboChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboSeriesItem) -> dict:
    out: dict = {}
    if "field_combo_series_item" in value:
        import capo_quicksight.types.field_combo_series_item

        out["FieldComboSeriesItem"] = (
            capo_quicksight.types.field_combo_series_item.serialize_json(
                value["field_combo_series_item"]
            )
        )
    if "data_field_combo_series_item" in value:
        import capo_quicksight.types.data_field_combo_series_item

        out["DataFieldComboSeriesItem"] = (
            capo_quicksight.types.data_field_combo_series_item.serialize_json(
                value["data_field_combo_series_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComboSeriesItem:
    out: ComboSeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldComboSeriesItem") is not None:
        import capo_quicksight.types.field_combo_series_item

        out["field_combo_series_item"] = (
            capo_quicksight.types.field_combo_series_item.deserialize_json(
                data["FieldComboSeriesItem"]
            )
        )
    if data.get("DataFieldComboSeriesItem") is not None:
        import capo_quicksight.types.data_field_combo_series_item

        out["data_field_combo_series_item"] = (
            capo_quicksight.types.data_field_combo_series_item.deserialize_json(
                data["DataFieldComboSeriesItem"]
            )
        )
    return out


def redact_sensitive(value: ComboSeriesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_field_combo_series_item" in value:
        import capo_quicksight.types.data_field_combo_series_item

        out["data_field_combo_series_item"] = (
            capo_quicksight.types.data_field_combo_series_item.redact_sensitive(
                value["data_field_combo_series_item"]
            )
        )
    return out
