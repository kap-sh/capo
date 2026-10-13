"""Generated from Smithy shape ``com.amazonaws.chime#Room``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.iso8601_timestamp
    import capo_chime.types.non_empty_string
    import capo_chime.types.sensitive_string


class Room(TypedDict, closed=True):
    room_id: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The room ID.</p>"""
    name: NotRequired["capo_chime.types.sensitive_string.SensitiveString"]
    """<p>The room name.</p>"""
    account_id: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Chime account ID.</p>"""
    created_by: NotRequired["capo_chime.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the room creator.</p>"""
    created_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The room creation timestamp, in ISO 8601 format.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The room update timestamp, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Room) -> dict:
    out: dict = {}
    if "room_id" in value:
        out["RoomId"] = value["room_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "created_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["CreatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_chime.types.iso8601_timestamp

        out["UpdatedTimestamp"] = capo_chime.types.iso8601_timestamp.serialize_json(
            value["updated_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> Room:
    out: Room = {}  # type: ignore[typeddict-item]
    if data.get("RoomId") is not None:
        out["room_id"] = data["RoomId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["created_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["CreatedTimestamp"]
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime.types.iso8601_timestamp

        out["updated_timestamp"] = capo_chime.types.iso8601_timestamp.deserialize_json(
            data["UpdatedTimestamp"]
        )
    return out


def redact_sensitive(value: Room) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
