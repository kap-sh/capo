"""Generated from Smithy shape ``com.amazonaws.deadline#ListAvailableMeteredProductsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token


class ListAvailableMeteredProductsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAvailableMeteredProductsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAvailableMeteredProductsRequest:
    out: ListAvailableMeteredProductsRequest = {}  # type: ignore[typeddict-item]
    return out
