"""Generated from Smithy shape ``com.amazonaws.lakeformation#Column``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.column_type_string
    import capo_lakeformation.types.name_string


class Column(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the column.</p>"""
    type: NotRequired["capo_lakeformation.types.column_type_string.ColumnTypeString"]
    """<p>The data type of the column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Column) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> Column:
    out: Column = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
