"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ListAgentProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.max_results
    import capo_wellarchitected.types.next_token


class ListAgentProfilesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_wellarchitected.types.max_results.MaxResults"]
    """<p>The maximum number of profiles to return in a single call. Default is 100.</p>"""
    next_token: NotRequired["capo_wellarchitected.types.next_token.NextToken"]
    """<p>A pagination token returned from a previous call to continue retrieving results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAgentProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAgentProfilesRequest:
    out: ListAgentProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
