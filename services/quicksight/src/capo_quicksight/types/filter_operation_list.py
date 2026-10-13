"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperationList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.filter_operation

FilterOperationList: TypeAlias = list[
    "capo_quicksight.types.filter_operation.FilterOperation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperationList) -> list:
    import capo_quicksight.types.filter_operation

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.filter_operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> FilterOperationList:
    import capo_quicksight.types.filter_operation

    out: FilterOperationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.filter_operation.deserialize_json(item))
    return out


def redact_sensitive(value: FilterOperationList) -> list[Any]:
    import capo_quicksight.types.filter_operation

    return [
        capo_quicksight.types.filter_operation.redact_sensitive(item) for item in value
    ]
