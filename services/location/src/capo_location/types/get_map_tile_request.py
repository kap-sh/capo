"""Generated from Smithy shape ``com.amazonaws.location#GetMapTileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.resource_name
    import capo_location.types.sensitive_string


class GetMapTileRequest(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The map resource to retrieve the map tiles from.</p>"""
    z: "capo_location.types.sensitive_string.SensitiveString"
    """<p>The zoom value for the map tile.</p>"""
    x: "capo_location.types.sensitive_string.SensitiveString"
    """<p>The X axis value for the map tile.</p>"""
    y: "capo_location.types.sensitive_string.SensitiveString"
    """<p>The Y axis value for the map tile. </p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapTileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMapTileRequest:
    out: GetMapTileRequest = {}  # type: ignore[typeddict-item]
    return out
