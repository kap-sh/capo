"""Generated from Smithy shape ``com.amazonaws.quicksight#AppendedColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_id
    import capo_quicksight.types.column_name


class AppendedColumn(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name of the column to include in the appended result.</p>"""
    new_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the column in the appended result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppendedColumn) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["NewColumnId"] = value["new_column_id"]
    return out


def deserialize_json(data: dict) -> AppendedColumn:
    out: AppendedColumn = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("NewColumnId") is not None:
        out["new_column_id"] = data["NewColumnId"]
    else:
        out["new_column_id"] = ""
    return out
