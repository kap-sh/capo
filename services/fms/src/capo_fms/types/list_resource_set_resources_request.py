"""Generated from Smithy shape ``com.amazonaws.fms#ListResourceSetResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_max_results
    import capo_fms.types.pagination_token
    import capo_fms.types.resource_id


class ListResourceSetResourcesRequest(TypedDict, closed=True):
    identifier: "capo_fms.types.resource_id.ResourceId"
    """<p>A unique identifier for the resource set, used in a request to refer to the resource set.</p>"""
    max_results: NotRequired[
        "capo_fms.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Firewall Manager returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceSetResourcesRequest) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceSetResourcesRequest:
    out: ListResourceSetResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
