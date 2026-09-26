"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListTemplatesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.entity_status_filter
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token


class ListTemplatesInput(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_network_security_manager.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>"""
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""
    status: NotRequired[
        "capo_network_security_manager.types.entity_status_filter.EntityStatusFilter"
    ]
    """<p>Filters the results by status, either <code>ACTIVE</code> or <code>DRAFT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTemplatesInput:
    out: ListTemplatesInput = {}  # type: ignore[typeddict-item]
    return out
