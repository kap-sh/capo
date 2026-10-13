"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetNumericFilterCondition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_name
    import capo_quicksight.types.data_set_numeric_comparison_filter_condition
    import capo_quicksight.types.data_set_numeric_range_filter_condition


class DataSetNumericFilterCondition(TypedDict, closed=True):
    column_name: NotRequired["capo_quicksight.types.column_name.ColumnName"]
    """<p>The name of the numeric column to filter.</p>"""
    comparison_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_numeric_comparison_filter_condition.DataSetNumericComparisonFilterCondition"
    ]
    """<p>A comparison-based filter condition for the numeric column.</p>"""
    range_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_numeric_range_filter_condition.DataSetNumericRangeFilterCondition"
    ]
    """<p>A range-based filter condition for the numeric column, filtering values between minimum and maximum numbers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetNumericFilterCondition) -> dict:
    out: dict = {}
    if "column_name" in value:
        out["ColumnName"] = value["column_name"]
    if "comparison_filter_condition" in value:
        import capo_quicksight.types.data_set_numeric_comparison_filter_condition

        out["ComparisonFilterCondition"] = (
            capo_quicksight.types.data_set_numeric_comparison_filter_condition.serialize_json(
                value["comparison_filter_condition"]
            )
        )
    if "range_filter_condition" in value:
        import capo_quicksight.types.data_set_numeric_range_filter_condition

        out["RangeFilterCondition"] = (
            capo_quicksight.types.data_set_numeric_range_filter_condition.serialize_json(
                value["range_filter_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataSetNumericFilterCondition:
    out: DataSetNumericFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    if data.get("ComparisonFilterCondition") is not None:
        import capo_quicksight.types.data_set_numeric_comparison_filter_condition

        out["comparison_filter_condition"] = (
            capo_quicksight.types.data_set_numeric_comparison_filter_condition.deserialize_json(
                data["ComparisonFilterCondition"]
            )
        )
    if data.get("RangeFilterCondition") is not None:
        import capo_quicksight.types.data_set_numeric_range_filter_condition

        out["range_filter_condition"] = (
            capo_quicksight.types.data_set_numeric_range_filter_condition.deserialize_json(
                data["RangeFilterCondition"]
            )
        )
    return out


def redact_sensitive(value: DataSetNumericFilterCondition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "comparison_filter_condition" in value:
        import capo_quicksight.types.data_set_numeric_comparison_filter_condition

        out["comparison_filter_condition"] = (
            capo_quicksight.types.data_set_numeric_comparison_filter_condition.redact_sensitive(
                value["comparison_filter_condition"]
            )
        )
    if "range_filter_condition" in value:
        import capo_quicksight.types.data_set_numeric_range_filter_condition

        out["range_filter_condition"] = (
            capo_quicksight.types.data_set_numeric_range_filter_condition.redact_sensitive(
                value["range_filter_condition"]
            )
        )
    return out
