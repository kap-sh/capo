"""Generated from Smithy shape ``com.amazonaws.connect#StartWebRTCContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.connection_data
    import capo_connect.types.contact_id
    import capo_connect.types.participant_id
    import capo_connect.types.participant_token


class StartWebRTCContactResponse(TypedDict, closed=True):
    connection_data: NotRequired["capo_connect.types.connection_data.ConnectionData"]
    """<p>Information required for the client application (mobile application or website) to connect to the call.</p>"""
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    participant_id: NotRequired["capo_connect.types.participant_id.ParticipantId"]
    """<p>The identifier for a contact participant. The <code>ParticipantId</code> for a contact participant is the same throughout the contact lifecycle.</p>"""
    participant_token: NotRequired[
        "capo_connect.types.participant_token.ParticipantToken"
    ]
    """<p>The token used by the contact participant to call the <a href="https://docs.aws.amazon.com/connect-participant/latest/APIReference/API_CreateParticipantConnection.html">CreateParticipantConnection</a> API. The participant token is valid for the lifetime of a contact participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWebRTCContactResponse) -> dict:
    out: dict = {}
    if "connection_data" in value:
        import capo_connect.types.connection_data

        out["ConnectionData"] = capo_connect.types.connection_data.serialize_json(
            value["connection_data"]
        )
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "participant_id" in value:
        out["ParticipantId"] = value["participant_id"]
    if "participant_token" in value:
        out["ParticipantToken"] = value["participant_token"]
    return out


def deserialize_json(data: dict) -> StartWebRTCContactResponse:
    out: StartWebRTCContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("ConnectionData") is not None:
        import capo_connect.types.connection_data

        out["connection_data"] = capo_connect.types.connection_data.deserialize_json(
            data["ConnectionData"]
        )
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    if data.get("ParticipantId") is not None:
        out["participant_id"] = data["ParticipantId"]
    if data.get("ParticipantToken") is not None:
        out["participant_token"] = data["ParticipantToken"]
    return out
