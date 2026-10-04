"""Generated from Smithy shape ``com.amazonaws.connect#Websocket``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.iso8601_datetime
    import capo_connect.types.pre_signed_connection_url


class Websocket(TypedDict, closed=True):
    url: NotRequired[
        "capo_connect.types.pre_signed_connection_url.PreSignedConnectionUrl"
    ]
    """<p>The URL of the websocket.</p>"""
    connection_expiry: NotRequired[
        "capo_connect.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The expiration of the websocket URL. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Websocket) -> dict:
    out: dict = {}
    if "url" in value:
        out["Url"] = value["url"]
    if "connection_expiry" in value:
        out["ConnectionExpiry"] = value["connection_expiry"]
    return out


def deserialize_json(data: dict) -> Websocket:
    out: Websocket = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    if data.get("ConnectionExpiry") is not None:
        out["connection_expiry"] = data["ConnectionExpiry"]
    return out
