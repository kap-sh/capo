"""Generated from Smithy shape ``com.amazonaws.continuum#ListAssociatedEnvironmentsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.collector_id
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token


class ListAssociatedEnvironmentsInput(TypedDict, closed=True):
    collector_id: "capo_continuum.types.collector_id.CollectorId"
    """The unique identifier of the Collector whose associations to list."""
    max_results: NotRequired["capo_continuum.types.max_results.MaxResults"]
    """Maximum number of Environment associations to return."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """Pagination token returned by a prior request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedEnvironmentsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedEnvironmentsInput:
    out: ListAssociatedEnvironmentsInput = {}  # type: ignore[typeddict-item]
    return out
