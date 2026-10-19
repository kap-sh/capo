"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.column_data_type
    import capo_iotsitewise.types.column_label


class ColumnInformation(TypedDict, closed=True):
    name: "capo_iotsitewise.types.column_label.ColumnLabel"
    """<p>The name of the column.</p>"""
    type: "capo_iotsitewise.types.column_data_type.ColumnDataType"
    """<p>The data type of the column. Valid values are STRING, DOUBLE, BOOLEAN, INTEGER, TIMESTAMP, and VARIANT.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnInformation) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    return out


def deserialize_json(data: dict) -> ColumnInformation:
    out: ColumnInformation = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    return out
