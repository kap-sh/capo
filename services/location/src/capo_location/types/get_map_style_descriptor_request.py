"""Generated from Smithy shape ``com.amazonaws.location#GetMapStyleDescriptorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.resource_name


class GetMapStyleDescriptorRequest(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The map resource to retrieve the style descriptor from.</p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapStyleDescriptorRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMapStyleDescriptorRequest:
    out: GetMapStyleDescriptorRequest = {}  # type: ignore[typeddict-item]
    return out
