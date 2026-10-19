"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxUsersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.id_type
    import capo_finspace.types.pagination_token
    import capo_finspace.types.result_limit


class ListKxUsersRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.id_type.IdType"
    """<p>A unique identifier for the kdb environment.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    max_results: NotRequired["capo_finspace.types.result_limit.ResultLimit"]
    """<p>The maximum number of results to return in this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxUsersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxUsersRequest:
    out: ListKxUsersRequest = {}  # type: ignore[typeddict-item]
    return out
