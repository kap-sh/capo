"""Generated from Smithy shape ``com.amazonaws.ivschat#DisconnectUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.reason
    import capo_ivschat.types.room_identifier
    import capo_ivschat.types.user_id


class DisconnectUserRequest(TypedDict, closed=True):
    room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room from which the user's clients should be disconnected. Currently this must be an ARN.</p>"""
    user_id: "capo_ivschat.types.user_id.UserID"
    """<p>ID of the user (connection) to disconnect from the room.</p>"""
    reason: NotRequired["capo_ivschat.types.reason.Reason"]
    """<p>Reason for disconnecting the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisconnectUserRequest) -> dict:
    out: dict = {}
    out["roomIdentifier"] = value["room_identifier"]
    out["userId"] = value["user_id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> DisconnectUserRequest:
    out: DisconnectUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("roomIdentifier") is not None:
        out["room_identifier"] = data["roomIdentifier"]
    else:
        out["room_identifier"] = ""
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out


def redact_sensitive(value: DisconnectUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_id" in value:
        out["user_id"] = "*** Sensitive Data Redacted ***"
    return out
