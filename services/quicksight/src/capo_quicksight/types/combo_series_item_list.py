"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboSeriesItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.combo_series_item

ComboSeriesItemList: TypeAlias = list[
    "capo_quicksight.types.combo_series_item.ComboSeriesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComboSeriesItemList) -> list:
    import capo_quicksight.types.combo_series_item

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.combo_series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ComboSeriesItemList:
    import capo_quicksight.types.combo_series_item

    out: ComboSeriesItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.combo_series_item.deserialize_json(item))
    return out


def redact_sensitive(value: ComboSeriesItemList) -> list[Any]:
    import capo_quicksight.types.combo_series_item

    return [
        capo_quicksight.types.combo_series_item.redact_sensitive(item) for item in value
    ]
