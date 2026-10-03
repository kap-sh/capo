"""Generated from Smithy shape ``com.amazonaws.connect#StartChatContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.participant_id
    import capo_connect.types.participant_token


class StartChatContactResponse(TypedDict, closed=True):
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of this contact within the Connect Customer instance. </p>"""
    participant_id: NotRequired["capo_connect.types.participant_id.ParticipantId"]
    """<p>The identifier for a chat participant. The participantId for a chat participant is the same throughout the chat lifecycle.</p>"""
    participant_token: NotRequired[
        "capo_connect.types.participant_token.ParticipantToken"
    ]
    """<p>The token used by the chat participant to call <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html">CreateParticipantConnection</a>. The participant token is valid for the lifetime of a chat participant.</p>"""
    continued_from_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The contactId from which a persistent chat session is started. This field is populated only for persistent chats.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChatContactResponse) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "participant_token" in value:
        out["ParticipantToken"] = value["participant_token"]
    if "continued_from_contact_id" in value:
        out["ContinuedFromContactId"] = value["continued_from_contact_id"]
    return out


def deserialize_json(data: dict) -> StartChatContactResponse:
    out: StartChatContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    if data.get("ParticipantId") is not None:
        out["participant_id"] = data["ParticipantId"]
    if data.get("ParticipantToken") is not None:
        out["participant_token"] = data["ParticipantToken"]
    if data.get("ContinuedFromContactId") is not None:
        out["continued_from_contact_id"] = data["ContinuedFromContactId"]
    return out
