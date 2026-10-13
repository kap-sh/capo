"""Generated from Smithy shape ``com.amazonaws.quicksight#SeriesItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_field_series_item
    import capo_quicksight.types.field_series_item


class SeriesItem(TypedDict, closed=True):
    field_series_item: NotRequired[
        "capo_quicksight.types.field_series_item.FieldSeriesItem"
    ]
    """<p>The field series item configuration of a line chart.</p>"""
    data_field_series_item: NotRequired[
        "capo_quicksight.types.data_field_series_item.DataFieldSeriesItem"
    ]
    """<p>The data field series item configuration of a line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeriesItem) -> dict:
    out: dict = {}
    if "field_series_item" in value:
        import capo_quicksight.types.field_series_item

        out["FieldSeriesItem"] = capo_quicksight.types.field_series_item.serialize_json(
            value["field_series_item"]
        )
    if "data_field_series_item" in value:
        import capo_quicksight.types.data_field_series_item

        out["DataFieldSeriesItem"] = (
            capo_quicksight.types.data_field_series_item.serialize_json(
                value["data_field_series_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> SeriesItem:
    out: SeriesItem = {}  # type: ignore[typeddict-item]
    if data.get("FieldSeriesItem") is not None:
        import capo_quicksight.types.field_series_item

        out["field_series_item"] = (
            capo_quicksight.types.field_series_item.deserialize_json(
                data["FieldSeriesItem"]
            )
        )
    if data.get("DataFieldSeriesItem") is not None:
        import capo_quicksight.types.data_field_series_item

        out["data_field_series_item"] = (
            capo_quicksight.types.data_field_series_item.deserialize_json(
                data["DataFieldSeriesItem"]
            )
        )
    return out


def redact_sensitive(value: SeriesItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "data_field_series_item" in value:
        import capo_quicksight.types.data_field_series_item

        out["data_field_series_item"] = (
            capo_quicksight.types.data_field_series_item.redact_sensitive(
                value["data_field_series_item"]
            )
        )
    return out
