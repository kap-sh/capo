"""Generated from Smithy shape ``com.amazonaws.quicksight#CalculatedColumnList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.calculated_column

CalculatedColumnList: TypeAlias = list[
    "capo_quicksight.types.calculated_column.CalculatedColumn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CalculatedColumnList) -> list:
    import capo_quicksight.types.calculated_column

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.calculated_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> CalculatedColumnList:
    import capo_quicksight.types.calculated_column

    out: CalculatedColumnList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.calculated_column.deserialize_json(item))
    return out


def redact_sensitive(value: CalculatedColumnList) -> list[Any]:
    import capo_quicksight.types.calculated_column

    return [
        capo_quicksight.types.calculated_column.redact_sensitive(item) for item in value
    ]
