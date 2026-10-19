"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterListConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.category_filter_match_operator
    import capo_quicksight.types.category_filter_select_all_options
    import capo_quicksight.types.category_value_list
    import capo_quicksight.types.filter_null_option


class FilterListConfiguration(TypedDict, closed=True):
    match_operator: "capo_quicksight.types.category_filter_match_operator.CategoryFilterMatchOperator"
    """<p>The match operator that is used to determine if a filter should be applied.</p>"""
    category_values: NotRequired[
        "capo_quicksight.types.category_value_list.CategoryValueList"
    ]
    """<p>The list of category values for the filter.</p>"""
    select_all_options: NotRequired[
        "capo_quicksight.types.category_filter_select_all_options.CategoryFilterSelectAllOptions"
    ]
    """<p>Select all of the values. Null is not the assigned value of select all.</p> <ul> <li> <p> <code>FILTER_ALL_VALUES</code> </p> </li> </ul>"""
    null_option: NotRequired[
        "capo_quicksight.types.filter_null_option.FilterNullOption"
    ]
    """<p>This option determines how null values should be treated when filtering data.</p> <ul> <li> <p> <code>ALL_VALUES</code>: Include null values in filtered results.</p> </li> <li> <p> <code>NULLS_ONLY</code>: Only include null values in filtered results.</p> </li> <li> <p> <code>NON_NULLS_ONLY</code>: Exclude null values from filtered results.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterListConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.category_filter_match_operator

    out["MatchOperator"] = (
        capo_quicksight.types.category_filter_match_operator.serialize_json(
            value["match_operator"]
        )
    )
    if "category_values" in value:
        import capo_quicksight.types.category_value_list

        out["CategoryValues"] = (
            capo_quicksight.types.category_value_list.serialize_json(
                value["category_values"]
            )
        )
    if "select_all_options" in value:
        import capo_quicksight.types.category_filter_select_all_options

        out["SelectAllOptions"] = (
            capo_quicksight.types.category_filter_select_all_options.serialize_json(
                value["select_all_options"]
            )
        )
    if "null_option" in value:
        import capo_quicksight.types.filter_null_option

        out["NullOption"] = capo_quicksight.types.filter_null_option.serialize_json(
            value["null_option"]
        )
    return out


def deserialize_json(data: dict) -> FilterListConfiguration:
    out: FilterListConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("CategoryValues") is not None:
        import capo_quicksight.types.category_value_list

        out["category_values"] = (
            capo_quicksight.types.category_value_list.deserialize_json(
                data["CategoryValues"]
            )
        )
    if data.get("SelectAllOptions") is not None:
        import capo_quicksight.types.category_filter_select_all_options

        out["select_all_options"] = (
            capo_quicksight.types.category_filter_select_all_options.deserialize_json(
                data["SelectAllOptions"]
            )
        )
    if data.get("NullOption") is not None:
        import capo_quicksight.types.filter_null_option

        out["null_option"] = capo_quicksight.types.filter_null_option.deserialize_json(
            data["NullOption"]
        )
    return out
