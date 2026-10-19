"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericEqualityFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.aggregation_function
    import capo_quicksight.types.column_identifier
    import capo_quicksight.types.default_filter_control_configuration
    import capo_quicksight.types.double
    import capo_quicksight.types.filter_null_option
    import capo_quicksight.types.numeric_equality_match_operator
    import capo_quicksight.types.numeric_filter_select_all_options
    import capo_quicksight.types.parameter_name
    import capo_quicksight.types.short_restrictive_resource_id


class NumericEqualityFilter(TypedDict, closed=True):
    filter_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>An identifier that uniquely identifies a filter within a dashboard, analysis, or template.</p>"""
    column: "capo_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the filter is applied to.</p>"""
    value: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The input value.</p>"""
    select_all_options: NotRequired[
        "capo_quicksight.types.numeric_filter_select_all_options.NumericFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    match_operator: "capo_quicksight.types.numeric_equality_match_operator.NumericEqualityMatchOperator"
    """<p>The match operator that is used to determine if a filter should be applied.</p>"""
    aggregation_function: NotRequired[
        "capo_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function of the filter.</p>"""
    parameter_name: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p>"""
    null_option: "capo_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""
    default_filter_control_configuration: NotRequired[
        "capo_quicksight.types.default_filter_control_configuration.DefaultFilterControlConfiguration"
    ]
    """<p>The default configurations for the associated controls. This applies only for filters that are scoped to multiple sheets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericEqualityFilter) -> dict:
    out: dict = {}
    out["FilterId"] = value["filter_id"]
    import capo_quicksight.types.column_identifier

    out["Column"] = capo_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "value" in value:
        out["Value"] = (
            "NaN"
            if value["value"] != value["value"]
            else "Infinity"
            if value["value"] == float("inf")
            else "-Infinity"
            if value["value"] == float("-inf")
            else value["value"]
        )
    if "select_all_options" in value:
        import capo_quicksight.types.numeric_filter_select_all_options

        out["SelectAllOptions"] = (
            capo_quicksight.types.numeric_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    import capo_quicksight.types.numeric_equality_match_operator

    out["MatchOperator"] = (
        capo_quicksight.types.numeric_equality_match_operator.serialize_json(
            value["match_operator"]
        )
    )
    if "aggregation_function" in value:
        import capo_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            capo_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
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


def deserialize_json(data: dict) -> NumericEqualityFilter:
    out: NumericEqualityFilter = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("NumericEqualityFilter.column required")
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    if data.get("SelectAllOptions") is not None:
        import capo_quicksight.types.numeric_filter_select_all_options

        out["select_all_options"] = (
            capo_quicksight.types.numeric_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if data.get("MatchOperator") is not None:
        import capo_quicksight.types.numeric_equality_match_operator

        out["match_operator"] = (
            capo_quicksight.types.numeric_equality_match_operator.deserialize_json(
                data["MatchOperator"]
            )
        )
    else:
        import typing

        out["match_operator"] = typing.cast(
            "capo_quicksight.types.numeric_equality_match_operator.NumericEqualityMatchOperator",
            "",
        )
    if data.get("AggregationFunction") is not None:
        import capo_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            capo_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if data.get("ParameterName") is not None:
        out["parameter_name"] = data["ParameterName"]
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
