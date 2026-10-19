"""Generated from Smithy shape ``com.amazonaws.mpa#ListIdentitySourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.max_results
    import capo_mpa.types.token


class ListIdentitySourcesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_mpa.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""
    next_token: NotRequired["capo_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentitySourcesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListIdentitySourcesRequest:
    out: ListIdentitySourcesRequest = {}  # type: ignore[typeddict-item]
    return out
