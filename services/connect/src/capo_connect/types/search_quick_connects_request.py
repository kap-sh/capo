"""Generated from Smithy shape ``com.amazonaws.connect#SearchQuickConnectsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token2500
    import capo_connect.types.quick_connect_search_criteria
    import capo_connect.types.quick_connect_search_filter


class SearchQuickConnectsRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    next_token: NotRequired["capo_connect.types.next_token2500.NextToken2500"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    search_filter: NotRequired[
        "capo_connect.types.quick_connect_search_filter.QuickConnectSearchFilter"
    ]
    """<p>Filters to be applied to search results.</p>"""
    search_criteria: NotRequired[
        "capo_connect.types.quick_connect_search_criteria.QuickConnectSearchCriteria"
    ]
    """<p>The search criteria to be used to return quick connects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuickConnectsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "search_filter" in value:
        import capo_connect.types.quick_connect_search_filter

        out["SearchFilter"] = (
            capo_connect.types.quick_connect_search_filter.serialize_json(
                value["search_filter"]
            )
        )
    if "search_criteria" in value:
        import capo_connect.types.quick_connect_search_criteria

        out["SearchCriteria"] = (
            capo_connect.types.quick_connect_search_criteria.serialize_json(
                value["search_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchQuickConnectsRequest:
    out: SearchQuickConnectsRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("SearchQuickConnectsRequest.instance_id required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SearchFilter") is not None:
        import capo_connect.types.quick_connect_search_filter

        out["search_filter"] = (
            capo_connect.types.quick_connect_search_filter.deserialize_json(
                data["SearchFilter"]
            )
        )
    if data.get("SearchCriteria") is not None:
        import capo_connect.types.quick_connect_search_criteria

        out["search_criteria"] = (
            capo_connect.types.quick_connect_search_criteria.deserialize_json(
                data["SearchCriteria"]
            )
        )
    return out
