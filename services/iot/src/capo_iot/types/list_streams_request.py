"""Generated from Smithy shape ``com.amazonaws.iot#ListStreamsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.ascending_order
    import capo_iot.types.max_results
    import capo_iot.types.next_token


class ListStreamsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at a time.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>A token used to get the next set of results.</p>"""
    ascending_order: NotRequired["capo_iot.types.ascending_order.AscendingOrder"]
    """<p>Set to true to return the list of streams in ascending order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListStreamsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListStreamsRequest:
    out: ListStreamsRequest = {}  # type: ignore[typeddict-item]
    return out
