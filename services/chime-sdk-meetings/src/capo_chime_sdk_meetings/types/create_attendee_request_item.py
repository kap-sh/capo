"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateAttendeeRequestItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_capabilities
    import capo_chime_sdk_meetings.types.external_user_id


class CreateAttendeeRequestItem(TypedDict, closed=True):
    external_user_id: "capo_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    r"""<p>The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>"""
    capabilities: NotRequired[
        "capo_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
    ]
    """<p>A list of one or more capabilities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttendeeRequestItem) -> dict:
    out: dict = {}
    out["ExternalUserId"] = value["external_user_id"]
    if "capabilities" in value:
        import capo_chime_sdk_meetings.types.attendee_capabilities

        out["Capabilities"] = (
            capo_chime_sdk_meetings.types.attendee_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAttendeeRequestItem:
    out: CreateAttendeeRequestItem = {}  # type: ignore[typeddict-item]
    if data.get("ExternalUserId") is not None:
        out["external_user_id"] = data["ExternalUserId"]
    else:
        raise DeserializationError(
            "CreateAttendeeRequestItem.external_user_id required"
        )
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_meetings.types.attendee_capabilities

        out["capabilities"] = (
            capo_chime_sdk_meetings.types.attendee_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    return out
