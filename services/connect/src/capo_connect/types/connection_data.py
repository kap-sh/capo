"""Generated from Smithy shape ``com.amazonaws.connect#ConnectionData``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attendee
    import capo_connect.types.meeting


class ConnectionData(TypedDict, closed=True):
    attendee: NotRequired["capo_connect.types.attendee.Attendee"]
    """<p>The attendee information, including attendee ID and join token.</p>"""
    meeting: NotRequired["capo_connect.types.meeting.Meeting"]
    """<p>A meeting created using the Amazon Chime SDK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionData) -> dict:
    out: dict = {}
    if "attendee" in value:
        import capo_connect.types.attendee

        out["Attendee"] = capo_connect.types.attendee.serialize_json(value["attendee"])
    if "meeting" in value:
        import capo_connect.types.meeting

        out["Meeting"] = capo_connect.types.meeting.serialize_json(value["meeting"])
    return out


def deserialize_json(data: dict) -> ConnectionData:
    out: ConnectionData = {}  # type: ignore[typeddict-item]
    if data.get("Attendee") is not None:
        import capo_connect.types.attendee

        out["attendee"] = capo_connect.types.attendee.deserialize_json(data["Attendee"])
    if data.get("Meeting") is not None:
        import capo_connect.types.meeting

        out["meeting"] = capo_connect.types.meeting.deserialize_json(data["Meeting"])
    return out


def redact_sensitive(value: ConnectionData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attendee" in value:
        import capo_connect.types.attendee

        out["attendee"] = capo_connect.types.attendee.redact_sensitive(
            value["attendee"]
        )
    return out
