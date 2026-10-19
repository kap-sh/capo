"""Generated from Smithy shape ``com.amazonaws.finspace#ListKxVolumesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.kx_environment_id
    import capo_finspace.types.kx_volume_type
    import capo_finspace.types.max_results
    import capo_finspace.types.pagination_token


class ListKxVolumesRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.kx_environment_id.KxEnvironmentId"
    """<p>A unique identifier for the kdb environment, whose clusters can attach to the volume. </p>"""
    max_results: NotRequired["capo_finspace.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in this request.</p>"""
    next_token: NotRequired["capo_finspace.types.pagination_token.PaginationToken"]
    """<p>A token that indicates where a results page should begin.</p>"""
    volume_type: NotRequired["capo_finspace.types.kx_volume_type.KxVolumeType"]
    """<p> The type of file system volume. Currently, FinSpace only supports <code>NAS_1</code> volume type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKxVolumesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKxVolumesRequest:
    out: ListKxVolumesRequest = {}  # type: ignore[typeddict-item]
    return out
