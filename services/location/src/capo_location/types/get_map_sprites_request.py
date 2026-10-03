"""Generated from Smithy shape ``com.amazonaws.location#GetMapSpritesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.resource_name


class GetMapSpritesRequest(TypedDict, closed=True):
    map_name: "capo_location.types.resource_name.ResourceName"
    """<p>The map resource associated with the sprite ﬁle.</p>"""
    file_name: "str"
    """<p>The name of the sprite ﬁle. Use the following ﬁle names for the sprite sheet:</p> <ul> <li> <p> <code>sprites.png</code> </p> </li> <li> <p> <code>sprites@2x.png</code> for high pixel density displays</p> </li> </ul> <p>For the JSON document containing image offsets. Use the following ﬁle names:</p> <ul> <li> <p> <code>sprites.json</code> </p> </li> <li> <p> <code>sprites@2x.json</code> for high pixel density displays</p> </li> </ul>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMapSpritesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMapSpritesRequest:
    out: GetMapSpritesRequest = {}  # type: ignore[typeddict-item]
    return out
