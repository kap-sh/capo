"""Generated from Smithy shape ``com.amazonaws.chime#UpdateRoomRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.sensitive_string


class UpdateRoomRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    room_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The room ID.</p>"""
    name: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The room name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoomRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateRoomRequest:
    out: UpdateRoomRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


def redact_sensitive(value: UpdateRoomRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
