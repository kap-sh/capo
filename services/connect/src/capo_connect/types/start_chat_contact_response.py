"""Generated from Smithy shape ``com.amazonaws.connect#StartChatContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.connection_credentials
    import capo_connect.types.contact_id
    import capo_connect.types.participant_id
    import capo_connect.types.participant_token
    import capo_connect.types.streaming_id
    import capo_connect.types.websocket


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
    connection_credentials: NotRequired[
        "capo_connect.types.connection_credentials.ConnectionCredentials"
    ]
    """<p>The connection credentials for the chat participant. Returned only when the request includes <code>CONNECTION_CREDENTIALS</code> in <code>ConnectionTypes</code>.</p>"""
    websocket: NotRequired["capo_connect.types.websocket.Websocket"]
    """<p>The websocket for the chat participant. Returned only when the request includes <code>WEBSOCKET</code> in <code>ConnectionTypes</code>.</p>"""
    streaming_id: NotRequired["capo_connect.types.streaming_id.StreamingId"]
    """<p>The identifier of the streaming configuration enabled with the chat. Returned only when the request sets <code>ChatStreamingConfiguration</code>. Use this value to call <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StopContactStreaming.html">StopContactStreaming</a>.</p>"""


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
    if "connection_credentials" in value:
        import capo_connect.types.connection_credentials

        out["ConnectionCredentials"] = (
            capo_connect.types.connection_credentials.serialize_json(
                value["connection_credentials"]
            )
        )
    if "websocket" in value:
        import capo_connect.types.websocket

        out["Websocket"] = capo_connect.types.websocket.serialize_json(
            value["websocket"]
        )
    if "streaming_id" in value:
        out["StreamingId"] = value["streaming_id"]
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
    if data.get("ConnectionCredentials") is not None:
        import capo_connect.types.connection_credentials

        out["connection_credentials"] = (
            capo_connect.types.connection_credentials.deserialize_json(
                data["ConnectionCredentials"]
            )
        )
    if data.get("Websocket") is not None:
        import capo_connect.types.websocket

        out["websocket"] = capo_connect.types.websocket.deserialize_json(
            data["Websocket"]
        )
    if data.get("StreamingId") is not None:
        out["streaming_id"] = data["StreamingId"]
    return out
