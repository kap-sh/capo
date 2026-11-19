"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextStoresRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListContextStoresRequest(TypedDict, closed=True):
    global_network_id: NotRequired[
        "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    ]
    """<p>The ID of a global network. If you specify this parameter, only the context stores in the global network are returned.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextStoresRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContextStoresRequest:
    out: ListContextStoresRequest = {}  # type: ignore[typeddict-item]
    return out
