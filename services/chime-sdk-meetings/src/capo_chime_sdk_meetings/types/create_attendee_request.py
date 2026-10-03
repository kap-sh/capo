"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateAttendeeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_meetings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.attendee_capabilities
    import capo_chime_sdk_meetings.types.external_user_id
    import capo_chime_sdk_meetings.types.guid_string


class CreateAttendeeRequest(TypedDict, closed=True):
    meeting_id: "capo_chime_sdk_meetings.types.guid_string.GuidString"
    """<p>The unique ID of the meeting.</p>"""
    external_user_id: "capo_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    r"""<p>The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix.</p>"""
    capabilities: NotRequired[
        "capo_chime_sdk_meetings.types.attendee_capabilities.AttendeeCapabilities"
    ]
    """<p>The capabilities (<code>audio</code>, <code>video</code>, or <code>content</code>) that you want to grant an attendee. If you don't specify capabilities, all users have send and receive capabilities on all media channels by default.</p> <note> <p>You use the capabilities with a set of values that control what the capabilities can do, such as <code>SendReceive</code> data. For more information about those values, see .</p> </note> <p>When using capabilities, be aware of these corner cases:</p> <ul> <li> <p>If you specify <code>MeetingFeatures:Video:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Video</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>If you specify <code>MeetingFeatures:Content:MaxResolution:None</code> when you create a meeting, all API requests that include <code>SendReceive</code>, <code>Send</code>, or <code>Receive</code> for <code>AttendeeCapabilities:Content</code> will be rejected with <code>ValidationError 400</code>.</p> </li> <li> <p>You can't set <code>content</code> capabilities to <code>SendReceive</code> or <code>Receive</code> unless you also set <code>video</code> capabilities to <code>SendReceive</code> or <code>Receive</code>. If you don't set the <code>video</code> capability to receive, the response will contain an HTTP 400 Bad Request status code. However, you can set your <code>video</code> capability to receive and you set your <code>content</code> capability to not receive.</p> </li> <li> <p>If meeting features is defined as <code>Video:MaxResolution:None</code> but <code>Content:MaxResolution</code> is defined as something other than <code>None</code> and attendee capabilities are not defined in the API request, then the default attendee video capability is set to <code>Receive</code> and attendee content capability is set to <code>SendReceive</code>. This is because content <code>SendReceive</code> requires video to be at least <code>Receive</code>.</p> </li> <li> <p>When you change an <code>audio</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee left their microphone unmuted, audio will flow from the attendee to the other meeting participants.</p> </li> <li> <p>When you change a <code>video</code> or <code>content</code> capability from <code>None</code> or <code>Receive</code> to <code>Send</code> or <code>SendReceive</code> , and if the attendee turned on their video or content streams, remote attendees can receive those streams, but only after media renegotiation between the client and the Amazon Chime back-end server.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttendeeRequest) -> dict:
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


def deserialize_json(data: dict) -> CreateAttendeeRequest:
    out: CreateAttendeeRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExternalUserId") is not None:
        out["external_user_id"] = data["ExternalUserId"]
    else:
        raise DeserializationError("CreateAttendeeRequest.external_user_id required")
    if data.get("Capabilities") is not None:
        import capo_chime_sdk_meetings.types.attendee_capabilities

        out["capabilities"] = (
            capo_chime_sdk_meetings.types.attendee_capabilities.deserialize_json(
                data["Capabilities"]
            )
        )
    return out
