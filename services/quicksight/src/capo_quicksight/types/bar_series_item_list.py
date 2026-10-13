"""Generated from Smithy shape ``com.amazonaws.quicksight#BarSeriesItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.bar_series_item

BarSeriesItemList: TypeAlias = list[
    "capo_quicksight.types.bar_series_item.BarSeriesItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BarSeriesItemList) -> list:
    import capo_quicksight.types.bar_series_item

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.bar_series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BarSeriesItemList:
    import capo_quicksight.types.bar_series_item

    out: BarSeriesItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.bar_series_item.deserialize_json(item))
    return out


def redact_sensitive(value: BarSeriesItemList) -> list[Any]:
    import capo_quicksight.types.bar_series_item

    return [
        capo_quicksight.types.bar_series_item.redact_sensitive(item) for item in value
    ]
