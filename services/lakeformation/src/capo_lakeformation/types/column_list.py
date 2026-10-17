"""Generated from Smithy shape ``com.amazonaws.lakeformation#ColumnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.column

ColumnList: TypeAlias = list["capo_lakeformation.types.column.Column"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnList) -> list:
    import capo_lakeformation.types.column

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.column.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnList:
    import capo_lakeformation.types.column

    out: ColumnList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lakeformation.types.column.deserialize_json(item))
    return out
