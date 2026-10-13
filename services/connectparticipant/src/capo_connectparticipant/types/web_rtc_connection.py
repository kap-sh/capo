"""Generated from Smithy shape ``com.amazonaws.connectparticipant#WebRTCConnection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.attendee
    import capo_connectparticipant.types.web_rtc_meeting


class WebRTCConnection(TypedDict, closed=True):
    attendee: NotRequired["capo_connectparticipant.types.attendee.Attendee"]
    meeting: NotRequired["capo_connectparticipant.types.web_rtc_meeting.WebRTCMeeting"]
    """<p>A meeting created using the Amazon Chime SDK.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebRTCConnection) -> dict:
    out: dict = {}
    if "attendee" in value:
        import capo_connectparticipant.types.attendee

        out["Attendee"] = capo_connectparticipant.types.attendee.serialize_json(
            value["attendee"]
        )
    if "meeting" in value:
        import capo_connectparticipant.types.web_rtc_meeting

        out["Meeting"] = capo_connectparticipant.types.web_rtc_meeting.serialize_json(
            value["meeting"]
        )
    return out


def deserialize_json(data: dict) -> WebRTCConnection:
    out: WebRTCConnection = {}  # type: ignore[typeddict-item]
    if data.get("Attendee") is not None:
        import capo_connectparticipant.types.attendee

        out["attendee"] = capo_connectparticipant.types.attendee.deserialize_json(
            data["Attendee"]
        )
    if data.get("Meeting") is not None:
        import capo_connectparticipant.types.web_rtc_meeting

        out["meeting"] = capo_connectparticipant.types.web_rtc_meeting.deserialize_json(
            data["Meeting"]
        )
    return out


def redact_sensitive(value: WebRTCConnection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attendee" in value:
        import capo_connectparticipant.types.attendee

        out["attendee"] = capo_connectparticipant.types.attendee.redact_sensitive(
            value["attendee"]
        )
    return out
