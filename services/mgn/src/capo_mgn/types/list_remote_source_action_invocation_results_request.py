"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionInvocationResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.source_server_id


class ListRemoteSourceActionInvocationResultsRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>The unique identifier of the source server to list invocation results for.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionInvocationResultsRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionInvocationResultsRequest:
    out: ListRemoteSourceActionInvocationResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
