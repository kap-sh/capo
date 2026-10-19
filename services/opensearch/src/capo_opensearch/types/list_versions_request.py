"""Generated from Smithy shape ``com.amazonaws.opensearch#ListVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.max_results
    import capo_opensearch.types.next_token


class ListVersionsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_opensearch.types.max_results.MaxResults"]
    """<p>An optional parameter that specifies the maximum number of results to return. You can use <code>nextToken</code> to get the next page of results.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>If your initial <code>ListVersions</code> operation returns a <code>nextToken</code>, you can include the returned <code>nextToken</code> in subsequent <code>ListVersions</code> operations, which returns results in the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListVersionsRequest:
    out: ListVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
