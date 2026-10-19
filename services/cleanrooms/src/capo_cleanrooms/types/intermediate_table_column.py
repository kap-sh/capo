"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_name
    import capo_cleanrooms.types.intermediate_table_column_type_string


class IntermediateTableColumn(TypedDict, closed=True):
    name: "capo_cleanrooms.types.column_name.ColumnName"
    """<p>The name of the column.</p>"""
    type: "capo_cleanrooms.types.intermediate_table_column_type_string.IntermediateTableColumnTypeString"
    """<p>The data type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableColumn) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> IntermediateTableColumn:
    out: IntermediateTableColumn = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
