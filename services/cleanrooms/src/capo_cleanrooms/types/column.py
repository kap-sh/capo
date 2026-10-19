"""Generated from Smithy shape ``com.amazonaws.cleanrooms#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.column_name
    import capo_cleanrooms.types.column_type_string


class Column(TypedDict, closed=True):
    name: "capo_cleanrooms.types.column_name.ColumnName"
    """<p>The name of the column.</p>"""
    type: "capo_cleanrooms.types.column_type_string.ColumnTypeString"
    """<p>The type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Column) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Column:
    out: Column = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
