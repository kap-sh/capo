"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.filter

FilterList: TypeAlias = list["capo_quicksight.types.filter.Filter"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterList) -> list:
    import capo_quicksight.types.filter

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterList:
    import capo_quicksight.types.filter

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.filter.deserialize_json(item))
    return out


def redact_sensitive(value: FilterList) -> list[Any]:
    import capo_quicksight.types.filter

    return [capo_quicksight.types.filter.redact_sensitive(item) for item in value]
