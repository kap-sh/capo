"""Generated from Smithy shape ``com.amazonaws.chime#CreateMeetingDialOutRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.e164_phone_number
    import capo_chime.types.guid_string
    import capo_chime.types.join_token_string


class CreateMeetingDialOutRequest(TypedDict, closed=True):
    meeting_id: "capo_chime.types.guid_string.GuidString"
    """<p>The Amazon Chime SDK meeting ID.</p>"""
    from_phone_number: "capo_chime.types.e164_phone_number.E164PhoneNumber"
    """<p>Phone number used as the caller ID when the remote party receives a call.</p>"""
    to_phone_number: "capo_chime.types.e164_phone_number.E164PhoneNumber"
    """<p>Phone number called when inviting someone to a meeting.</p>"""
    join_token: "capo_chime.types.join_token_string.JoinTokenString"
    """<p>Token used by the Amazon Chime SDK attendee. Call the <a href="https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateAttendee.html">CreateAttendee</a> action to get a join token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMeetingDialOutRequest) -> dict:
    out: dict = {}
    out["FromPhoneNumber"] = value["from_phone_number"]
    out["ToPhoneNumber"] = value["to_phone_number"]
    out["JoinToken"] = value["join_token"]
    return out


def deserialize_json(data: dict) -> CreateMeetingDialOutRequest:
    out: CreateMeetingDialOutRequest = {}  # type: ignore[typeddict-item]
    if data.get("FromPhoneNumber") is not None:
        out["from_phone_number"] = data["FromPhoneNumber"]
    else:
        raise DeserializationError(
            "CreateMeetingDialOutRequest.from_phone_number required"
        )
    if data.get("ToPhoneNumber") is not None:
        out["to_phone_number"] = data["ToPhoneNumber"]
    else:
        raise DeserializationError(
            "CreateMeetingDialOutRequest.to_phone_number required"
        )
    if data.get("JoinToken") is not None:
        out["join_token"] = data["JoinToken"]
    else:
        raise DeserializationError("CreateMeetingDialOutRequest.join_token required")
    return out
