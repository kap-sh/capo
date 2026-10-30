"""Generated from Smithy shape ``com.amazonaws.continuum#ListAssociatedCollectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token


class ListAssociatedCollectorsInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The unique identifier of the Environment whose associations to list."""
    max_results: NotRequired["capo_continuum.types.max_results.MaxResults"]
    """Maximum number of associated Collectors to return."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """Pagination token returned by a prior request."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedCollectorsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssociatedCollectorsInput:
    out: ListAssociatedCollectorsInput = {}  # type: ignore[typeddict-item]
    return out
