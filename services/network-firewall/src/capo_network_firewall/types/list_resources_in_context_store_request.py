"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListResourcesInContextStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.context_filters
    import capo_network_firewall.types.context_store_id
    import capo_network_firewall.types.pagination_max_results
    import capo_network_firewall.types.pagination_token


class ListResourcesInContextStoreRequest(TypedDict, closed=True):
    context_store_id: "capo_network_firewall.types.context_store_id.ContextStoreId"
    """<p>The unique identifier of the context store. To get the identifiers of the context stores that are associated with your firewalls, call <code>ListContextStores</code>.</p>"""
    filters: NotRequired["capo_network_firewall.types.context_filters.ContextFilters"]
    """<p>Optional filters that limit the results to resources in a specific Region, of a specific resource type, or both. If you specify both filters, Network Firewall returns only the resources that match both.</p>"""
    max_results: NotRequired[
        "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p> <p>A token is valid only for the same <code>ContextStoreId</code> and filters as the request that returned it.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourcesInContextStoreRequest) -> dict:
    out: dict = {}
    out["ContextStoreId"] = value["context_store_id"]
    if "filters" in value:
        import capo_network_firewall.types.context_filters

        out["Filters"] = (
            capo_network_firewall.types.context_filters.serialize_aws_json_1_0(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourcesInContextStoreRequest:
    out: ListResourcesInContextStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContextStoreId") is not None:
        out["context_store_id"] = data["ContextStoreId"]
    else:
        out["context_store_id"] = ""
    if data.get("Filters") is not None:
        import capo_network_firewall.types.context_filters

        out["filters"] = (
            capo_network_firewall.types.context_filters.deserialize_aws_json_1_0(
                data["Filters"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
