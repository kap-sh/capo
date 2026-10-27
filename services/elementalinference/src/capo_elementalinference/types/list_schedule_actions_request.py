"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListScheduleActionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.feed_id


class ListScheduleActionsRequest(TypedDict, closed=True):
    id: "capo_elementalinference.types.feed_id.FeedId"
    """<p>The ID of the feed that you want to query.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return for each API request. If you don't specify MaxResults, Elemental Inference returns a maximum of 10 results for each page. </p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the batch of results that you want to see. To see the next batch, submit the request a second time and specify the NextToken value that Elemental Inference returned. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListScheduleActionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListScheduleActionsRequest:
    out: ListScheduleActionsRequest = {}  # type: ignore[typeddict-item]
    return out
