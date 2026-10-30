"""Generated from Smithy shape ``com.amazonaws.continuum#ListEnvironmentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token


class ListEnvironmentsInput(TypedDict, closed=True):
    max_results: NotRequired["capo_continuum.types.max_results.MaxResults"]
    """The maximum number of results to return in a single call."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEnvironmentsInput:
    out: ListEnvironmentsInput = {}  # type: ignore[typeddict-item]
    return out
