"""Generated from Smithy shape ``com.amazonaws.quicksight#SeriesItemList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.series_item

SeriesItemList: TypeAlias = list["capo_quicksight.types.series_item.SeriesItem"]


# --- restJson1 ser/de ---
def serialize_json(value: SeriesItemList) -> list:
    import capo_quicksight.types.series_item

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.series_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> SeriesItemList:
    import capo_quicksight.types.series_item

    out: SeriesItemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.series_item.deserialize_json(item))
    return out


def redact_sensitive(value: SeriesItemList) -> list[Any]:
    import capo_quicksight.types.series_item

    return [capo_quicksight.types.series_item.redact_sensitive(item) for item in value]
