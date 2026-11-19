"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.context_store_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListContextsRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContextsRequest:
    out: ListContextsRequest = {}  # type: ignore[typeddict-item]
    return out
