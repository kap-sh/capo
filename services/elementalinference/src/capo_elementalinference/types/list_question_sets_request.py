"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListQuestionSetsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListQuestionSetsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per API request. Valid range: 1 to 100.</p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the next batch of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQuestionSetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListQuestionSetsRequest:
    out: ListQuestionSetsRequest = {}  # type: ignore[typeddict-item]
    return out
