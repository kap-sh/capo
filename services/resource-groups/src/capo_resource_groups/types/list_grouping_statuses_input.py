"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupingStatusesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_string_v2
    import capo_resource_groups.types.list_grouping_statuses_filter_list
    import capo_resource_groups.types.max_results
    import capo_resource_groups.types.next_token


class ListGroupingStatusesInput(TypedDict, closed=True):
    group: "capo_resource_groups.types.group_string_v2.GroupStringV2"
    """<p>The application group identifier, expressed as an Amazon resource name (ARN) or the application group name. </p>"""
    max_results: NotRequired["capo_resource_groups.types.max_results.MaxResults"]
    """<p>The maximum number of resources and their statuses returned in the response. </p>"""
    filters: NotRequired[
        "capo_resource_groups.types.list_grouping_statuses_filter_list.ListGroupingStatusesFilterList"
    ]
    """<p>The filter name and value pair that is used to return more specific results from a list of resources. </p>"""
    next_token: NotRequired["capo_resource_groups.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupingStatusesInput) -> dict:
    out: dict = {}
    out["Group"] = value["group"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_resource_groups.types.list_grouping_statuses_filter_list

        out["Filters"] = (
            capo_resource_groups.types.list_grouping_statuses_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupingStatusesInput:
    out: ListGroupingStatusesInput = {}  # type: ignore[typeddict-item]
    if data.get("Group") is not None:
        out["group"] = data["Group"]
    else:
        out["group"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_resource_groups.types.list_grouping_statuses_filter_list

        out["filters"] = (
            capo_resource_groups.types.list_grouping_statuses_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
