"""Generated from Smithy shape ``com.amazonaws.s3outposts#ListEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3outposts.types.max_results
    import capo_s3outposts.types.next_token


class ListEndpointsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_s3outposts.types.next_token.NextToken"]
    """<p>If a previous response from this operation included a <code>NextToken</code> value, provide that value here to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_s3outposts.types.max_results.MaxResults"]
    """<p>The maximum number of endpoints that will be returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEndpointsRequest:
    out: ListEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
