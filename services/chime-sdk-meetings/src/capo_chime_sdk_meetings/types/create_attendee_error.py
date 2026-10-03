"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#CreateAttendeeError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_meetings.types.external_user_id
    import capo_chime_sdk_meetings.types.string


class CreateAttendeeError(TypedDict, closed=True):
    external_user_id: NotRequired[
        "capo_chime_sdk_meetings.types.external_user_id.ExternalUserId"
    ]
    r"""<p>The Amazon Chime SDK external user ID. An idempotency token. Links the attendee to an identity managed by a builder application.</p> <p>Pattern: <code>[-_&@+=,(){}\[\]\/«».:|'"#a-zA-Z0-9À-ÿ\s]*</code> </p> <p>Values that begin with <code>aws:</code> are reserved. You can't configure a value that uses this prefix. Case insensitive.</p>"""
    error_code: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The error code.</p>"""
    error_message: NotRequired["capo_chime_sdk_meetings.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAttendeeError) -> dict:
    out: dict = {}
    if "external_user_id" in value:
        out["ExternalUserId"] = value["external_user_id"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> CreateAttendeeError:
    out: CreateAttendeeError = {}  # type: ignore[typeddict-item]
    if data.get("ExternalUserId") is not None:
        out["external_user_id"] = data["ExternalUserId"]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
