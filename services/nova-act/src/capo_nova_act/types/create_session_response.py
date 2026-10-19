"""Generated from Smithy shape ``com.amazonaws.novaact#CreateSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_nova_act.types.uuid_string


class CreateSessionResponse(TypedDict, closed=True):
    session_id: "capo_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier for the created session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSessionResponse) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> CreateSessionResponse:
    out: CreateSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    return out
