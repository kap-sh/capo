"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetDateRangeFilterCondition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.boolean
    import capo_quicksight.types.data_set_date_filter_value


class DataSetDateRangeFilterCondition(TypedDict, closed=True):
    range_minimum: NotRequired[
        "capo_quicksight.types.data_set_date_filter_value.DataSetDateFilterValue"
    ]
    """<p>The minimum date value for the range filter.</p>"""
    range_maximum: NotRequired[
        "capo_quicksight.types.data_set_date_filter_value.DataSetDateFilterValue"
    ]
    """<p>The maximum date value for the range filter.</p>"""
    include_minimum: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Whether to include the minimum value in the filter range.</p>"""
    include_maximum: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Whether to include the maximum value in the filter range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetDateRangeFilterCondition) -> dict:
    out: dict = {}
    if "range_minimum" in value:
        import capo_quicksight.types.data_set_date_filter_value

        out["RangeMinimum"] = (
            capo_quicksight.types.data_set_date_filter_value.serialize_json(
                value["range_minimum"]
            )
        )
    if "range_maximum" in value:
        import capo_quicksight.types.data_set_date_filter_value

        out["RangeMaximum"] = (
            capo_quicksight.types.data_set_date_filter_value.serialize_json(
                value["range_maximum"]
            )
        )
    if "include_minimum" in value:
        out["IncludeMinimum"] = value["include_minimum"]
    if "include_maximum" in value:
        out["IncludeMaximum"] = value["include_maximum"]
    return out


def deserialize_json(data: dict) -> DataSetDateRangeFilterCondition:
    out: DataSetDateRangeFilterCondition = {}  # type: ignore[typeddict-item]
    if data.get("RangeMinimum") is not None:
        import capo_quicksight.types.data_set_date_filter_value

        out["range_minimum"] = (
            capo_quicksight.types.data_set_date_filter_value.deserialize_json(
                data["RangeMinimum"]
            )
        )
    if data.get("RangeMaximum") is not None:
        import capo_quicksight.types.data_set_date_filter_value

        out["range_maximum"] = (
            capo_quicksight.types.data_set_date_filter_value.deserialize_json(
                data["RangeMaximum"]
            )
        )
    if data.get("IncludeMinimum") is not None:
        out["include_minimum"] = data["IncludeMinimum"]
    if data.get("IncludeMaximum") is not None:
        out["include_maximum"] = data["IncludeMaximum"]
    return out


def redact_sensitive(value: DataSetDateRangeFilterCondition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "range_minimum" in value:
        import capo_quicksight.types.data_set_date_filter_value

        out["range_minimum"] = (
            capo_quicksight.types.data_set_date_filter_value.redact_sensitive(
                value["range_minimum"]
            )
        )
    if "range_maximum" in value:
        import capo_quicksight.types.data_set_date_filter_value

        out["range_maximum"] = (
            capo_quicksight.types.data_set_date_filter_value.redact_sensitive(
                value["range_maximum"]
            )
        )
    return out
