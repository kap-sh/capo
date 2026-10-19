"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetColumnIdMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_id


class DataSetColumnIdMapping(TypedDict, closed=True):
    source_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>Source column ID.</p>"""
    target_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>Target column ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetColumnIdMapping) -> dict:
    out: dict = {}
    out["SourceColumnId"] = value["source_column_id"]
    out["TargetColumnId"] = value["target_column_id"]
    return out


def deserialize_json(data: dict) -> DataSetColumnIdMapping:
    out: DataSetColumnIdMapping = {}  # type: ignore[typeddict-item]
    if data.get("SourceColumnId") is not None:
        out["source_column_id"] = data["SourceColumnId"]
    else:
        out["source_column_id"] = ""
    if data.get("TargetColumnId") is not None:
        out["target_column_id"] = data["TargetColumnId"]
    else:
        out["target_column_id"] = ""
    return out
