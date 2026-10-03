"""Generated from Smithy shape ``com.amazonaws.ivschat#DeleteMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivschat.types.message_id
    import capo_ivschat.types.reason
    import capo_ivschat.types.room_identifier


class DeleteMessageRequest(TypedDict, closed=True):
    room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room where the message should be deleted. Currently this must be an ARN. </p>"""
    id: "capo_ivschat.types.message_id.MessageID"
    """<p>ID of the message to be deleted. This is the <code>Id</code> field in the received message (see <a href="https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-message-subscribe.html"> Message (Subscribe)</a> in the Chat Messaging API).</p>"""
    reason: NotRequired["capo_ivschat.types.reason.Reason"]
    """<p>Reason for deleting the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMessageRequest) -> dict:
    out: dict = {}
    out["roomIdentifier"] = value["room_identifier"]
    out["id"] = value["id"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> DeleteMessageRequest:
    out: DeleteMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("roomIdentifier") is not None:
        out["room_identifier"] = data["roomIdentifier"]
    else:
        raise DeserializationError("DeleteMessageRequest.room_identifier required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteMessageRequest.id required")
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
