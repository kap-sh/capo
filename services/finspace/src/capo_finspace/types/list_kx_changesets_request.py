"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxChangesetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.database_name
    import capo_finspace.types.environment_id
    import capo_finspace.types.max_results
    import capo_finspace.types.pagination_token


class ListKxChangesetsRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "capo_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: NotRequired["capo_finspace.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxChangesetsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxChangesetsRequest:
    out: ListKxChangesetsRequest = {}  # type: ignore[typeddict-item]
    return out
