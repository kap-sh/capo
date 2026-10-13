"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.meeting


class CreateMeetingResponse(TypedDict, closed=True):
    meeting: NotRequired["capo_chime_sdk_meetings.types.meeting.Meeting"]
    """<p>The meeting information, including the meeting ID and <code>MediaPlacement</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingResponse) -> dict:
    out: dict = {}
    if "meeting" in value:
        import capo_chime_sdk_meetings.types.meeting

        out["Meeting"] = capo_chime_sdk_meetings.types.meeting.serialize_json(
            value["meeting"]
        )
    return out


def deserialize_json(data: dict) -> CreateMeetingResponse:
    out: CreateMeetingResponse = {}  # type: ignore[typeddict-item]
    if data.get("Meeting") is not None:
        import capo_chime_sdk_meetings.types.meeting

        out["meeting"] = capo_chime_sdk_meetings.types.meeting.deserialize_json(
            data["Meeting"]
        )
    return out


def redact_sensitive(value: CreateMeetingResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "meeting" in value:
        import capo_chime_sdk_meetings.types.meeting

        out["meeting"] = capo_chime_sdk_meetings.types.meeting.redact_sensitive(
            value["meeting"]
        )
    return out
