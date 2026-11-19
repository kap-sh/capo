"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionInvocationResultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.pagination_token
    import capo_mgn.types.remote_source_action_invocation_results_list


class ListRemoteSourceActionInvocationResultsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.remote_source_action_invocation_results_list.RemoteSourceActionInvocationResultsList"
    ]
    """<p>A list of source action invocation results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionInvocationResultsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.remote_source_action_invocation_results_list

        out["items"] = (
            capo_mgn.types.remote_source_action_invocation_results_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionInvocationResultsResponse:
    out: ListRemoteSourceActionInvocationResultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.remote_source_action_invocation_results_list

        out["items"] = (
            capo_mgn.types.remote_source_action_invocation_results_list.deserialize_json(
                data["items"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
