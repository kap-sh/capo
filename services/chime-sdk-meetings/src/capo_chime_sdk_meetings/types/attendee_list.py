"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#AttendeeList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee

AttendeeList: TypeAlias = list["capo_chime_sdk_meetings.types.attendee.Attendee"]


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeList) -> list:
    import capo_chime_sdk_meetings.types.attendee

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_meetings.types.attendee.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttendeeList:
    import capo_chime_sdk_meetings.types.attendee

    out: AttendeeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_meetings.types.attendee.deserialize_json(item))
    return out


def redact_sensitive(value: AttendeeList) -> list[Any]:
    import capo_chime_sdk_meetings.types.attendee

    return [
        capo_chime_sdk_meetings.types.attendee.redact_sensitive(item) for item in value
    ]
