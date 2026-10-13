"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotFieldSortOptionsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.pivot_field_sort_options

PivotFieldSortOptionsList: TypeAlias = list[
    "capo_quicksight.types.pivot_field_sort_options.PivotFieldSortOptions"
]


# --- restJson1 ser/de ---
def serialize_json(value: PivotFieldSortOptionsList) -> list:
    import capo_quicksight.types.pivot_field_sort_options

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.pivot_field_sort_options.serialize_json(item))
    return out


def deserialize_json(data: list) -> PivotFieldSortOptionsList:
    import capo_quicksight.types.pivot_field_sort_options

    out: PivotFieldSortOptionsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.pivot_field_sort_options.deserialize_json(item)
        )
    return out


def redact_sensitive(value: PivotFieldSortOptionsList) -> list[Any]:
    import capo_quicksight.types.pivot_field_sort_options

    return [
        capo_quicksight.types.pivot_field_sort_options.redact_sensitive(item)
        for item in value
    ]
