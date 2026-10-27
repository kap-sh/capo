"""Generated from Smithy shape ``com.amazonaws.deadline#ListLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.max_results
    import capo_deadline.types.next_token


class ListLimitsRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The unique identifier of the farm that contains the limits."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """The token for the next set of results, or <code>null</code> to start from the beginning."""
    max_results: NotRequired["capo_deadline.types.max_results.MaxResults"]
    """The maximum number of limits to return in each page of results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListLimitsRequest:
    out: ListLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
