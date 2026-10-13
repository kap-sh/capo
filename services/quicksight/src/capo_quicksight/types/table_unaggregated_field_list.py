"""Generated from Smithy shape ``com.amazonaws.quicksight#TableUnaggregatedFieldList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.unaggregated_field

TableUnaggregatedFieldList: TypeAlias = list[
    "capo_quicksight.types.unaggregated_field.UnaggregatedField"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableUnaggregatedFieldList) -> list:
    import capo_quicksight.types.unaggregated_field

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.unaggregated_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableUnaggregatedFieldList:
    import capo_quicksight.types.unaggregated_field

    out: TableUnaggregatedFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.unaggregated_field.deserialize_json(item))
    return out


def redact_sensitive(value: TableUnaggregatedFieldList) -> list[Any]:
    import capo_quicksight.types.unaggregated_field

    return [
        capo_quicksight.types.unaggregated_field.redact_sensitive(item)
        for item in value
    ]
