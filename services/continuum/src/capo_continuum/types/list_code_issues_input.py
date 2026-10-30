"""Generated from Smithy shape ``com.amazonaws.continuum#ListCodeIssuesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.max_results
    import capo_continuum.types.next_token


class ListCodeIssuesInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment whose issues to list."""
    max_results: NotRequired["capo_continuum.types.max_results.MaxResults"]
    """The maximum number of results to return in a single call."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """A pagination token returned by a previous call. Set to null for the first request; use the returned token for subsequent calls."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeIssuesInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCodeIssuesInput:
    out: ListCodeIssuesInput = {}  # type: ignore[typeddict-item]
    return out
