"""Generated from Smithy shape ``com.amazonaws.connectparticipant#CreateParticipantConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.bool
    import capo_connectparticipant.types.connection_type_list
    import capo_connectparticipant.types.participant_token


class CreateParticipantConnectionRequest(TypedDict, closed=True):
    type: NotRequired[
        "capo_connectparticipant.types.connection_type_list.ConnectionTypeList"
    ]
    """<p>Type of connection information required. If you need <code>CONNECTION_CREDENTIALS</code> along with marking participant as connected, pass <code>CONNECTION_CREDENTIALS</code> in <code>Type</code>.</p>"""
    participant_token: (
        "capo_connectparticipant.types.participant_token.ParticipantToken"
    )
    """<p>This is a header parameter.</p> <p>The ParticipantToken as obtained from <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html">StartChatContact</a> API response.</p>"""
    connect_participant: NotRequired["capo_connectparticipant.types.bool.Bool"]
    """<p>Amazon Connect Participant is used to mark the participant as connected for customer participant in message streaming, as well as for agent or manager participant in non-streaming chats.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantConnectionRequest) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connectparticipant.types.connection_type_list

        out["Type"] = capo_connectparticipant.types.connection_type_list.serialize_json(
            value["type"]
        )
    if "connect_participant" in value:
        out["ConnectParticipant"] = value["connect_participant"]
    return out


def deserialize_json(data: dict) -> CreateParticipantConnectionRequest:
    out: CreateParticipantConnectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_connectparticipant.types.connection_type_list

        out["type"] = (
            capo_connectparticipant.types.connection_type_list.deserialize_json(
                data["Type"]
            )
        )
    if data.get("ConnectParticipant") is not None:
        out["connect_participant"] = data["ConnectParticipant"]
    return out
