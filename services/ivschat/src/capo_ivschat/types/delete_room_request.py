"""Generated from Smithy shape ``com.amazonaws.ivschat#DeleteRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.room_identifier


class DeleteRoomRequest(TypedDict, closed=True):
    identifier: "capo_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room to be deleted. Currently this must be an ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRoomRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> DeleteRoomRequest:
    out: DeleteRoomRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
