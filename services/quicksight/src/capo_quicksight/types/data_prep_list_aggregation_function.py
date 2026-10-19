"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepListAggregationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.column_name
    import capo_quicksight.types.separator


class DataPrepListAggregationFunction(TypedDict, closed=True):
    input_column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The name of the column containing values to be concatenated.</p>"""
    separator: "capo_quicksight.types.separator.Separator"
    """<p>The string used to separate values in the concatenated result.</p>"""
    distinct: "capo_quicksight.types.boolean.Boolean"
    """<p>Whether to include only distinct values in the concatenated result, removing duplicates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepListAggregationFunction) -> dict:
    out: dict = {}
    if "input_column_name" in value:
        out["InputColumnName"] = value["input_column_name"]
    out["Separator"] = value["separator"]
    out["Distinct"] = value.get("distinct", False)
    return out


def deserialize_json(data: dict) -> DataPrepListAggregationFunction:
    out: DataPrepListAggregationFunction = {}  # type: ignore[typeddict-item]
    if data.get("InputColumnName") is not None:
        out["input_column_name"] = data["InputColumnName"]
    if data.get("Separator") is not None:
        out["separator"] = data["Separator"]
    else:
        out["separator"] = ""
    if data.get("Distinct") is not None:
        out["distinct"] = data["Distinct"]
    else:
        out["distinct"] = False
    return out
