"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#BatchCreateAttendeeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_list
    import capo_chime_sdk_meetings.types.batch_create_attendee_error_list


class BatchCreateAttendeeResponse(TypedDict, closed=True):
    attendees: NotRequired["capo_chime_sdk_meetings.types.attendee_list.AttendeeList"]
    """<p>The attendee information, including attendees' IDs and join tokens.</p>"""
    errors: NotRequired[
        "capo_chime_sdk_meetings.types.batch_create_attendee_error_list.BatchCreateAttendeeErrorList"
    ]
    """<p>If the action fails for one or more of the attendees in the request, a list of the attendees is returned, along with error codes and error messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateAttendeeResponse) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> BatchCreateAttendeeResponse:
    out: BatchCreateAttendeeResponse = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: BatchCreateAttendeeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
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
