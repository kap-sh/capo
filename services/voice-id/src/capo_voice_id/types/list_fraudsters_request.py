"""Generated from Smithy shape ``com.amazonaws.voiceid#ListFraudstersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.max_results_for_list
    import capo_voice_id.types.next_token
    import capo_voice_id.types.watchlist_id


class ListFraudstersRequest(TypedDict, closed=True):
    domain_id: "capo_voice_id.types.domain_id.DomainId"
    """<p>The identifier of the domain. </p>"""
    watchlist_id: NotRequired["capo_voice_id.types.watchlist_id.WatchlistId"]
    """<p>The identifier of the watchlist. If provided, all fraudsters in the watchlist are listed. If not provided, all fraudsters in the domain are listed.</p>"""
    max_results: NotRequired[
        "capo_voice_id.types.max_results_for_list.MaxResultsForList"
    ]
    """<p>The maximum number of results that are returned per call. You can use <code>NextToken</code> to obtain more pages of results. The default is 100; the maximum allowed page size is also 100. </p>"""
    next_token: NotRequired["capo_voice_id.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFraudstersRequest) -> dict:
    out: dict = {}
    out["DomainId"] = value["domain_id"]
    if "watchlist_id" in value:
        out["WatchlistId"] = value["watchlist_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFraudstersRequest:
    out: ListFraudstersRequest = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    else:
        out["domain_id"] = ""
    if data.get("WatchlistId") is not None:
        out["watchlist_id"] = data["WatchlistId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
