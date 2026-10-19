"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericRangeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_function
    import capo_quicksight.types.boolean
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.filter_null_option
    import capo_quicksight.types.numeric_filter_select_all_options
    import capo_quicksight.types.numeric_range_filter_value
    import capo_quicksight.types.short_restrictive_resource_id


class NumericRangeFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    include_minimum: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the minimum value in the filter value range should be included in the filtered results.</p>"""
    include_maximum: NotRequired["capo_quicksight.types.boolean.Boolean"]
    """<p>Determines whether the maximum value in the filter value range should be included in the filtered results.</p>"""
    range_minimum: NotRequired[
        "capo_quicksight.types.numeric_range_filter_value.NumericRangeFilterValue"
    ]
    """<p>The minimum value for the filter value range.</p>"""
    range_maximum: NotRequired[
        "capo_quicksight.types.numeric_range_filter_value.NumericRangeFilterValue"
    ]
    """<p>The maximum value for the filter value range.</p>"""
    select_all_options: NotRequired[
        "capo_quicksight.types.numeric_filter_select_all_options.NumericFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    aggregation_function: NotRequired[
        "capo_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function of the filter.</p>"""
    null_option: "capo_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericRangeFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "include_minimum" in value:
        out["IncludeMinimum"] = value["include_minimum"]
    if "include_maximum" in value:
        out["IncludeMaximum"] = value["include_maximum"]
    if "range_minimum" in value:
        import capo_quicksight.types.numeric_range_filter_value

        out["RangeMinimum"] = (
            capo_quicksight.types.numeric_range_filter_value.serialize_json(
                value["range_minimum"]
            )
        )
    if "range_maximum" in value:
        import capo_quicksight.types.numeric_range_filter_value

        out["RangeMaximum"] = (
            capo_quicksight.types.numeric_range_filter_value.serialize_json(
                value["range_maximum"]
            )
        )
    if "select_all_options" in value:
        import capo_quicksight.types.numeric_filter_select_all_options

        out["SelectAllOptions"] = (
            capo_quicksight.types.numeric_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    if "aggregation_function" in value:
        import capo_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            capo_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    import capo_quicksight.types.filter_null_option

    out["NullOption"] = capo_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    if "default_filter_control_configuration" in value:
        import capo_quicksight.types.default_filter_control_configuration

        out["DefaultFilterControlConfiguration"] = (
            capo_quicksight.types.default_filter_control_configuration.serialize_json(
                value["default_filter_control_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericRangeFilter:
    out: NumericRangeFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterId") is not None:
        out["filter_id"] = data["FilterId"]
    else:
        out["filter_id"] = ""
    if data.get("Column") is not None:
        import capo_quicksight.types.column_identifier

        out["column"] = capo_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("NumericRangeFilter.column required")
    if data.get("IncludeMinimum") is not None:
        out["include_minimum"] = data["IncludeMinimum"]
    if data.get("IncludeMaximum") is not None:
        out["include_maximum"] = data["IncludeMaximum"]
    if data.get("RangeMinimum") is not None:
        import capo_quicksight.types.numeric_range_filter_value

        out["range_minimum"] = (
            capo_quicksight.types.numeric_range_filter_value.deserialize_json(
                data["RangeMinimum"]
            )
        )
    if data.get("RangeMaximum") is not None:
        import capo_quicksight.types.numeric_range_filter_value

        out["range_maximum"] = (
            capo_quicksight.types.numeric_range_filter_value.deserialize_json(
                data["RangeMaximum"]
            )
        )
    if data.get("SelectAllOptions") is not None:
        import capo_quicksight.types.numeric_filter_select_all_options

        out["select_all_options"] = (
            capo_quicksight.types.numeric_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if data.get("AggregationFunction") is not None:
        import capo_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            capo_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if data.get("NullOption") is not None:
        import capo_quicksight.types.filter_null_option

        out["null_option"] = capo_quicksight.types.filter_null_option.deserialize_json(
            data["NullOption"]
        )
    else:
        import typing

        out["null_option"] = typing.cast(
            "capo_quicksight.types.filter_null_option.FilterNullOption", ""
        )
    if data.get("DefaultFilterControlConfiguration") is not None:
        import capo_quicksight.types.default_filter_control_configuration

        out["default_filter_control_configuration"] = (
            capo_quicksight.types.default_filter_control_configuration.deserialize_json(
                data["DefaultFilterControlConfiguration"]
            )
        )
    return out
