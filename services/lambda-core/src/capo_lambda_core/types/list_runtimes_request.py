"""Generated from Smithy shape ``com.amazonaws.lambdacore#ListRuntimesRequest``."""

from typing_extensions import NotRequired, TypedDict


class ListRuntimesRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """The pagination token from a previous response. Use it to retrieve the next page of results."""
    max_results: NotRequired["int"]
    """The maximum number of runtimes to return per page. Valid range: 1 to 100."""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuntimesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRuntimesRequest:
    out: ListRuntimesRequest = {}  # type: ignore[typeddict-item]
    return out
