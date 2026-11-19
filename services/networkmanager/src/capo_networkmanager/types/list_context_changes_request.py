"""Generated from Smithy shape ``com.amazonaws.networkmanager#ListContextChangesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.context_store_id
    import capo_networkmanager.types.max_results
    import capo_networkmanager.types.next_token


class ListContextChangesRequest(TypedDict, closed=True):
    context_store_id: "capo_networkmanager.types.context_store_id.ContextStoreId"
    """<p>The ID of the context store.</p>"""
    from_version_id: "capo_networkmanager.types.constrained_string.ConstrainedString"
    """<p>The version to return changes from. Specify a version returned by <code>ListContexts</code>, <code>GetContextVersion</code>, or the <code>ToVersionId</code> of a previous <code>ListContextChanges</code> request. If the version is no longer available, the request fails, and you must call <code>ListContexts</code> to get the current context entries.</p>"""
    max_results: NotRequired["capo_networkmanager.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContextChangesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListContextChangesRequest:
    out: ListContextChangesRequest = {}  # type: ignore[typeddict-item]
    return out
