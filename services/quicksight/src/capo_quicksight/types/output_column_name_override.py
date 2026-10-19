"""Generated from Smithy shape ``com.amazonaws.quicksight#OutputColumnNameOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name


class OutputColumnNameOverride(TypedDict, closed=True):
    source_column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The original name of the column from the source transform operation.</p>"""
    output_column_name: "capo_quicksight.types.column_name.ColumnName"
    """<p>The new name to assign to the column in the output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnNameOverride) -> dict:
    out: dict = {}
    if "source_column_name" in value:
        out["SourceColumnName"] = value["source_column_name"]
    out["OutputColumnName"] = value["output_column_name"]
    return out


def deserialize_json(data: dict) -> OutputColumnNameOverride:
    out: OutputColumnNameOverride = {}  # type: ignore[typeddict-item]
    if data.get("SourceColumnName") is not None:
        out["source_column_name"] = data["SourceColumnName"]
    if data.get("OutputColumnName") is not None:
        out["output_column_name"] = data["OutputColumnName"]
    else:
        out["output_column_name"] = ""
    return out
