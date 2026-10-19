"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepSimpleAggregationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.data_prep_simple_aggregation_function_type


class DataPrepSimpleAggregationFunction(TypedDict, closed=True):
    input_column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The name of the column on which to perform the aggregation function.</p>"""
    function_type: "capo_quicksight.types.data_prep_simple_aggregation_function_type.DataPrepSimpleAggregationFunctionType"
    """<p>The type of aggregation function to perform, such as <code>COUNT</code>, <code>SUM</code>, <code>AVERAGE</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>VARIANCE</code>, or <code>STANDARD_DEVIATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepSimpleAggregationFunction) -> dict:
    out: dict = {}
    if "input_column_name" in value:
        out["InputColumnName"] = value["input_column_name"]
    import capo_quicksight.types.data_prep_simple_aggregation_function_type

    out["FunctionType"] = (
        capo_quicksight.types.data_prep_simple_aggregation_function_type.serialize_json(
            value["function_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataPrepSimpleAggregationFunction:
    out: DataPrepSimpleAggregationFunction = {}  # type: ignore[typeddict-item]
    if data.get("InputColumnName") is not None:
        out["input_column_name"] = data["InputColumnName"]
    if data.get("FunctionType") is not None:
        import capo_quicksight.types.data_prep_simple_aggregation_function_type

        out["function_type"] = (
            capo_quicksight.types.data_prep_simple_aggregation_function_type.deserialize_json(
                data["FunctionType"]
            )
        )
    else:
        import typing

        out["function_type"] = typing.cast(
            "capo_quicksight.types.data_prep_simple_aggregation_function_type.DataPrepSimpleAggregationFunctionType",
            "",
        )
    return out
