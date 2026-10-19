"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAppsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.filter_operator
    import capo_quicksight.types.search_apps_filter_name


class SearchAppsFilter(TypedDict, closed=True):
    name: "capo_quicksight.types.search_apps_filter_name.SearchAppsFilterName"
    """<p>The name of the filter attribute.</p>"""
    operator: "capo_quicksight.types.filter_operator.FilterOperator"
    """<p>The comparison operator for the filter.</p>"""
    value: "str"
    """<p>The value to filter on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAppsFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.search_apps_filter_name

    out["Name"] = capo_quicksight.types.search_apps_filter_name.serialize_json(
        value["name"]
    )
    import capo_quicksight.types.filter_operator

    out["Operator"] = capo_quicksight.types.filter_operator.serialize_json(
        value["operator"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> SearchAppsFilter:
    out: SearchAppsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_quicksight.types.search_apps_filter_name

        out["name"] = capo_quicksight.types.search_apps_filter_name.deserialize_json(
            data["Name"]
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_quicksight.types.search_apps_filter_name.SearchAppsFilterName", ""
        )
    if data.get("Operator") is not None:
        import capo_quicksight.types.filter_operator

        out["operator"] = capo_quicksight.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_quicksight.types.filter_operator.FilterOperator", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
