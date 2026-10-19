"""Generated from Smithy shape ``com.amazonaws.fms#ListAppsListsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_fms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.pagination_max_results
    import capo_fms.types.pagination_token


class ListAppsListsRequest(TypedDict, closed=True):
    default_lists: NotRequired["capo_fms.types.boolean.Boolean"]
    """<p>Specifies whether the lists to retrieve are default lists owned by Firewall Manager.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If you specify a value for <code>MaxResults</code> in your list request, and you have more objects than the maximum, Firewall Manager returns this token in the response. For all but the first request, you provide the token returned by the prior request in the request parameters, to retrieve the next batch of objects.</p>"""
    max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults"
    """<p>The maximum number of objects that you want Firewall Manager to return for this request. If more objects are available, in the response, Firewall Manager provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify this, Firewall Manager returns all available objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAppsListsRequest) -> dict:
    out: dict = {}
    if "default_lists" in value:
        out["DefaultLists"] = value["default_lists"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAppsListsRequest:
    out: ListAppsListsRequest = {}  # type: ignore[typeddict-item]
    if data.get("DefaultLists") is not None:
        out["default_lists"] = data["DefaultLists"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        raise DeserializationError("ListAppsListsRequest.max_results required")
    return out
