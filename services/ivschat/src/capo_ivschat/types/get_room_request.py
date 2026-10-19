"""Generated from Smithy shape ``com.amazonaws.ivschat#GetRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.room_identifier


class GetRoomRequest(TypedDict, closed=True):
    identifier: "capo_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room for which the configuration is to be retrieved. Currently this must be an ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRoomRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_json(data: dict) -> GetRoomRequest:
    out: GetRoomRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
