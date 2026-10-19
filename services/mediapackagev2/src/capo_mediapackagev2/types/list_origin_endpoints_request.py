"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#ListOriginEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.list_resource_max_results
    import capo_mediapackagev2.types.resource_name


class ListOriginEndpointsRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel group. The name is the primary identifier for the channel group, and must be unique for your account in the AWS Region.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name that describes the channel. The name is the primary identifier for the channel, and must be unique for your account in the AWS Region and channel group. </p>"""
    max_results: NotRequired[
        "capo_mediapackagev2.types.list_resource_max_results.ListResourceMaxResults"
    ]
    """<p>The maximum number of results to return in the response.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token from the GET list request. Use the token to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOriginEndpointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListOriginEndpointsRequest:
    out: ListOriginEndpointsRequest = {}  # type: ignore[typeddict-item]
    return out
