"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ListAttendeesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_list
    import capo_chime_sdk_meetings.types.string


class ListAttendeesResponse(TypedDict, closed=True):
    attendees: NotRequired["capo_chime_sdk_meetings.types.attendee_list.AttendeeList"]
    """<p>The Amazon Chime SDK attendee information.</p>"""
    next_token: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAttendeesResponse) -> dict:
    out: dict = {}
    if "attendees" in value:
        import capo_chime_sdk_meetings.types.attendee_list

        out["Attendees"] = capo_chime_sdk_meetings.types.attendee_list.serialize_json(
            value["attendees"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAttendeesResponse:
    out: ListAttendeesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Attendees") is not None:
        import capo_chime_sdk_meetings.types.attendee_list

        out["attendees"] = capo_chime_sdk_meetings.types.attendee_list.deserialize_json(
            data["Attendees"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListAttendeesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attendees" in value:
        import capo_chime_sdk_meetings.types.attendee_list

        out["attendees"] = capo_chime_sdk_meetings.types.attendee_list.redact_sensitive(
            value["attendees"]
        )
    return out
