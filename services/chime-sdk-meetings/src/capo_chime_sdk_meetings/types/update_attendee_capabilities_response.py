"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#UpdateAttendeeCapabilitiesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee


class UpdateAttendeeCapabilitiesResponse(TypedDict, closed=True):
    attendee: NotRequired["capo_chime_sdk_meetings.types.attendee.Attendee"]
    """<p>The updated attendee data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAttendeeCapabilitiesResponse) -> dict:
    out: dict = {}
    if "attendee" in value:
        import capo_chime_sdk_meetings.types.attendee

        out["Attendee"] = capo_chime_sdk_meetings.types.attendee.serialize_json(
            value["attendee"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAttendeeCapabilitiesResponse:
    out: UpdateAttendeeCapabilitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Attendee") is not None:
        import capo_chime_sdk_meetings.types.attendee

        out["attendee"] = capo_chime_sdk_meetings.types.attendee.deserialize_json(
            data["Attendee"]
        )
    return out


def redact_sensitive(value: UpdateAttendeeCapabilitiesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "attendee" in value:
        import capo_chime_sdk_meetings.types.attendee

        out["attendee"] = capo_chime_sdk_meetings.types.attendee.redact_sensitive(
            value["attendee"]
        )
    return out
