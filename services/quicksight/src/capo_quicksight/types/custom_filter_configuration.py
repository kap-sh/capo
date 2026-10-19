"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomFilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.category_filter_match_operator
    import capo_quicksight.types.category_filter_select_all_options
    import capo_quicksight.types.category_value
    import capo_quicksight.types.filter_null_option
    import capo_quicksight.types.parameter_name


class CustomFilterConfiguration(TypedDict, closed=True):
    match_operator: "capo_quicksight.types.category_filter_match_operator.CategoryFilterMatchOperator"
    """<p>The match operator that is used to determine if a filter should be applied.</p>"""
    category_value: NotRequired["capo_quicksight.types.category_value.CategoryValue"]
    """<p>The category value for the filter.</p> <p>This field is mutually exclusive to <code>ParameterName</code>.</p>"""
    select_all_options: NotRequired[
        "capo_quicksight.types.category_filter_select_all_options.CategoryFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    parameter_name: NotRequired["capo_quicksight.types.parameter_name.ParameterName"]
    """<p>The parameter whose value should be used for the filter value.</p> <p>This field is mutually exclusive to <code>CategoryValue</code>.</p>"""
    null_option: "capo_quicksight.types.filter_null_option.FilterNullOption"
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomFilterConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.category_filter_match_operator

    out["MatchOperator"] = (
        capo_quicksight.types.category_filter_match_operator.serialize_json(
            value["match_operator"]
        )
    )
    if "category_value" in value:
        out["CategoryValue"] = value["category_value"]
    if "select_all_options" in value:
        import capo_quicksight.types.category_filter_select_all_options

        out["SelectAllOptions"] = (
            capo_quicksight.types.category_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    if "parameter_name" in value:
        out["ParameterName"] = value["parameter_name"]
    import capo_quicksight.types.filter_null_option

    out["NullOption"] = capo_quicksight.types.filter_null_option.serialize_json(
        value["null_option"]
    )
    return out


def deserialize_json(data: dict) -> CustomFilterConfiguration:
    out: CustomFilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MatchOperator") is not None:
        import capo_quicksight.types.category_filter_match_operator

        out["match_operator"] = (
            capo_quicksight.types.category_filter_match_operator.deserialize_json(
                data["MatchOperator"]
            )
        )
    else:
        import typing

        out["match_operator"] = typing.cast(
            "capo_quicksight.types.category_filter_match_operator.CategoryFilterMatchOperator",
            "",
        )
    if data.get("CategoryValue") is not None:
        out["category_value"] = data["CategoryValue"]
    if data.get("SelectAllOptions") is not None:
        import capo_quicksight.types.category_filter_select_all_options

        out["select_all_options"] = (
            capo_quicksight.types.category_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
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
    return out
