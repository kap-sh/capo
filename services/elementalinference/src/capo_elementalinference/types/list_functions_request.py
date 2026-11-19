"""Generated from Smithy shape ``com.amazonaws.elementalinference#ListFunctionsRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListFunctionsRequest(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of functions to return in one response. Valid range: 1 to 100. The default is 100. </p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the page of results to return. Use the nextToken value from a previous response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListFunctionsRequest:
    out: ListFunctionsRequest = {}  # type: ignore[typeddict-item]
    return out
