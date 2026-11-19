"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.list_remote_source_actions_request_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class ListRemoteSourceActionsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_mgn.types.list_remote_source_actions_request_filters.ListRemoteSourceActionsRequestFilters"
    ]
    """<p>Filters to apply when listing source actions.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_mgn.types.list_remote_source_actions_request_filters

        out["filters"] = (
            capo_mgn.types.list_remote_source_actions_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionsRequest:
    out: ListRemoteSourceActionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("filters") is not None:
        import capo_mgn.types.list_remote_source_actions_request_filters

        out["filters"] = (
            capo_mgn.types.list_remote_source_actions_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    return out
