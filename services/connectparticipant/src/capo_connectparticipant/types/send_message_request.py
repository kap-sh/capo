"""Generated from Smithy shape ``com.amazonaws.connectparticipant#SendMessageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connectparticipant.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectparticipant.types.chat_content
    import capo_connectparticipant.types.chat_content_type
    import capo_connectparticipant.types.client_token
    import capo_connectparticipant.types.participant_token


class SendMessageRequest(TypedDict, closed=True):
    content_type: "capo_connectparticipant.types.chat_content_type.ChatContentType"
    """<p>The type of the content. Possible types are <code>text/plain</code>, <code>text/markdown</code>, <code>application/json</code>, and <code>application/vnd.amazonaws.connect.message.interactive.response</code>. </p> <p>Supported types on the contact are configured through <code>SupportedMessagingContentTypes</code> on <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html">StartChatContact</a> and <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html">StartOutboundChatContact</a>.</p> <p> For Apple Messages for Business, SMS, and WhatsApp Business Messaging contacts, only <code>text/plain</code> is supported.</p>"""
    content: "capo_connectparticipant.types.chat_content.ChatContent"
    """<p>The content of the message. </p> <ul> <li> <p>For <code>text/plain</code> and <code>text/markdown</code>, the Length Constraints are Minimum of 1, Maximum of 1024. </p> </li> <li> <p>For <code>application/json</code>, the Length Constraints are Minimum of 1, Maximum of 12000. </p> </li> <li> <p>For <code>application/vnd.amazonaws.connect.message.interactive.response</code>, the Length Constraints are Minimum of 1, Maximum of 12288.</p> </li> </ul>"""
    client_token: NotRequired["capo_connectparticipant.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    connection_token: "capo_connectparticipant.types.participant_token.ParticipantToken"
    """<p>The authentication token associated with the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendMessageRequest) -> dict:
    out: dict = {}
    out["ContentType"] = value["content_type"]
    out["Content"] = value["content"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendMessageRequest:
    out: SendMessageRequest = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("SendMessageRequest.content_type required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("SendMessageRequest.content required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
