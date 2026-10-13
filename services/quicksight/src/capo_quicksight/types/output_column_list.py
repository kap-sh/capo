"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumnList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.output_column

OutputColumnList: TypeAlias = list["capo_quicksight.types.output_column.OutputColumn"]


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnList) -> list:
    import capo_quicksight.types.output_column

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.output_column.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutputColumnList:
    import capo_quicksight.types.output_column

    out: OutputColumnList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.output_column.deserialize_json(item))
    return out


def redact_sensitive(value: OutputColumnList) -> list[Any]:
    import capo_quicksight.types.output_column

    return [
        capo_quicksight.types.output_column.redact_sensitive(item) for item in value
    ]
