"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.list_grouping_statuses_filter_name
    import capo_resource_groups.types.list_grouping_statuses_filter_values


class ListGroupingStatusesFilter(TypedDict, closed=True):
    name: "capo_resource_groups.types.list_grouping_statuses_filter_name.ListGroupingStatusesFilterName"
    """<p>The name of the filter. Filter names are case-sensitive. </p>"""
    values: "capo_resource_groups.types.list_grouping_statuses_filter_values.ListGroupingStatusesFilterValues"
    """<p>One or more filter values. Allowed filter values vary by resource filter name, and are case-sensitive. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesFilter) -> dict:
    out: dict = {}
    import capo_resource_groups.types.list_grouping_statuses_filter_name

    out["Name"] = (
        capo_resource_groups.types.list_grouping_statuses_filter_name.serialize_json(
            value["name"]
        )
    )
    import capo_resource_groups.types.list_grouping_statuses_filter_values

    out["Values"] = (
        capo_resource_groups.types.list_grouping_statuses_filter_values.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListGroupingStatusesFilter:
    out: ListGroupingStatusesFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_resource_groups.types.list_grouping_statuses_filter_name

        out["name"] = (
            capo_resource_groups.types.list_grouping_statuses_filter_name.deserialize_json(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_resource_groups.types.list_grouping_statuses_filter_name.ListGroupingStatusesFilterName",
            "",
        )
    if data.get("Values") is not None:
        import capo_resource_groups.types.list_grouping_statuses_filter_values

        out["values"] = (
            capo_resource_groups.types.list_grouping_statuses_filter_values.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
