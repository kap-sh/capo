"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#BatchUpdateAttendeeCapabilitiesExceptRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_capabilities
    import capo_chime_sdk_meetings.types.attendee_ids_list
    import capo_chime_sdk_meetings.types.guid_string


class BatchUpdateAttendeeCapabilitiesExceptRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The ID of the meeting associated with the update request.</p>"""
    excluded_attendee_ids: (
        "capo_chime_sdk_meetings.types.attendee_ids_list.AttendeeIdsList"
    )
    """<p>The <code>AttendeeIDs</code> that you want to exclude from one or more capabilities.</p>"""
    capabilities: (
        "capo_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
    )
    """<p>The capabilities (<code>audio</code>, <code>video</code>, or <code>content</code>) that you want to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateAttendeeCapabilitiesExceptRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_meetings.types.attendee_ids_list

    out["ExcludedAttendeeIds"] = (
        capo_chime_sdk_meetings.types.attendee_ids_list.serialize_json(
            value["excluded_attendee_ids"]
        )
    )
    import capo_chime_sdk_meetings.types.attendee_capabilities

    out["Capabilities"] = (
        capo_chime_sdk_meetings.types.attendee_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateAttendeeCapabilitiesExceptRequest:
    out: BatchUpdateAttendeeCapabilitiesExceptRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExcludedAttendeeIds") is not None:
        import capo_chime_sdk_meetings.types.attendee_ids_list

        out["excluded_attendee_ids"] = (
            capo_chime_sdk_meetings.types.attendee_ids_list.deserialize_json(
                data["ExcludedAttendeeIds"]
            )
        )
    else:
        out["excluded_attendee_ids"] = []
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_meetings.types.attendee_capabilities

        out["capabilities"] = (
            capo_chime_sdk_meetings.types.attendee_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateAttendeeCapabilitiesExceptRequest.capabilities required"
        )
    return out
