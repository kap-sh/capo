"""Generated from Smithy shape ``com.amazonaws.quicksight#RenameColumnOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name


class RenameColumnOperation(TypedDict, closed=True):
    column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name of the column to be renamed.</p>"""
    new_column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The new name for the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RenameColumnOperation) -> dict:
    out: dict = {}
    out["ColumnName"] = value["column_name"]
    out["NewColumnName"] = value["new_column_name"]
    return out


def deserialize_json(data: dict) -> RenameColumnOperation:
    out: RenameColumnOperation = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("NewColumnName") is not None:
        out["new_column_name"] = data["NewColumnName"]
    else:
        out["new_column_name"] = ""
    return out
