"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateMeetingWithAttendeesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_list
    import capo_chime_sdk_meetings.types.batch_create_attendee_error_list
    import capo_chime_sdk_meetings.types.meeting


class CreateMeetingWithAttendeesResponse(TypedDict, closed=True):
    meeting: NotRequired["capo_chime_sdk_meetings.types.meeting.Meeting"]
    """<p>The meeting information, including the meeting ID and <code>MediaPlacement</code>.</p>"""
    attendees: NotRequired["capo_chime_sdk_meetings.types.attendee_list.AttendeeList"]
    """<p>The attendee information, including attendees' IDs and join tokens.</p>"""
    errors: NotRequired[
        "capo_chime_sdk_meetings.types.batch_create_attendee_error_list.BatchCreateAttendeeErrorList"
    ]
    """<p>If the action fails for one or more of the attendees in the request, a list of the attendees is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingWithAttendeesResponse) -> dict:
    out: dict = {}
    if "meeting" in value:
        import capo_chime_sdk_meetings.types.meeting

        out["Meeting"] = capo_chime_sdk_meetings.types.meeting.serialize_json(
            value["meeting"]
        )
    if "attendees" in value:
        import capo_chime_sdk_meetings.types.attendee_list

        out["Attendees"] = capo_chime_sdk_meetings.types.attendee_list.serialize_json(
            value["attendees"]
        )
    if "errors" in value:
        import capo_chime_sdk_meetings.types.batch_create_attendee_error_list

        out["Errors"] = (
            capo_chime_sdk_meetings.types.batch_create_attendee_error_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMeetingWithAttendeesResponse:
    out: CreateMeetingWithAttendeesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Meeting") is not None:
        import capo_chime_sdk_meetings.types.meeting

        out["meeting"] = capo_chime_sdk_meetings.types.meeting.deserialize_json(
            data["Meeting"]
        )
    if data.get("Attendees") is not None:
        import capo_chime_sdk_meetings.types.attendee_list

        out["attendees"] = capo_chime_sdk_meetings.types.attendee_list.deserialize_json(
            data["Attendees"]
        )
    if data.get("Errors") is not None:
        import capo_chime_sdk_meetings.types.batch_create_attendee_error_list

        out["errors"] = (
            capo_chime_sdk_meetings.types.batch_create_attendee_error_list.deserialize_json(
                data["Errors"]
            )
        )
    return out


def redact_sensitive(value: CreateMeetingWithAttendeesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "meeting" in value:
        import capo_chime_sdk_meetings.types.meeting

        out["meeting"] = capo_chime_sdk_meetings.types.meeting.redact_sensitive(
            value["meeting"]
        )
    if "attendees" in value:
        import capo_chime_sdk_meetings.types.attendee_list

        out["attendees"] = capo_chime_sdk_meetings.types.attendee_list.redact_sensitive(
            value["attendees"]
        )
    if "errors" in value:
        import capo_chime_sdk_meetings.types.batch_create_attendee_error_list

        out["errors"] = (
            capo_chime_sdk_meetings.types.batch_create_attendee_error_list.redact_sensitive(
                value["errors"]
            )
        )
    return out
