"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.group_search_filter_list
    import capo_quicksight.types.max_results
    import capo_quicksight.types.namespace
    import capo_quicksight.types.string


class SearchGroupsRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that the group is in. Currently, you use the ID for the Amazon Web Services account that contains your Amazon Quick Sight account.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["capo_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return from this request.</p>"""
    namespace: "capo_quicksight.types.namespace.Namespace"
    """<p>The namespace that you want to search.</p>"""
    filters: "capo_quicksight.types.group_search_filter_list.GroupSearchFilterList"
    """<p>The structure for the search filters that you want to apply to your search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchGroupsRequest) -> dict:
    out: dict = {}
    import capo_quicksight.types.group_search_filter_list

    out["Filters"] = capo_quicksight.types.group_search_filter_list.serialize_json(
        value["filters"]
    )
    return out


def deserialize_json(data: dict) -> SearchGroupsRequest:
    out: SearchGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_quicksight.types.group_search_filter_list

        out["filters"] = (
            capo_quicksight.types.group_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        out["filters"] = []
    return out
