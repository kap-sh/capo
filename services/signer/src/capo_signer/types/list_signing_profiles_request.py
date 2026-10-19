"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.bool
    import capo_signer.types.max_results
    import capo_signer.types.next_token
    import capo_signer.types.platform_id
    import capo_signer.types.statuses


class ListSigningProfilesRequest(TypedDict, closed=True):
    include_canceled: NotRequired["capo_signer.types.bool.bool"]
    """<p>Designates whether to include profiles with the status of <code>CANCELED</code>.</p>"""
    max_results: NotRequired["capo_signer.types.max_results.MaxResults"]
    """<p>The maximum number of profiles to be returned.</p>"""
    next_token: NotRequired["capo_signer.types.next_token.NextToken"]
    """<p>Value for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.</p>"""
    platform_id: NotRequired["capo_signer.types.platform_id.PlatformId"]
    """<p>Filters results to return only signing jobs initiated for a specified signing platform.</p>"""
    statuses: NotRequired["capo_signer.types.statuses.Statuses"]
    """<p>Filters results to return only signing jobs with statuses in the specified list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSigningProfilesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSigningProfilesRequest:
    out: ListSigningProfilesRequest = {}  # type: ignore[typeddict-item]
    return out
