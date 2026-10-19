"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxScalingGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.max_results
    import capo_finspace.types.pagination_token


class ListKxScalingGroupsRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, for which you want to retrieve a list of scaling groups.</p>"""
    max_results: NotRequired["capo_finspace.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this request.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p> A token that indicates where a results page should begin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxScalingGroupsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxScalingGroupsRequest:
    out: ListKxScalingGroupsRequest = {}  # type: ignore[typeddict-item]
    return out
