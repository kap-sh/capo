"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#BatchCreateAttendeeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.create_attendee_request_item_list
    import capo_chime_sdk_meetings.types.guid_string


class BatchCreateAttendeeRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK ID of the meeting to which you're adding attendees.</p>"""
    attendees: "capo_chime_sdk_meetings.types.create_attendee_request_item_list.CreateAttendeeRequestItemList"
    """<p>The attendee information, including attendees' IDs and join tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateAttendeeRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_meetings.types.create_attendee_request_item_list

    out["Attendees"] = (
        capo_chime_sdk_meetings.types.create_attendee_request_item_list.serialize_json(
            value["attendees"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchCreateAttendeeRequest:
    out: BatchCreateAttendeeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Attendees") is not None:
        import capo_chime_sdk_meetings.types.create_attendee_request_item_list

        out["attendees"] = (
            capo_chime_sdk_meetings.types.create_attendee_request_item_list.deserialize_json(
                data["Attendees"]
            )
        )
    else:
        out["attendees"] = []
    return out


def redact_sensitive(value: BatchCreateAttendeeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attendees" in value:
        import capo_chime_sdk_meetings.types.create_attendee_request_item_list

        out["attendees"] = (
            capo_chime_sdk_meetings.types.create_attendee_request_item_list.redact_sensitive(
                value["attendees"]
            )
        )
    return out
