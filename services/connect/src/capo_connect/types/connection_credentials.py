"""Generated from Smithy shape ``com.amazonaws.connect#ConnectionCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.iso8601_datetime
    import capo_connect.types.participant_token


class ConnectionCredentials(TypedDict, closed=True):
    connection_token: NotRequired[
        "capo_connect.types.participant_token.ParticipantToken"
    ]
    """<p>The connection token used by the chat participant to call the Connect Customer Participant Service.</p>"""
    expiry: NotRequired["capo_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The expiration of the token. It's specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionCredentials) -> dict:
    out: dict = {}
    if "connection_token" in value:
        out["ConnectionToken"] = value["connection_token"]
    if "expiry" in value:
        out["Expiry"] = value["expiry"]
    return out


def deserialize_json(data: dict) -> ConnectionCredentials:
    out: ConnectionCredentials = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionToken") is not None:
        out["connection_token"] = data["ConnectionToken"]
    if data.get("Expiry") is not None:
        out["expiry"] = data["Expiry"]
    return out
