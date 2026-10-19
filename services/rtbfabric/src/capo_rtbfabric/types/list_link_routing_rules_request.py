"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ListLinkRoutingRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.gateway_id
    import capo_rtbfabric.types.link_id


class ListLinkRoutingRulesRequest(TypedDict, closed=True):
    gateway_id: "capo_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    next_token: NotRequired["str"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an <i>HTTP 400 InvalidToken error</i>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that are returned per call. You can use <code>nextToken</code> to obtain further pages of results.</p> <p>This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinkRoutingRulesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLinkRoutingRulesRequest:
    out: ListLinkRoutingRulesRequest = {}  # type: ignore[typeddict-item]
    return out
