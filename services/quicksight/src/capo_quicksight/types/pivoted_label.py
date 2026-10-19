"""Generated from Smithy shape ``com.amazonaws.quicksight#PivotedLabel``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.cell_value
    import capo_quicksight.types.column_id
    import capo_quicksight.types.column_name


class PivotedLabel(TypedDict, closed=True):
    label_name: "capo_quicksight.types.cell_value.CellValue"
    """<p>The label value from the source data to be pivoted.</p>"""
    new_column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column created from this pivoted label.</p>"""
    new_column_id: "capo_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column created from this pivoted label.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PivotedLabel) -> dict:
    out: dict = {}
    out["LabelName"] = value["label_name"]
    out["NewColumnName"] = value["new_column_name"]
    out["NewColumnId"] = value["new_column_id"]
    return out


def deserialize_json(data: dict) -> PivotedLabel:
    out: PivotedLabel = {}  # type: ignore[typeddict-item]
    if data.get("LabelName") is not None:
        out["label_name"] = data["LabelName"]
    else:
        out["label_name"] = ""
    if data.get("NewColumnName") is not None:
        out["new_column_name"] = data["NewColumnName"]
    else:
        out["new_column_name"] = ""
    if data.get("NewColumnId") is not None:
        out["new_column_id"] = data["NewColumnId"]
    else:
        out["new_column_id"] = ""
    return out
